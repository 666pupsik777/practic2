from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('register/', views.RegisterUser.as_view(), name='register'),  # Регистрация
    path('login/', views.LoginUser.as_view(), name='login'),  # Вход
    path('logout/', LogoutView.as_view(), name='logout'),   # Выход
    path('profile/', views.ProfileUser.as_view(), name='profile'),  # Профиль
    path('home/', views.index, name='home'),  # Домой главная
]

