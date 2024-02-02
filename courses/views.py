from datetime import date
import os
import random
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from courses.forms import CourseCreateForm,CourseEditForm
from .models import Categories, Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

# data={
#     "programlama":"Pogramlama kursu Listesi",
#     "web-gelistirme":"Web Gelistirme kursu Listesi",
#     "mobil-programlama":"Mobil Pogramlama kursu Listesi"
# }

# db={
#     "courses":[
#         {"title":"Javascript Kursu",
#          "description":"Javascript Kurs Açıklaması",
#          "slug":"javascript-course",
#          "imageUrl":"js.jpeg",
#          "date":date(2023,10,10),
#          "isActive":True,
#          "isUptaded":False
            
#             },
#         {"title":"Python Kursu",
#          "description":"Python Kurs Açıklaması",
#          "slug":"python-course",
#          "imageUrl":"python.png",
#          "date":date(2023,10,10),
#          "isActive":False,
#          "isUptaded":False
#             },
#         {"title":"Java kursu",
#          "description":"Java Kurs Açıklaması",
#          "slug":"java-course",
#          "imageUrl":"java.jpg",
#          "date":date(2023,10,10),
#          "isActive":True,
#          "isUptaded":True
#             }
#     ],
#     "categories":[{"id":1,"name":"Programlama","slug":"programlama"},
#                   {"id":2,"name":"Web Geliştirme","slug":"web-gelistirme"},
#                   {"id":3,"name":"Mobil Programlama","slug":"mobil-programlama"}]
# }

# #dinamik olarak html etiketleri oluşturduk
# def course(req):
#     list_item=""
#     course_list=list(data.keys())
#     for item in course_list:
#         redirect_url=reverse('courses_by_category',args=[item])
#         list_item+=f"<li><a href='{redirect_url}'>{item}</a></li>"
    
#     html=f"<ul>{list_item}</ul>"
#     return HttpResponse(html)






def details(req,course_slug):
    # try:
    #     course=Course.objects.get(slug=course_slug)
    # except:
    #     raise Http404()
    #fillTheSlug()   bu fonksiyonu slug alanını doldurmak için yazdım
    
    #yukardaki kodun kısaltılmışı aşağıdaki metotdur
    course=get_object_or_404(Course,slug=course_slug)
    
    context={
        "course":course
    }
    
    return render (req,"details.html",context)


# def create_course(request):
#     selectedCategories=[]
#     categories=Categories.objects.all()
#     if request.method=="POST":
#         title=request.POST["title"]
#         imageUrl=request.POST["imageUrl"]
#         description=request.POST["description"]
#         isActive=request.POST.get("isActive",False)#default değer ile kullanım
#         for cat in categories:
#             isCatOn=request.POST.get(cat.slug,False)
#             if isCatOn=="on":
#                 selectedCategories.append(cat.name)
#                 print(selectedCategories)
        
#         if isActive== "on":
#             isActive=True
        
        
#         kurs=Course(title=title,imageUrl=imageUrl,description=description,isActive=isActive)
#         #kurs.categories.add(selectedCategories)
        
#         kurs.save()
        
#         return redirect("/course")
    
#     return render(request,"create_course2.html",{"categories":categories})

def is_Admin(user):
    return user.is_superuser

@user_passes_test(is_Admin)
def create_course(request):
    if request.method=="POST":
        form=CourseCreateForm(request.POST)
        
        if form.is_valid():
            kurs=Course(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                imageUrl=form.cleaned_data["imageUrl"],
                isActive=form.cleaned_data["isActive"]
            )
            kurs.save()
            #form.save() eğer model form kullandıysak tek satırla da kayıt yapılabilir
            return redirect('/course')   
             
    form=CourseCreateForm()
    return render(request,"create_course.html",{"form":form})


#user_pases_test sayesinde sadece admin olanlar bu metotu kullanabilecekler
#is_admin fonksiyonu çağrılır ve ordan true dönerse fonk çalıştırılır
#Aslında bu view çağrıldığında önce LOGIN_URL deki url e gidilir sonra isadmin çağrılır kontrol yapılır
@user_passes_test(is_Admin)
def edit_course(request,id):
    course=get_object_or_404(Course,pk=id)
    if request.method=="POST":
        form=CourseEditForm(request.POST,instance=course)
        form.save()
        return redirect("course_list_url")
    else:
        form=CourseEditForm(instance=course)
        
    
    return render(request,"edit_course.html",{"form":form})

@user_passes_test(is_Admin)
def delete_course(req,id):
    course=get_object_or_404(Course,pk=id)
    if req.method=="POST":
        #Course.objects.get(pk=id).delete() şeklinde de yazılabilir
        course.delete()
        return redirect("course_list_url")
    
    return render(req,"delete_course.html",{"course":course})

def upload(request):
    if request.method == "POST":
        uploaded_images = request.FILES.getlist("images")
        for file in uploaded_images:
            handle_uploaded_files(file)
        
        return render(request,"success.html")
    return render(request,"upload.html")

def handle_uploaded_files(file):
    number=random.randint(1,9999)
    filename,file_extention=os.path.splitext(file.name)
    name=filename+"_"+str(number)+file_extention
    with open("temp/"+name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

#login required sayesinde sadece login olunduğunda nu metto kullanılabilecek
@login_required()            
def course_list(req):
    courses=Course.objects.all()
    return render(req,"course_list.html",{"courses":courses})



def search(req):
    try:
        if "q" in req.GET and req.GET["q"] !="":
            categories=Categories.objects.all()
            search=req.GET.get("q")
            courses=Course.objects.filter(isActive=1,title__contains=search).order_by("-date")
        else:
            return redirect("/course")
        
        
        p=Paginator(courses,2)
        page=req.GET.get("page",1)
        page_obj=p.page(page)
        
        
        return render(req,'search.html',{"page_obj":page_obj,"categories":categories})
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")#sayfa bulunamadıysa status=404

# def mobiluygulamalar(req):
#     return HttpResponse("Mobil Uygulamalar sayfası")

# def getCoursesByCategoryName(req,category_name):
#     text=""
#     if(category_name=="web-gelistirme"):
#         text="Web Geliştirme Kurları Listesi"
#     elif(category_name=="mobil-programlama"):
#         text="Mobil Programlama Kurs Lİstesi"
#     else:
#         text="Yanlış Kurs Seçimi"
#     return HttpResponse(text)

#yukardaki kodu data bilgisiyle profesyonelleştirdik
# #kullanıcı yanlış url girerse hata sayfası çıktı verdik
# def getCoursesByCategoryName(req,category_name):
#     try:
#         text=data[category_name]
#         return HttpResponse(text)#başarılı is status=200 olur
#     except:
#         return HttpResponseNotFound("Yanlış Kategori Seçimi")#sayfa bulunamadıysa status=404



#yeni versiyon 
def getCoursesByCategoryName(req,category_slug_name):
    try:
        # selected_category=Categories.objects.get(slug=category_slug_name)
        # kurslar=Course.objects.filter(category=selected_category)
        categories=Categories.objects.all()
        #cat=Categories.objects.get(slug=category_slug_name)
        #courses=cat.course_set.all()
        #yukardaki 2 kod yerine aşağıdaki tek kodu yazabiliriz
        courses=Course.objects.filter(isActive=1,categories__slug=category_slug_name).order_by("-date")
        #istersek "categories__name" gibi ilşkil tablonun kolonuna göre sıralayabiliriz.baştaki - işreti desc içindir.
        
        
        #Sayfa başına gösterilecek kurs sayısını ayarlayalım
        p=Paginator(courses,2)
        page=req.GET.get("page",1)#progrmlama?page=3 yazıldığında bize 3 değeri gelecek yoksa varsayılan 1 gelecek biz e page değikenine set ederiz
        page_obj=p.page(page)#o anki sayfanın objesini dönderir
        
        
        return render(req,'index.html',{"page_obj":page_obj,"categories":categories,"selected_slug":category_slug_name})
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")#sayfa bulunamadıysa status=404
    

# def getCoursesByCategoryId(req,category_id):
#     category_keys=list(data.keys())
#     if(category_id>len(category_keys)):
#         return HttpResponseNotFound("Yanlış Kategori Seçimi")
#     category_name=category_keys[category_id-1]
    
#     #urlleri elle yazmak hatya neden olabilir ayrıca url değişirse tüm o urlyi kullanları güncellememiz gerekir o nedenle named url kullanıyoruz
#     redirect_url=reverse('courses_by_category',args=[category_name])
#     return redirect(redirect_url)
#artık int olarak gelen id lere karşılık gelen category name öğrenilip url sine yönlendirildi
#aynısını kısa kod ile de yapabilirdik
#return getCoursesByCategoryName(req,category_name)


def index(req):
    #courses=db["courses"]
    #Artık verimizi static verimizden değil gerçek db den çekecez
    
    courses=Course.objects.filter(isActive=1).order_by("-date")
    p=Paginator(courses,4)
    page=req.GET.get("page",1)
    page_obj=p.page(page)
    
    #courses=[course for course in db["courses"] if course["isActive"]s==True]
    #Sayfaya direk filtrelenmiş veriyi gönderbiliriz.Böylece template kısmında filtre yapmaya gerek kalmaz
    
    categories=Categories.objects.all()
    return render(req,"index.html",{"page_obj":page_obj,"categories":categories})
#eğer index.html aynı app içinde bulunmazsa diğer appler içinde aranır
#settings.py içindeki appçdirs=true bunu enable eder
#for işini template içinde yapacağız,biz sadece render ile veriyi oraya göndereceğiz