from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작ㅈ성된 모든 댓글 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def comments_create(request, pk):
    # GET으로 요청보내는 경우가 없어서 else 안써도 됨
    # 어떤 게사글에 작성되는지 게시글을 조회
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # form에서는 사용자의 입력만 받아서 오므로 외래키를 따로 입력해야하는 순간이 필요하다.
        # 외래 키 데이터를 넣는 타이밍이 필요
        # 외래 키를 넣을면 2가지 조건이 필요
        # 1. comment 인스턴스 필요
        # 2. save메서드가 호출되기 전이어야함
        # 그런데 comment인스턴스는 save 메서드가 호출되야 생성됨
        # 그래서 django의 save 메서드는 인스턴스만 제공하고, 실제 저장은 잠시 대기하는 옵션을 제공
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글을 삭제할지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # detail에 article pk를 넘기는 첫번째 방법
    # article_pk = comment.article.pk
    # detail에 article_pk를 넘기는 두번째 방법
    article = Article.objects.get(pk=article_pk)
    comment.delete()
    return redirect('articles:detail', article.pk)