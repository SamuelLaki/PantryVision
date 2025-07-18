from django.urls import path
from . import views


urlpatterns = [
    path('', views.image_view, name = 'upload'),
    path('recipes', views.recipes, name = 'recipes'),
    path('success', views.success, name = 'success')
]