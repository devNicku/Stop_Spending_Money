from django.urls import path
from . import views

urlpatterns = [

#Render Routes
    path('', views.index),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('goals', views.goals),
    path('about', views.about),

#Action/Redirect Routes
    path('logout', views.logout),
    path('reg_user', views.register_user),
    path('log_in', views.log_in),
    path('goals/add_goal',views.add_goal)
]