from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Meta:
        verbose_name = "공지사항"
        ordering = ['-created_at']

    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    user = models.CharField(max_length=100, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트시간")
    image = models.ImageField(upload_to="posts/img", blank=True, default="posts/default/1.jpg", verbose_name="썸네일 이미지")

    def __unicode__(self):
        return self.title


class Counsel(models.Model):
    class Meta:
        verbose_name = "상담"
        ordering = ['-created_at']

    name = models.CharField(max_length=200, verbose_name="이름")
    phone = models.CharField(max_length=200, verbose_name="연락처")
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    password = models.CharField(max_length=200, verbose_name="비밀번호")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __unicode__(self):
        return self.title


