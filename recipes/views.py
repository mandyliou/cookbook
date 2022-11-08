from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeStep
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author=request.user)
    context={
        "show_recipe": recipes,
    }
    return render(request, "recipes/list.html", context)

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "show_recipe": recipe,
    }
    return render(request, "recipes/detail.html", context)

def recipe_list(request):#get
    recipes = Recipe.objects.all()
    context = {
        "show_recipe": recipes,
    }
    return render(request, "recipes/list.html", context)

@login_required
def create_recipe(request):
    if request.method == "POST": #create has POST no id
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return (redirect("recipe_list"))
    else:
        form = RecipeForm()
        context = {
            "form": form,
        }
        return render(request, "recipes/create.html", context)

def edit_recipe(request, id):#view bc POST and id
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=recipe)
        context = {
            "recipe": recipe,
            "form": form,
        }
        return render(request, "recipes/edit.html", context)

# from django.shortcuts import render, get_object_or_404
# from recipes.models import Recipe

# def show_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     context = {
#         "recipe_object": recipe,
#     }
#     return render(request, "recipes/detail.html", context)

# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     context = {
#         "recipe_list": recipes,
#     }
#     return render(request, "recipes/list.html", context)

# def create_recipe(request):
#     if request.method == "POST":
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = RecipeForm()
#         context = {"form": form}
#     return render(request, "recipes/create.html", context)

# Create your views here.
# create context dictionary containing a key for each recipe
# def show_recipe_list(request):
#     dict = {}
#     for i in range(len(Recipe.objects.all())):
#         dict["recipe_object_"+str(i)] = Recipe.objects.all()[i]
#     context = dict
#     return render(request, "recipes/list.html", context)
