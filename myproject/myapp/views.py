from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
 
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the 'home' URL name
        else:
            # Authentication failed, render the login form again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # GET request, render the login form
        return render(request, 'login.html')


def create_tenant_view(request):
    return render(request, 'create_tenant.html')

def create_vrf_view(request):
    return render(request, 'create_vrf.html')
    
def BD_view(request):
    return render(request,'BD.html')    
def vlanpool_view(request):
    return render(request,'vlanpool.html') 
def AEP_view(request):
    return render(request,'AEP.html')    

def IGP_view(request):
    return render(request,'IPG.html')
    
def CIP_view(request):
    return render(request,'CIP.html')    

def SP_view(request):
    return render(request,'SP.html')    
    
def SWP_view(request):
    return render(request,'SWP.html') 

def S1_view(request):
    return render(request,'S1.html') 

def S2_view(request):
    return render(request,'S2.html')  

def Inv_view(request):
    return render(request,'Inv.html')      
def L3OUT_view(request):
    return render(request,'L3OUT.html')               
