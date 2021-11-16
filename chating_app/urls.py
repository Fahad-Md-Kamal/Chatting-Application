from django.urls import path, include

from . import views

app_name = 'chat_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:other_user_id>/', views.room, name='room'),

]