from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from .models import LLM, SystemPrompt, UserPrompt, Interaction
from .llmapis import get_response


def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        key = list(kwargs.keys())[0]
        value = kwargs[key]
        return JsonResponse(
            {"error": f"{model.__name__} with {key} '{value}' does not exist."},
            status=404,
        )


@csrf_exempt
def get_llms(request):
    llms = LLM.objects.all()
    return JsonResponse([llm.slug for llm in llms], safe=False)


@csrf_exempt
def get_system_prompts(request):
    system_prompts = SystemPrompt.objects.all()
    return JsonResponse(
        [system_prompt.name for system_prompt in system_prompts], safe=False
    )


@csrf_exempt
def create_interaction(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

    # Check for required parameters
    required_params = ["llm", "system_prompt", "user_prompt", "random_seed"]
    for param in required_params:
        if param not in request.POST:
            return JsonResponse(
                {"error": f"Missing required parameter: {param}"}, status=400
            )

    llm_response = get_object_or_404(LLM, slug=request.POST["llm"])
    if isinstance(llm_response, JsonResponse):
        return llm_response
    llm = llm_response

    system_prompt_response = get_object_or_404(
        SystemPrompt, name=request.POST["system_prompt"]
    )
    if isinstance(system_prompt_response, JsonResponse):
        return system_prompt_response
    system_prompt = system_prompt_response

    user_prompt, _ = UserPrompt.objects.get_or_create(
        prompt=request.POST["user_prompt"]
    )

    try:
        random_seed = int(request.POST["random_seed"])
    except ValueError:
        return JsonResponse({"error": "random_seed must be an integer."}, status=400)

    interaction, created = Interaction.objects.get_or_create(
        llm=llm,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        random_seed=random_seed,
    )
    if created:
        interaction.response = get_response(
            llm, system_prompt, user_prompt, random_seed
        )
        interaction.save()

    return JsonResponse(model_to_dict(interaction), status=201 if created else 200)
