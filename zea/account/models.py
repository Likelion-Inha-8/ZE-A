from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileStu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique= True)
    fullname = models.TextField(max_length=15)
    school = models.TextField(max_length=30)
    department = models.TextField(max_length= 50)
    grade = models.IntegerField(default=1)
    bank2 = models.TextField(max_length = 30) #은행
    bank = models.TextField(max_length = 30) #계좌번호 
    subject = models.TextField(max_length = 30)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now= True)
    STORE2 = "소상업체"
    STUDENT2 = "대학생"
    
    CATEGORY_CHOICES = (
        (STORE2, "소상업체"),
        (STUDENT2, "대학생"),
        
    ) # 파이썬에서 상수를 사용하고 싶을 때 관용적으로 대문자로 작성 
    your_category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=STORE2,
    )
 

class ProfileMer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique= True)
    fullname = models.TextField(max_length=15) 
    num1 = models.IntegerField() #사업자 등록번호1
    num2 = models.IntegerField() #사업자 등록번호2
    num3 = models.IntegerField() #사업자 등록번호3
    #title = models.CharField(max_length = 100)
    #photo = models.ImageField(null=True, blank=True, upload_to="merchandiser")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now= True)
    STORE2 = "소상업체"
    STUDENT2 = "대학생"
    
    CATEGORY_CHOICES = (
        (STORE2, "소상업체"),
        (STUDENT2, "대학생"),
        
    ) # 파이썬에서 상수를 사용하고 싶을 때 관용적으로 대문자로 작성 
    your_category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=STORE2,
    )
 
 

   