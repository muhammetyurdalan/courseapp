from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(req):
    #return HttpResponse("Ana sayfaya hoşgeldiniz")
    #app template(html sayfası) render edecez
    return render(req,"pagesFile/index.html")
def about(request):
   return render(request,"pagesFile/about.html")

def contact(req):
    return render(req,"pagesFile/contact.html")

# return HttpResponse("yazı yazılabilir")
#eğer templates içinde yeni bir klasöre views leri taşırsak hmtl ler diğer app lerde var mı diye aranıp bulunmasını engelleriz