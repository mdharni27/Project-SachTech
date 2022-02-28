from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from APP1.models import Testimonial,Contact,Reservation,Profile,Order,Dishes,Category
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import random

# HOST='http://127.0.0.1:8000/'

# Create your views here.
def home(request):
   return render(request,"home.html")

def signup(request):
    context={}
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        check=User.objects.filter(username=email)
        if len(check)==0:
         usr=User.objects.create_user(email,email,password)
         usr.first_name=name
         usr.save()
         profile=Profile(user=usr)
         profile.save()
         context['status']=f"User {name} Registered Successfully!!"
        else:
            context['error']=f"A User with this email already exists!"    
    return render(request,"signup.html",context)   

def check_user(request):
    email = request.GET.get('usern')
    check = User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'message':'Not Exist'})
    else:
        return JsonResponse({'status':1,'message':'A user with this email already exists!'})

def services(request):
    return render(request,"services.html")

def signin(request):
    context={}
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        check_user=authenticate(username=email,password=password)       
        if check_user:
          login(request, check_user)
          if check_user.is_superuser or check_user.is_staff:
             return HttpResponseRedirect('/admin')
          return HttpResponseRedirect('/dashboard')
        else:
          context.update({'message':'Invalid Login Details!','class':'alert-danger','action':'open'})

    return render(request,"home.html",context)
    
    # return render(request,"header_footer.html")
 
def menu(request):
    context={}
    dishes = Dishes.objects.all()
    if "q" in request.GET:
        id = request.GET.get("q")
        dishes = Dishes.objects.filter(category__id=id)
        context['dish_category'] = Category.objects.get(id=id).name 
    context['dishes'] = dishes
    return render(request,"menu.html",context)    

def single_dish(request, id):
    context={}
    dish = get_object_or_404(Dishes, id=id)

    if request.user.is_authenticated: 
        cust = get_object_or_404(Profile, user__id = request.user.id)
        order = Order(customer=cust, item=dish)
        order.save()
        inv = f'INV0000-{order.id}'

        paypal_dict = {
            'business':settings.PAYPAL_RECEIVER_EMAIL,
            'amount':dish.price,
            'item_name':dish.name,
            'user_id':request.user.id,
            'invoice':inv,
            'currency_code':'INR',
            'notify_url':'http://{}{}'.format(settings.HOST, reverse('paypal-ipn')),
            'return_url':'http://{}{}'.format(settings.HOST,reverse('payment_done')),
            'cancel_url':'http://{}{}'.format(settings.HOST,reverse('payment_cancel')),
            }
        order.invoice_id = inv 
        order.save()
        request.session['order_id'] = order.id
        form = PayPalPaymentsForm(initial=paypal_dict)
        context.update({'dish':dish, 'form':form})
    return render(request,'dish.html', context)

def reservation(request):
    context={}
    if request.method=="POST":
        name=request.POST.get("name")
        em=request.POST.get("email")
        text=request.POST.get("text")
        phone=request.POST.get("phone")
        date=request.POST.get("date")
        obj=Reservation(name=name,email=em,text=text,phone=phone,date=date)
        obj.save()
        n=random.randint(100,300)
        nl='\n'
        context['message']=f"Dear {name}, Your table has been reserved!! Your  Table Number is {n}."
    return render(request,"reservations.html",context)

def team(request):
    return render(request,"team.html")

def testimonial(request):
      context={}
      if request.method=="POST":
        name=request.POST.get("name")
        em=request.POST.get("email")
        message=request.POST.get("message")
        obj=Testimonial(name=name,email=em,message=message)
        obj.save()
        context['message']="Dear "+name+" Thank you for your feedback!!"
        #return HttpResponse("Dear "+name+" Thank you for your time!!")
      return render(request,"testimonial.html", context)

def privacy(request):
    return render(request,"privacy.html")

def history(request):
    return render(request,"history.html")   

def contact(request):
    context={}
    if request.method=="POST":
       name=request.POST.get("name")
       em=request.POST.get("email")
       message=request.POST.get("message")
       obj=Contact(name=name,email=em,message=message)
       obj.save()
       context['message']=f"Dear {name}, Thank you for your time.We have received your question.."
    return render(request,"contactus.html",context)

def dashboard(request):
    context={}
    login_user = get_object_or_404(User, id = request.user.id)
    #fetch login user's details
    profile = Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile
    
    #update profile
    if "update_profile" in request.POST:
        print("file=",request.FILES)
        name = request.POST.get('name')
        add = request.POST.get('address')
       

        profile.user.first_name = name 
        profile.user.save() 
        profile.address = add 

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            profile.profile_pic = pic
        profile.save()
        context['status'] = 'Profile updated successfully!'
    
    #Change Password 
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')
                        
        check = login_user.check_password(c_password)
        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!' 
        else:
            context['status'] = 'Current Password Incorrect!'
    
    #My Orders 
    orders = Order.objects.filter(customer__user__id=request.user.id).order_by('-id')
    context['orders']=orders

    return render(request, "dashboard.html", context)    
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def payment_done(request):
    pid = request.GET.get('PayerID')
    order_id = request.session.get('order_id')
    order_obj = Order.objects.get(id=order_id)
    order_obj.status=True 
    order_obj.payer_id = pid
    order_obj.save()
    return render(request, 'payment_successfull.html') 
                                          
def payment_cancel(request):
    ## remove comment to delete cancelled order
     order_id = request.session.get('order_id')
     Order.objects.get(id=order_id).delete()
     return render(request, 'payment_failed.html') 

def hf(request):
    return render(request,"header_footer.html")