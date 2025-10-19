from django.shortcuts import render, redirect
from .models import Renter
from django.contrib.auth.models import User

def renter_list(request):
    renters = Renter.objects.all()
    return render(request, 'renter/renter_list.html', {'renters': renters})

def renter_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = User.objects.create_user(username=username, password=password)
        Renter.objects.create(user=user, phone=phone)
        return redirect('renter_list')
    return render(request, 'renter/renter_create.html')