from django.urls import path
from . import views

# recipes:nome da rota
app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/<int:id>/", views.recipe, name="recipe"),
]
