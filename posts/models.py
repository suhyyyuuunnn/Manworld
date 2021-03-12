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

    def __unicode__(self):
        return self.title
