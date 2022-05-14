from django.db import models
from .category import Category
from django.shortcuts import render, get_object_or_404


class Photo(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self) -> str:
        return self.description

    @classmethod
    def get_all_photos(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_photo(cls, id):
        return get_object_or_404(cls, pk=id)