from django.db import models

# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Category_name
    
    class Meta:
        verbose_name_plural = "Categories"

class MenuItem(models.Model):
    Item_name = models.CharField(max_length=200)
    description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Item_name

class Review(models.Model):
    User_name = models.CharField(max_length=100)
    Description = models.TextField()
    Rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    Image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.User_name} - {self.Rating} stars"

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
