from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)


def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' : article,
  }
  return render(request, 'articles/detail.html', context)


def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()

  return redirect('articles:index')


def create(request):
  # 내가 게시글 생성 버튼을 눌렀을 때
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    # 유효성 검사 대표적 2가지
    # 1. 모든 필수 필드가 채워져 있는지
    # 2. 입력된 데이터가 필드의 조건(ex. 데이터 형식)을 만족하는지.
    # 3. 등등....
    if form.is_valid():
      article = form.save()
      # create 함수 부분
      return redirect('articles:detail', article.pk)

  # 게시글 생성 버튼을 누르기 전 또는 다른 버튼 눌렀을 때(다른 방식(method)일 때)
  else:
    form = ArticleForm()
  # 1. 유효성 검사 통과하지 못한 경우(에러와 함께 폼 다시 표시)
  # 2. GET 요청인 경우(빈 폼 표시)
  context = {
    'form' : form,
  }
  return render(request, 'articles/create.html', context)


# 단일 게시글 조회하고 변경
def update(request, pk):
  # 조회 먼저
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
    # 기존 게시글의 데이터를 미리 채운다.
    form = ArticleForm(request.POST, request.FILES, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  
  # 변경 버튼 누르기전 또는 다른 버튼 눌렀을 때
  else:
    form = ArticleForm(instance=article)
  context = {
    # 기존에 존재했던 데이터
    'article' : article, 
    # 새로 받은 데이터
    'form' : form,
  }
  return render(request, 'articles/update.html', context)