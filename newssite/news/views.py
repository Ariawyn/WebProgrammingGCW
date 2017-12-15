from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from .models import Article

def index(request):
	latest_article_list = Article.objects.all()
	return render(request,'news/index.html', {'latest_article_list': latest_article_list})
	
def detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'news/detail.html', {'article': article})