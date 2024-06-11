"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('create_tenant/', views.create_tenant_view, name='create_tenant'),
     path('create_vrf/', views.create_vrf_view, name='create_vrf') , 
	 path('create_bd/', views.BD_view , name='BD') ,
path('create_vlanpool/', views.vlanpool_view , name='vlanpool') , 

path('create_AEP/', views.AEP_view , name='AEP') , 

path('create_IGP/', views.IGP_view , name='IGP'), 
path('CIP/', views.CIP_view , name='CIP') , 

path('SP/', views.SP_view , name='SP') , 

path('create_SWP/', views.SWP_view , name='SWP') , 


path('Profil_select/', views.S1_view , name='S1') ,

path('create_switch_profil/', views.S2_view , name='S2') , 

path('create_Inv/', views.Inv_view , name='Inv') ,
path('create_L3OUT/', views.L3OUT_view , name='L3OUT') 
]



