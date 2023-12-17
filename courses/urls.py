from django.urls import path,include
from . import views

#int olan dinamik url i başa yazmalıyız yoksa int urller de str sanılıp str dinamik url yi çalıştırır
#courseName tüm strleri karşılamasın diye category_name lerin başına yeni url verdik
#

urlpatterns = [
    path("",views.index,name="index_url"),
    path("create_course",views.create_course,name="create_course_url"),
    path("search",views.search,name="search_url"),
    path("course_list",views.course_list,name="course_list_url"),
    path("upload",views.upload,name="upload_url"),
    path("edit_course/<int:id>",views.edit_course,name="edit_course_url"),
    path("delete_course/<int:id>",views.delete_course,name="delete_course_url"),
    path("<slug:course_slug>",views.details,name="course_details_url"),
    #path("category/<int:category_id>",views.getCoursesByCategoryId),
    path("category/<str:category_slug_name>",views.getCoursesByCategoryName,name="courses_by_category")
]
