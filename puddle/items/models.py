from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    # This simulates an item's category
    name = models.CharField(max_length=255)

    class Meta():
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    # This represents an item on the website
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
