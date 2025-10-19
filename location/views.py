from django.shortcuts import render, redirect
from .models import Location
from owner.models import Owner
from django.shortcuts import get_object_or_404

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location/location_list.html', {'locations': locations})

def location_create(request):
    owners = Owner.objects.all()
    if request.method == 'POST':
        owner_id = request.POST['owner']
        title = request.POST['title']
        address = request.POST['address']
        price_per_night = request.POST['price_per_night']
        available = 'available' in request.POST
        description = request.POST['description']
        owner = Owner.objects.get(id=owner_id)
        Location.objects.create(
            owner=owner,
            title=title,
            address=address,
            price_per_night=price_per_night,
            available=available,
            description=description
        )
        return redirect('location_list')
    return render(request, 'location/location_create.html', {'owners': owners})

def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    owners = Owner.objects.all()
    if request.method == 'POST':
        location.owner = Owner.objects.get(id=request.POST['owner'])
        location.title = request.POST['title']
        location.address = request.POST['address']
        location.price_per_night = request.POST['price_per_night']
        location.available = 'available' in request.POST
        location.description = request.POST['description']
        location.save()
        return redirect('location_list')
    return render(request, 'location/location_update.html', {'location': location, 'owners': owners})

def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, 'location/location_delete.html', {'location': location})


