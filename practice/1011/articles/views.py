from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)


def detail(request, pk):
  article = Article.objects.get(pk = pk)
  comment_form = CommentForm()

  # comment_set -> 역참조
  # 게시글에 달린 모든 댓글을 가져오기 위해서 (역참조)
  comments = article.comment_set.all()

  context = {
    'article' : article,
    'comment_form' : comment_form,
    'comments' : comments,
  }
  return render(request, 'articles/detail.html', context)


@login_required
def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      # 바로 DB에 자동으로 저장 -> request.user정보(수동으로 저장) -> commit=False
      article = form.save(commit=False)
      # request.user -> 로그인한 사용자
      article.user = request.user
      article.save() # 최종적으로 DB에 저장
      return redirect('articles:detail', article.pk)
    
  else:
    form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
  article = Article.objects.get(pk = pk)
  # request.user : 로그인한 사용자
  # article.user : 게시글 작성자
  if request.user == article.user:
    article.delete()
  return redirect('articles:index')


@login_required
def update(request, pk):
  article = Article.objects.get(pk = pk)
  # 로그인한 유저와 게시글 작성자가 같을 때 update를 할 수 있다
  if request.user == article.user:
    if request.method == 'POST':
      form = ArticleForm(request.POST, request.FILES, instance = article)
      if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    else:
      form = ArticleForm(instance = article)

  else:
    return redirect('articles:index')
  
  context = {
    'article' : article,
    'form' : form,
  }
  return render(request, 'articles/update.html', context)


@login_required
def comments_create(request, pk):
  # 게시글 조회
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  # 댓글 유효성 검사
  if comment_form.is_valid():
    # 댓글을 바로 DB에 저장하지 않고 2개 따로 저장
    comment = comment_form.save(commit=False)
    # 첫 번째 : 게시글의 외래키
    comment.article = article
    # 두번째 : 로그인 사용자
    comment.user = request.user
    # DB에 수동으로 저장
    comment.save()
    return redirect('articles:detail', article.pk)
  
  # 유효성 검사 실패
  context = {
    'article' : article,
    'comment_form' : comment_form,
  }
  return render(request, 'articles:detail.html', context)


@login_required
def comments_delete(request, article_pk, comment_pk):
  article = Article.objects.get(pk=article_pk)
  comment = Comment.objects.get(pk=comment_pk)
  if request.user == comment.user:
    comment.delete()
  return redirect('articles:detail', article.pk)