from .models import Account
# from django.shortcuts import render
from os import access
from django.contrib import messages
from django.contrib.auth import( 
                                authenticate,
                                logout,
                                login,
                                )
from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm
from products.models import Product

def home(request):
    context = {}
    data = Product.objects.all()
    context['products'] = data
    return render(request, "store/items/list.html", context )



def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                phone = form.cleaned_data['phone'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
        
        else:
            print(request.POST, form.errors)
            form = RegistrationForm()
            return render(request, 'account/register.html', {'form': form})
    
    else:
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        print("user authenticated")
        return redirect('products:products_list')
    if request.POST:
        form = LoginForm(request.POST)
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(phone=phone, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("products:products_list")
        else:
            print(request.POST, form.errors)
            return render(request, 'account/login.html', {'login_form': form})
            messages.error(request, 'please Correct Below Errors')

    else:
        form = LoginForm()
        context['login_form'] = form
        return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return render(request, "account/logout.html")


def profile_view(request, phone):
    user = Account.objects.get(phone=phone)
    return render(request, 'account/profile.html', {"user":user})


def about_page(request):
    return render(request, 'about_us.html')
