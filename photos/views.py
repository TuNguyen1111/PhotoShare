from .models import Category, Photo

from django.shortcuts import render, get_object_or_404


# Create your views here.

def gallery(request):
    categories = Category.get_all_categories()
    photos = Photo.get_all_photos()
    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, 'photos/gallery.html', context)

def view_photo(request, pk):
    photo = Photo.get_specific_photo(pk)
    context = {
        'photo': photo
    }
    return render(request, 'photos/photo.html', context)

def add_photo(request):
    return render(request, 'photos/add.html')