from django.shortcuts import render, redirect
from django.views import View
from .forms import InteractionForm
from .models import Interaction
from model_manager.models import LLM

class InteractionView(View):
    def get(self, request):
        form = InteractionForm()
        return render(request, 'model_ask/interaction_form.html', {'form': form})

    def post(self, request):
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            # Here you would implement the logic to get a response from the LLM.
            # For demonstration, we will just echo the prompt.
            interaction.response = f"Response to '{interaction.prompt}' from model '{interaction.llm}'"
            interaction.save()
            return redirect('interaction_result', pk=interaction.pk)
        return render(request, 'model_ask/interaction_form.html', {'form': form})

class InteractionResultView(View):
    def get(self, request, pk):
        interaction = Interaction.objects.get(pk=pk)
        return render(request, 'model_ask/interaction_result.html', {'interaction': interaction})
