from django.contrib import admin
from .models import Course,Categories

# Register your models here.


#Admin panelini özelleştirme 1.yöntem
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #ekranda gösterilecek kolonları seçiyoruz
    #category_list bizim yazdığımız fonksiyon ismi
    list_display=("title","isActive","slug","isUptaded","category_list")
    #tıklanınca edit sayfasına yönlendir
    list_display_links=("title","slug")
    #sadece okunabilir yapma
    readonly_fields=("slug",)  #prepopulated_fields={"slug":("title",)} slugify yerine bu kos yazılabilir
    #yan tarafta çıkacak filtreleme listesi
    list_filter=("isActive","isUptaded",)
    #edit sayfasına gitmeden düzenleyebilmek için
    list_editable=("isActive","isUptaded")
    #arama textfielde içinde neleri arayabileceğimiz
    search_fields=("title","description")
    
    
    
    def category_list(self,obj):
        #obj bize gelen tablodaki her course nesnesini temsil eder
        text=""
        for cat in obj.categories.all():
            text+=cat.name+","   
        text=text[0:-1]#sondaki virgülü siler

        return text
    
    
#Admin panelini özelleştirme 2.yöntem
class CateoriesAdmin(admin.ModelAdmin):
    #ekranda her kategorinin kaç kursa sahip oldğunu yazdırmak için course_count ismli bir fonk yazacaz
    list_display=("name","slug","course_count")
    
    def course_count(self,obj):
        #obj bize gelen tablodaki her kategori nesnesini temsil eder
        
        return obj.course_set.count()




admin.site.register(Categories,CateoriesAdmin)
