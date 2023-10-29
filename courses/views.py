from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
         "imageUrl":"https://northsoft.co/blog/wp-content/uploads/2022/11/image-1024x538.jpeg",
         "date":date(2023,10,10),
         "isActive":True
            
            },
        {"title":"Python Kursu",
         "description":"Python Kurs Açıklaması",
         "slug":"python-course",
         "imageUrl":"https://miro.medium.com/v2/resize:fit:1400/1*m0H6-tUbW6grMlezlb52yw.png",
         "date":date(2023,10,10),
         "isActive":False
            },
        {"title":"Java kursu",
         "description":"Java Kurs Açıklaması",
         "slug":"java-course",
         "imageUrl":"https://www.bilgiyazan.com.tr/wp-content/uploads/2015/07/Java-E%C4%9Fitimi.jpg",
         "date":date(2023,10,10),
         "isActive":True
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








# def details(req,courseName):
#     return HttpResponse(f"{courseName} Kursu Detayları sayfası")

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
    courses=db["courses"]
    categories=db["categories"]
    return render(req,"index.html",{"courses":courses,"categories":categories})
#eğer index.html aynı app içinde bulunmazsa diğer appler içinde aranır
#settings.py içindeki appçdirs=true bunu enable eder
#for işini template içinde yapacağız,biz sadece render ile veriyi oraya göndereceğiz