"""
URL configuration for llmask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from sohbat import views as sohbat_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "create_interaction/",
        sohbat_views.create_interaction,
        name="create_interaction",
    ),
    path("get_llms/", sohbat_views.get_llms, name="get_llms"),
    path(
        "get_system_prompts/",
        sohbat_views.get_system_prompts,
        name="get_system_prompts",
    ),
]
