
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('random_recipe',views.random_recipe,name='random_recipe'),
    path('share_recipe',views.share_recipe,name='share_recipe'),
    path('users_recipe',views.users_recipe,name='users_recipe'),
    path('indian_dish',views.indian_dish,name='indian_dish'),
    path('user_auth/', views.user_auth, name='user_auth'),
    path('login', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.LogoutPage, name='Logout'),
    path('my_recipe',views.my_recipe,name='my_recipe'),
    path('delete_recipe/<int:id>',views.delete_recipe,name='delete'),
    path('edit_recipe/<int:id>',views.edit_recipe,name='edit'),
    path('search',views.search,name='search'),
]
