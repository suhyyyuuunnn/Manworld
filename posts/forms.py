from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user', 'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'user': '작성자',
            'image': '썸네일 이미지',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': SummernoteWidget(),
        }