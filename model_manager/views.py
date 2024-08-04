from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import LLM

class LLMListView(ListView):
    model = LLM
    template_name = 'llm_app/llm_list.html'

class LLMCreateView(CreateView):
    model = LLM
    fields = ['provider_name', 'model_name']
    template_name = 'llm_app/llm_form.html'
    success_url = reverse_lazy('llm_list')

class LLMDeleteView(DeleteView):
    model = LLM
    template_name = 'llm_app/llm_confirm_delete.html'
    success_url = reverse_lazy('llm_list')

