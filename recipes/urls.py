
from django.urls import path
# import show_recipe from views
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe, my_recipe_list

# "recipes" is the URL (localhost:8000/recipes)
# show_recipe is our view function name
urlpatterns = [
    path("", recipe_list),
    path("recipes/", recipe_list, name="recipe_list"),#specify the view we want to handle out logic
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("mine/", my_recipe_list, name="my_recipe_list"),
]

#name is django to find it
