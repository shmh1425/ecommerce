from django.shortcuts import render ,redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse ,JsonResponse
from .models import storetype,items,itemsdetails,cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login ,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginUserForm


# Create your views here.

def page(request):
    templates=loader.get_template('page.html')
    return HttpResponse(templates.render({'request':request}))

def index(request):
    templates=loader.get_template('index.html')
    return HttpResponse(templates.render({'request':request}))

def listitems(request):
    p=items.objects.filter(st_id=1)
    template=loader.get_template('listitems.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def listitemsbedroom(request):
    p = items.objects.filter(st_id=2)
    template=loader.get_template('listitemsbedroom.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def lightindoor(request):
    p=items.objects.filter(st_id=3)
    template=loader.get_template('lightindoor.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def lightoutdoor(request):
    p=items.objects.filter(st_id=4)
    template=loader.get_template('lightoutdor.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def details(request, id):    
    template = loader.get_template('details.html')
    data = itemsdetails.objects.select_related('items').get(items__id=id)
    data.total = data.tax * data.items.price + data.items.price
    return HttpResponse(template.render({'data': data}, request))

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        id = request.POST.get("id")  # Get the item ID from the request
        item = get_object_or_404(items, id=id)  # Fetch the corresponding items instance

        p = cart(itemsid=item)  # Assign the items instance to the itemsid field
        p.save()

        # Count the number of items in the cart
        count = cart.objects.count()
        request.session["cart"] = count  # Store the count in the session

        return JsonResponse({'count': count})
    
@login_required(login_url='/auth_login/')
def checkout(request,id):
     
      template=loader.get_template('checkout.html')
      data=itemsdetails.objects.select_related('items').get(items__id=id) 
      print(data)
      data.total = data.tax * data.items.price + data.items.price
      return HttpResponse(template.render({'data':data,'request':request}))

@csrf_exempt
def auth_login(request):
     form=LoginUserForm()
     if request.method=="POST" :
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password) #check if username in DB or not
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'checkout.html')
     context={'form':form}
     return render(request,'auth_login.html',context)

@csrf_exempt
def auth_register(request):
   template=loader.get_template('auth_register.html')
   form=CreateUserForm()
   if request.method=="POST":
       form=CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('auth_login')
   context={'registerform':form}
   return HttpResponse(template.render(context=context))
