from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def index(request):
    context = {
        "users" : User.objects.all()
        }
    return render(request, 'chating_app/index.html', context=context)

def room(request, other_user_id):
    return render(request, 'chating_app/room.html', {
        'room_name': other_user_id
    })