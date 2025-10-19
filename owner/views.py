from django.shortcuts import render, redirect
from .models import Owner
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner/owner_list.html', {'owners': owners})

def owner_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = User.objects.create_user(username=username, password=password)
        Owner.objects.create(user=user, phone=phone)
        return redirect('owner_list')
    return render(request, 'owner/owner_create.html')
    
    def owner_update(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        owner.phone = request.POST['phone']
        owner.save()
        return redirect('owner_list')
    return render(request, 'owner/owner_update.html', {'owner': owner})

def owner_delete(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list')
    return render(request, 'owner/owner_delete.html', {'owner': owner})