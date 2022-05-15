from .models import Category, Photo
from .forms import PhotoForm

from django.shortcuts import render, redirect


# Create your views here.

def gallery(request):
    categories = Category.get_all_categories()
    category_filter = request.GET.get('category')
    if category_filter:
        conditions = {
            'category__name': category_filter
        }
        photos = Photo.filter_photos_by_conditions(conditions)
    else:
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
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    context = {
        'form': form,
    }
    return render(request, 'photos/add.html', context)