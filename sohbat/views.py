from django.shortcuts import render, redirect
from .models import LLM, SystemPrompt, UserPrompt, Interaction
from .llmapis import get_response

def create_interaction(request):
    if request.method == "POST":
        llm = LLM.objects.get(id=request.POST['llm'])
        system_prompt = SystemPrompt.objects.get(id=request.POST['system_prompt'])
        user_prompt = UserPrompt.objects.get(id=request.POST['user_prompt'])
        random_seed = int(request.POST['random_seed'])
        response = get_response(
            llm=llm,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            random_seed=random_seed
        )
        
        interaction = Interaction.objects.create(
            llm=llm,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response=response,
            random_seed=random_seed
        )
        return redirect('show_interaction', interaction_id=interaction.id)

    llms = LLM.objects.all()
    system_prompts = SystemPrompt.objects.all()
    user_prompts = UserPrompt.objects.all()
    interactions = Interaction.objects.all()
    
    return render(request, 'interaction_form.html', {
        'llms': llms,
        'system_prompts': system_prompts,
        'user_prompts': user_prompts,
        'interactions': interactions,
        'default_seed': Interaction._meta.get_field("random_seed").get_default()
    })


def show_interaction(request, interaction_id):
    interaction = Interaction.objects.get(id=interaction_id)
    return render(request, 'interaction_detail.html', {'interaction': interaction})
