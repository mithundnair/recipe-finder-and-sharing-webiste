from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Recipes
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import requests
# Create your views here.


#For User Authentication

def user_auth(request):

    return render(request,'LogReg.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
            # messages.add_message(request, messages.INFO, "Hello world.")
           

    return render(request, 'LogReg.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user = User.objects.create_user(username, email, password)
        my_user.save()

        return redirect('user_login')

    return render(request, 'LogReg.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')



def home(request):
    return render(request,"front.html")

def random_recipe(request):

    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    data=response.json()
    food_name=(data['meals'][0]['strMeal'])
    cuisine=(data['meals'][0]['strArea'])
    cooking_instructions=(data['meals'][0]['strInstructions'])
    food_image=(data['meals'][0]['strMealThumb'])
    food_tags=(data['meals'][0]['strTags'])
    Ingrediants=(data['meals'][0]['strIngredient1'])
    Measures=(data['meals'][0]['strMeasure1'])
   
    # print(data['meals'][0]['strMealThumb'])
    ingredients = [data['meals'][0][f'strIngredient{i}'] for i in range(1, 21) if data['meals'][0][f'strIngredient{i}']]

    non_empty_ingredients = [ingredient for ingredient in ingredients if ingredient and ingredient.lower() not in ['null', '']]
    random_meal={
        "food_name":food_name,
        "cuisine":cuisine,
        "cooking_instructions":cooking_instructions,
        "food_image":food_image,
        "food_tags":food_tags,
        "ingredients":non_empty_ingredients,
        # "Measures":Measures,

    }
    return render(request,"randomrecipe.html",random_meal)

def search(request):

    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s")
    data = response.json()

    fud_name = (data['meals'][0]['strMeal'])
    category = (data['meals'][0]['strCategory'])
    cuisine = (data['meals'][0]['strArea'])
    instructions = (data['meals'][0]['strInstructions'])
    fud_image = (data['meals'][0]['strMealThumb'])
    ingredients = (data['meals'][0]['strIngredient1'])

    # print(data['meals'][0]['strArea'])
    
    ingredients = [data['meals'][0][f'strIngredient{i}'] for i in range(1, 21) if data['meals'][0][f'strIngredient{i}']]

    non_empty_ingredients = [ingredient for ingredient in ingredients if ingredient and ingredient.lower() not in ['null', '']]

    All_meals = {
        "fud_name":fud_name,
        "category":category,
        "cuisine":cuisine,
        "instructions":instructions,
        "fud_image":fud_image,
        "ingredients":non_empty_ingredients,
    }

    return render(request,'Search.html',All_meals)

@login_required
def my_recipe(request):

    user_recipes = Recipes.objects.filter(author=request.user)
    return render(request, "myrecipe.html",{"current_user_recipe":user_recipes})

def indian_dish(request):
    return render(request, 'Indian.html')

@login_required
def share_recipe(request):

    if request.POST:
        food_name=request.POST.get('food_name')
        recipe_description=request.POST.get('recipe_description')
        # Get the current user
        author = request.user
        recipe_obj=Recipes(author=author,food_name=food_name,recipe=recipe_description)
        recipe_obj.save()
        return redirect('users_recipe')


    return render(request,"Your.html")

def users_recipe(request):
    users_recipe=Recipes.objects.all()

    return render(request,"user.html",{"users_recipe":users_recipe})


def delete_recipe(request,id):
    recipe=get_object_or_404(Recipes,pk=id)
    recipe.delete()

    return redirect('my_recipe')


def edit_recipe(request,id):
    recipe_to_edit=get_object_or_404(Recipes,pk=id)    
    if request.POST:

        recipe_to_edit.food_name=request.POST.get('food_name')
        recipe_to_edit.recipe=request.POST.get('recipe_description')
        recipe_to_edit.save()
        return redirect('my_recipe')
   
    return render(request,'edit_recipe.html',{"recipe_to_edit":recipe_to_edit})