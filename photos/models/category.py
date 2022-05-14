from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_category(cls, id):
        return cls.objects.get(id=id)