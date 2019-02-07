from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects #모델로부터 Blog의 객체목록을 전달 받을 수 있게함. ==> 쿼리셋(querySet)
    #쿼리셋을 이용하게 해주는 것 => 메소드
    return render(request, 'home.html', {'blogs': blogs})

    #쿼리셋과 메소드의 형식
    #모델이름.쿼리셋(object).메소드

def introduce(request):
    return render(request, 'introduce.html')
