from django.urls import path
from . import views

urlpatterns = [
    path('', views.LLMListView.as_view(), name='llm_list'),
    path('add/', views.LLMCreateView.as_view(), name='llm_add'),
    path('delete/<int:pk>/', views.LLMDeleteView.as_view(), name='llm_delete'),
]

