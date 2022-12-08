from django.shortcuts import redirect, render
from django.db.models import Count, Q
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Cart, Product, Customer
from .forms import CustomeRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from Apps import forms



# Create your views here.
def Home(request):
    return render(request, "Apps/index.html")

def about(request):
    return render(request, "Apps/about.html")

def contact(request):
    return render(request, "Apps/contact.html")

class category(View):
    def get(self, request, val, *args, **kwargs,):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'Apps/category.html', locals())

class categoryTitle(View):
    def get(self, request, val, *args, **kwargs,):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'Apps/category.html', locals())

class productView(View):
    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        return render(request, 'Apps/productView.html', locals())
    
class CustomerRegistrationView(View):
    def get(self, request, *args, **kwargs):
        Forms = CustomeRegistrationForm()
        return render(request, 'Apps/CustomerRegistration.html', locals())
    def post(self, request, *args, **kwargs):
        Forms = CustomeRegistrationForm(request.POST)
        if Forms.is_valid():
            Forms.save()
            messages.success(request, "Congratulation! User Register Successfully.")
        else:
            messages.error(request, "invalid Input data.")
        return render(request, 'Apps/CustomerRegistration.html', locals())

      
# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         login = LoginForm()
#         return render(request, 'Apps/login.html', locals())

#     def post(self, request, *args, **kwargs):
#         login = LoginForm(request.POST)
#         if login.is_valid():
#             username = forms.cleaned_data.get('username')
#             password = forms.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, "You are now logged in as {username}.")
#             else:
#                 messages.error(request, "Invalid username & password.")
#         else:
#             messages.error(request, "Invalid username & password.")
#         login = LoginForm()
#         return render(request, 'Apps/login.html', locals())
        
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        form = CustomerProfileForm()
        return render(request, 'Apps/profile.html', locals())

    def post(self, request, *args, **kwargs):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile save successfully.")
        else:
            messages.error(request,"Invalid input data. please try again")
        return render(request, 'Apps/profile.html', locals())
    

def address(request):
    address = Customer.objects.filter(user = request.user)
    return render(request, 'Apps/address.html', locals())

class UpdateAddressView(View):
    def get(self, request, pk, *args, **kwargs):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'Apps/updateAddress.html', locals())

    def post(self, request, pk, *args, **kwargs):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk = pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']

            add.save()
            messages.success(request,"Congratulation! Your Profile update successfully.")
        else:
            messages.error(request,"Invalid input data. please try again")
        return redirect('address')

    
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discount_price
        amount = amount + value
    totalamount = amount + 40;
    return render(request, 'Apps/addtocart.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity':c.quantity,
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discount_price
            amount = amount + value
        totalamount = amount + 40
        data = {
            'amount': amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
