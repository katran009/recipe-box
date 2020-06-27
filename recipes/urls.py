from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipeadd/', views.recipeadd, name="recipe_add"),
    path('authoradd/', views.authoradd, name="author_add"),
    path('recipedetail/<int:id>/', views.recipe_detail, name="recipe_detail"),
    path('author/<int:id>/', views.author_detail, name="author_detail"),
    path('login/', views.loginview, name="login_url"),
    path('logout/', views.logoutview, name="logout_url"),
    path('register/', views.user_create, name="create_url")
    
]
