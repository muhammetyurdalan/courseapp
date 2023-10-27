from django.urls import path,include
from . import views

#int olan dinamik url i başa yazmalıyız yoksa int urller de str sanılıp str dinamik url yi çalıştırır
#courseName tüm strleri karşılamasın diye category_name lerin başına yeni url verdik
#

urlpatterns = [
    path("",views.index),
    path("list",views.course),
    path("mobil-uygulamalar",views.mobiluygulamalar),
    path("<courseName>",views.details),
    path("category/<int:category_id>",views.getCoursesByCategoryId),
    path("category/<str:category_name>",views.getCoursesByCategoryName,name="courses_by_category")
]
