from django.shortcuts import render

# Create your views here.
def index(request):
  # context는 딕셔너리 구조
  # template에서 {{name}}} 즉, dtl context의 key의 value 값을 사용할 수 있다.
  context = {
    "name" : "Jane",
    "number" : 1
  }
  # 항상 render 함수의 3번째 항목에는 매개변수(context)
  return render(request, "articles/index.html", context)

import random
def dinner(request):
  foods = ['족발', '보쌈', '치킨', '피자']
  picked = random.choice(foods)
  context = {
    'foods' : foods,
    'picked' : picked,
  }
  return render(request, "articles/dinner.html", context)

def search(request):
  return render(request, "articles/search.html")

def throw(request):
  return render(request, "articles/throw.html")

def catch(request):
  # name의 값으로 .get()안에 적어야함
  text = request.GET.get('message')
  # message = request.GET['message']
  # print(text)
  context = {
    'talk' : text
  }
  return render(request, "articles/catch.html", context)

def detail(request, number):

  context = {
    'num' : number
  }

  return render(request, "articles/detail.html", context)