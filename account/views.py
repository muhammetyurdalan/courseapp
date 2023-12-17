from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
#LOGIN_URL burayı gösterdiği için decoratorlerden buraya gelinir.ve GET requestte "next" ifadei olur
def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"account/login.html",{"error":"Yetkiniz bulunmamaktadır"})
    
    if request.method=="POST":
        username=request.POST["username"]     
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            nextUrl=request.GET.get("next",None)
            if nextUrl is None:
                return redirect('index_url')
            else:
                return redirect(nextUrl)
        else:
            return render(request,"account/login.html",{"error":"Kullanıcı adı veya şifresi hatalı!"})
    else:
        return render(request, 'account/login.html')

def user_register(request):
    
    if request.method=="POST":
        username=request.POST["username"]     
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        
        if repassword != password:
            return render(request,'account/register.html',
                          {
                              'error':'Şİfreler uyuşmuyor.',
                              "username":username,
                              "email":email 
                              })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'account/register.html',
                          {
                              "error":"Kullanıcı adı kullanılıyor.",
                              "username":username,
                              "email":email 
                              
                           })
        
        if User.objects.filter(email=email).exists():
            return render(request, 'account/register.html',
                          {
                            "error":"Email kullanılıyor.",
                            "username":username,
                            "email":email 
                            })
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('user_login_url')
        
    else:
        return render(request, 'account/register.html')

def user_logout(request):
    logout(request)
    return redirect("index_url")