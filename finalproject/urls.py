"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from APP1 import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('check_user/',views.check_user,name="check_user"),
    path('login',views.signin,name="login"),
    path('menu/',views.menu,name="menu"),
    path('services/',views.services,name="services"),
    path('reservation/',views.reservation,name="reservation"),
    path('team/',views.team,name="team"),
    path('testimonials/',views.testimonial,name="testimonial"),
    path('privacy_policy/',views.privacy,name="privacy"),
    path('aboutus/',views.history,name="history"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dish/<int:id>/', views.single_dish, name='dish'),
    path('logout/',views.user_logout,name="logout"),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
    path('hf/',views.hf)

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

