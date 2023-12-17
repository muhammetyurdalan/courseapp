from django import forms

from courses.models import Course

class CourseCreateForm(forms.Form):
    title=forms.CharField(
        error_messages={"required":"Bu alan zorunludur"},
        label="Kurs Başlığı",
        required=True,
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    description=forms.CharField(
        error_messages={"required":"Bu alan zorunludur"},
        label="Açıklama",
        required=True,
        widget=forms.Textarea(attrs={"class":"form-control"})
        )
    imageUrl=forms.CharField(
        error_messages={"required":"Bu alan zorunludur"},
        label="Resim Url",
        required=True,
        widget=forms.TextInput(attrs={"class":"form-control"})
        )
    isActive=forms.BooleanField(
        label="Aktif-Pasif",
        required=False
        )
    
    
    #Form Oluşturmada 2. Yöntem
    #Var olan modeli kullanarak otomatik bir form oluşturabiliriz.yeni özellikler ekleyebilir.
    #Modeldeki fieldların sadece bazılarını form haline çevirebiliriz
class CourseEditForm(forms.ModelForm):
    class Meta:
        model=Course
            #fields='__all_'  tüm modeli ekler
        fields=('title','description','imageUrl','isActive','categories')
        labels={
                'title':'Kurs Başlığı',
                'description':"Açıklama",
                'imageUrl':"Resim",
                'isActive':"Aktif",
            }
        widgets={
                "title":forms.TextInput(attrs={"class":"form-control"}),
                "description":forms.Textarea(attrs={"class":"form-control"}),
                "imageUrl":forms.TextInput(attrs={"class":"form-control"}),
                "categories":forms.SelectMultiple(attrs={"class":"form-control"})
            }
        error_massage={
                "title":{
                    "required":"Bu alan zorunludur",
                    "max_length":"Maximum 50 karakter girmelisiniz",
                }
            }