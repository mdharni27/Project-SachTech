from django.contrib import admin
from APP1.models import Testimonial,Dishes,Contact,Reservation,Profile,Order,Category
# Register your models here.
admin.site.site_header="FoodPlanet | Admin"

class TestimonialAdmin(admin.ModelAdmin):
     list_display=['id','name','email','message']
     list_filter=['name','email']
     list_editable=['name']
     search_fields=['name','email']
admin.site.register(Testimonial,TestimonialAdmin)

class DishesAdmin(admin.ModelAdmin):
     list_display=['id','name','price','added_on','updated_on']

admin.site.register(Dishes,DishesAdmin)

class ContactAdmin(admin.ModelAdmin):
     list_display=['id','name','email','message']
     list_filter=['name','email']
     list_editable=['name'] 
     search_fields=['name','email']
admin.site.register(Contact,ContactAdmin)

class ReservationAdmin(admin.ModelAdmin):
     list_display=['id','name','phone','email','date','time','text']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']
admin.site.register(Category,CategoryAdmin)    
admin .site.register(Reservation,ReservationAdmin)
admin.site.register(Profile)     
admin.site.register(Order)
