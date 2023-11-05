from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Categories, Course

# Create your views here.

data={
    "programlama":"Pogramlama kursu Listesi",
    "web-gelistirme":"Web Gelistirme kursu Listesi",
    "mobil-programlama":"Mobil Pogramlama kursu Listesi"
}

db={
    "courses":[
        {"title":"Javascript Kursu",
         "description":"Javascript Kurs Açıklaması",
         "slug":"javascript-course",
         "imageUrl":"js.jpeg",
         "date":date(2023,10,10),
         "isActive":True,
         "isUptaded":False
            
            },
        {"title":"Python Kursu",
         "description":"Python Kurs Açıklaması",
         "slug":"python-course",
         "imageUrl":"python.png",
         "date":date(2023,10,10),
         "isActive":False,
         "isUptaded":False
            },
        {"title":"Java kursu",
         "description":"Java Kurs Açıklaması",
         "slug":"java-course",
         "imageUrl":"java.jpg",
         "date":date(2023,10,10),
         "isActive":True,
         "isUptaded":True
            }
    ],
    "categories":[{"id":1,"name":"Programlama","slug":"programlama"},
                  {"id":2,"name":"Web Geliştirme","slug":"web-gelistirme"},
                  {"id":3,"name":"Mobil Programlama","slug":"mobil-programlama"}]
}

# #dinamik olarak html etiketleri oluşturduk
# def course(req):
#     list_item=""
#     course_list=list(data.keys())
#     for item in course_list:
#         redirect_url=reverse('courses_by_category',args=[item])
#         list_item+=f"<li><a href='{redirect_url}'>{item}</a></li>"
    
#     html=f"<ul>{list_item}</ul>"
#     return HttpResponse(html)




# def fillTheSlug():
#     course=Course.objects.all()
#     for c in course:
#         c.save()



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
def getCoursesByCategoryName(req,category_name):
    try:
        text=data[category_name]
        return render(req,'index.html',{"category_name":category_name,"category_text":text})
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")#sayfa bulunamadıysa status=404
    

def getCoursesByCategoryId(req,category_id):
    category_keys=list(data.keys())
    if(category_id>len(category_keys)):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name=category_keys[category_id-1]
    
    #urlleri elle yazmak hatya neden olabilir ayrıca url değişirse tüm o urlyi kullanları güncellememiz gerekir o nedenle named url kullanıyoruz
    redirect_url=reverse('courses_by_category',args=[category_name])
    return redirect(redirect_url)
#artık int olarak gelen id lere karşılık gelen category name öğrenilip url sine yönlendirildi
#aynısını kısa kod ile de yapabilirdik
#return getCoursesByCategoryName(req,category_name)


def index(req):
    #courses=db["courses"]
    #Artık verimizi static verimizden değil gerçek db den çekecez
    
    courses=Course.objects.filter(isActive=1)
    
    #courses=[course for course in db["courses"] if course["isActive"]s==True]
    #Sayfaya direk filtrelenmiş veriyi gönderbiliriz.Böylece template kısmında filtre yapmaya gerek kalmaz
    
    categories=Categories.objects.all()
    return render(req,"index.html",{"courses":courses,"categories":categories})
#eğer index.html aynı app içinde bulunmazsa diğer appler içinde aranır
#settings.py içindeki appçdirs=true bunu enable eder
#for işini template içinde yapacağız,biz sadece render ile veriyi oraya göndereceğiz