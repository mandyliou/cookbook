# from django.forms import ModelForm

# from .models import Recipe

# class RecipeForm(ModelForm):
#         class Meta:
#             model= Recipe
#             fields = ["title", "picture", "description"]


from django.forms import ModelForm

from .models import Recipe, Ingredient

class RecipeForm(ModelForm):
    # email_address = forms.EmailField(max_length=300)
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
            "stars"
        ]

class IngredientForm(ModelForm):
    # email_address = forms.EmailField(max_length=300)
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "food_item",
            "recipe",
        ]
