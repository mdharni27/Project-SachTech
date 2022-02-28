from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Testimonial(models.Model):
     name=models.CharField(max_length=250)
     email=models.EmailField(unique=True)
     message=models.TextField()

     def __str__(self):
        return self.name
     class Meta:
          verbose_name_plural="Testimonial Table"          

class Dishes(models.Model):
   name=models.CharField(max_length=250)
   image=models.ImageField(upload_to='dishes')
   ingredients=models.TextField()
   details = models.TextField(blank=True)
   #category = models.ForeignKey(Category, on_delete=models.CASCADE)
   price = models.FloatField()
   discounted_price = models.FloatField(blank=True)
   is_available = models.BooleanField(default=True)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.name 

   class Meta:
        verbose_name_plural ="Dish Table"    

class Contact(models.Model):
     name=models.CharField(max_length=250)
     email=models.EmailField(unique=True)
     message=models.TextField()
     
     def __str__(self):
       return self.name

     class Meta:
          verbose_name_plural="Contact Table"  
    
class Reservation(models.Model):
     name=models.CharField(max_length=250)
     email=models.EmailField()
     phone=models.PositiveIntegerField()
     date=models.DateField()
     time=models.TimeField(auto_now=True)
     text=models.TextField()
     
     def __str__(self):
          return self.name
     
     class Meta:
          verbose_name_plural="Reservation Table"

class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     profile_pic = models.ImageField(upload_to='profiles', null=True, blank=True)
     address=models.TextField(null=True)
     updated_on=models.DateTimeField(auto_now=True)
     # contact_number=models.CharField(max_length=15)
     def __str__(self):
          return self.user.first_name

     class Meta:
          verbose_name_plural="Profile Table"    

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    invoice_id = models.CharField(max_length=100, blank=True)
    payer_id = models.CharField(max_length=100, blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.user.first_name

    class Meta:
        verbose_name_plural = "Order Table"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/%Y/%m/%d")
    icon = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name