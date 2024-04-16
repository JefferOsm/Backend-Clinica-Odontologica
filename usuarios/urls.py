from django.urls import path
from . import views
app_name = 'usuarios'


urlpatterns = [
    path('login/', views.login, name='Login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]