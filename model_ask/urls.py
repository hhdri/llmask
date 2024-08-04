from django.urls import path
from .views import InteractionView, InteractionResultView

urlpatterns = [
    path('', InteractionView.as_view(), name='interaction_form'),
    path('result/<int:pk>/', InteractionResultView.as_view(), name='interaction_result'),
]
