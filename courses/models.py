from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here..

class Categories(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(default="",blank=True,editable=False,null=False,unique=True,db_index=True)
    
    
    def __str__(self):
        return f"{self.name}"
    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(args,kwargs)



class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50)
    #auto_now_add=True denirse nesne oluşturulduğu anın bilgisi oto işlenir
    #auto_now=True denirse migrate ile db ye eklendiği anın tarihi işlenir
    date=models.DateField(auto_now=True)
    #default olarak yeni eklnen kurslarda isactive true yapıldığı için set etmeye gerek kalmaz
    isActive=models.BooleanField(default=1)
    slug=models.SlugField(default="",blank=True,editable=False,null=False,unique=True,db_index=True)
    #blank form esnasında boş geçilebilmesi için true
    #editable=false ise hiç sorulmamasını sağlar
    isUptaded=models.BooleanField(default=True)
    #1 e çok ilşki için category field ekelyecez
    #category silindiğinde ona bağlı tüm kurslar silinsin için Cascade seçiyoruz
    #category silindiğinde ona bağlı tüm kurslar silinmesin sadece category alanına null set edllsin için SET_NULL seçiyoruz
    #tabi aytıca null=true atamasıyla izin verilmelidir
    #SET_DEFAULT atayıp default=1 dersek silindiğinde kolona 1 değeri set edilir
    
    #related_name ile sorgularda kullanacağımı hayali kolona isim verebiliriz.Açıklama aşağıda
    #category=models.ForeignKey(Categories,default=1,on_delete=models.CASCADE,related_name="selectedCourses")
    
    #M-N ilişki için aşağıdaki kolon oluşturulur ve django otomatik olarak 3.ilşki tablosunu oluşturur
    #foreignkey kolonu silinmelidir
    categories=models.ManyToManyField(Categories)
    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)
    
    
    def __str__(self):
        return f"{self.title}"
    

    #İlşikili Kayıda ulaşma
    
    #1-kurs modelinde filtre yaparak kategoriye göre kursa erişme => "__" operatörü
    
    #kurs1=Course.objects.get(category__name="programlama")   yani category kolonundaki nesnenin name alanına ulaşıyoruz
    #kurs1=Course.objects.get(category__name__contains="program")
    #kurslar=Course.objects.filter(category__slug="web-gelistirme") çoklu dönüş
    
    #2-kategori nesnesi ile kategoriyi kullanan kurslara erişme => "İlişkiliTabloİsmi_set" operatörü veya related name eset eilen isim kullanılır
    
    #category1=Categories.objects.get(name="programlama")
    #kurslar=category1.course_set.all() veya
    #kurslar=category1.course_set.filter()  yani aslında kategoriler tablosunda hayali olarak "ilişkilitabloismi_set"
    #şeklinde bir kolon oluşturulur ve içinde bu kategoriyi kullanan kurslar saklanır 
    #veya foreign kolonuna related_name="abc" ataması yaparsak artık "course_set" yerine "abc"yi kullanabiliriz
    
    
    #M-N ilişkili taloya veri ekleme
    
    #prog=Categories.objects.get(pk=1)
    #k1=Course.objects.get(pk=1)
    #k1.categories.add(prog)  veya  prog.course_set.add(k1)  her iki tablodan da veri ekleyebilir sorgulayabiliriz
    
    #prog da kaç tane course var
    #prog.course_set.all()  
    #eğer categories ismli kolona related_name ataması yapmış olsaydık course_set yerine o ismi kullanabilirdik
    
    #prog da kaç kurs var sorgusunu Course ile yapmak
    #Course.objects.filter(isActive=1,categories__name="programlama")
    
    #silme 
    #k1.categories.remove(Categories.objects.get(pk=1))    
    #k1.categories.clear() tüm kategorileri siler   
    