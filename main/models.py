from django.db import models

# 장고에서 model을 지원해준다.
# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # 객체를 표현 Post Object(1) 대신 
    # 다른 형식으로 표현하기 위한 함수
    def __str__(self):
        return self.postname
