from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class DatePlace(models.Model):

    THEMA_CHOICES = [
        ('ROMANTIC', '로맨틱'),
        ('ACTIVE', '액티브'),
        ('CULTURAL', '문화'),
        ('NATURE', '자연')
    ]

    title = models.CharField(max_length=20) # 데이트장소 타이틀
    thema = models.CharField(max_length=20, choices=THEMA_CHOICES) # 테마 선택
    date_name = models.CharField(max_length=100) # 데이트

class Place(models.Model):
    name = models.CharField(max_length=100), # 장소 이름
    latitude = models.DecimalField(max_digits=9, decimal_places=6) # 위도
    longitude = models.DecimalField(max_digits=9, decimal_places=6) # 경도
    address = models.CharField(max_length=255, null=True, black=True) # 주소
    description = models.TextField(max_length=100, null=True, black=True) # 장소 설명
    opening_hours = models.CharField(max_length=100, null=True, black=True) # 영업 시간
    website = models.URLField(null=True, blank=True) # 웹사이트
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # 생성 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정 시간
    
    def __str__(self):
        return self.name