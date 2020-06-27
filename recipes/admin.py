from django.contrib import admin

# Register your models here.
from recipes.models import Author, RecipeItem

admin.site.register(Author)
admin.site.register(RecipeItem)
