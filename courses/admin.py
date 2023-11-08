from django.contrib import admin
from .models import Course,Categories

# Register your models here.


#Admin panelini özelleştirme 1.yöntem
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    #ekranda gösterilecek kolonları seçiyoruz
    list_display=("title","isActive","slug","isUptaded")
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


#Admin panelini özelleştirme 2.yöntem
class CateoriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categories,CateoriesAdmin)
