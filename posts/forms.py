from django import forms
from .models import Post, Counsel
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


class CounselForm(forms.ModelForm):
    class Meta:
        model = Counsel
        fields = ['name', 'phone', 'title', 'content', 'password']
        labels = {
            'title': '제목',
            'content': '내용',
            'phone': '연락처',
            'name': '이름',
            'password': '비밀번호',

        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'

            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }