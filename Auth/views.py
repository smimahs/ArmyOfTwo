from django.shortcuts import render
from django.http import HttpResponse
from .models import Clients,Post,Product
from django.core.mail import EmailMessage
from Auth.forms import SignUpForm,SignInForm
from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404


# Create your views here.
def checkLogin(request):
    if not 'login' in request.session.keys():
        request.session['login']=False

def index(request):
    checkLogin(request)
    print(request.session.keys())
    return render(request,'index.html',{'login':request.session['login']})

def signUp(request):
    if request.method == 'GET':
        form=SignUpForm()

    elif request.method == 'POST':
        
        email=request.POST.get("email")
        form = SignUpForm(request.POST)
        if form.is_valid():
            if (not Clients.objects.filter(email=email).exists()):
                name=request.POST.get("name")
                password=request.POST.get("password")
                cpassword=request.POST.get("cpassword")
                user = Clients(name=name, email=email, password=password, cpassword=cpassword, is_active=False)
                user.save()
                #email = EmailMessage('Activation Email', 'Body', to=[email])
                #email.send() 
                return redirect(signIn)

    return render(request,'signup.html', {"form": form})   

'''
def signUpEmployee(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        email=request.POST.get("email")
        if (not Employer.objects.get(email=email)):
            name=request.POST['name']
            companyName=request.POST['companyName']
            pasword=request.POST['pasword']
            cpasword=request.POST['cpasword']
            user = Employer(name=name, companyName=companyName, email=email, pasword=pasword, cpasword=cpasword, is_active=False)
            user.save()  
            email = EmailMessage('Activation Email', 'Body', to=[email])
            email.send()          
'''

def signIn(request):
    if request.method == 'GET':
        form=SignInForm()

    elif request.method == 'POST':       
        email=request.POST.get("email")
        form = SignInForm(request.POST)
        if form.is_valid():
            if (Clients.objects.filter(email=email).exists()):
                password=request.POST.get("password")
                user=Clients.objects.filter(email=email).first()
                if(user.password == password):
                    request.session['login']=True
                    request.session['email']=email
                    return redirect(index)
         
    return render(request,'signin.html', {"form": form})

def logout(request):
    request.session['login']=False
    del request.session['email']
    return redirect(signIn)

def blog(request):
    checkLogin(request)
    posts=Post.objects.all()
    return render(request,'blog.html',{'posts':posts,'login':request.session['login']})

def post(request,slug):
    checkLogin(request)
    return render(None,'post.html', {'post':get_object_or_404(Post,slug=slug),'login':request.session['login']})

def shop(request):
    checkLogin(request)
    products=Product.objects.all()
    return render(request,'shop.html',{'products':products,'login':request.session['login']})

def product(request,slug):
    checkLogin(request)
    return render(None,'product.html', {'product':get_object_or_404(Product,slug=slug),'login':request.session['login']})

def getProduct():
    products=Product.objects.all()
    return products




