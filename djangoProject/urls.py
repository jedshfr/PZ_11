from django.contrib import admin
from django.urls import path
from myNewProject import views
urlpatterns = [
    path('', views.first_page),
    path('second/', views.second_page),
    path('third/', views.third_page),
    path('fourth/', views.fourth_page),
    path('fifth/', views.fifth_page)
]