from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from .models import Article
def index(request):
	return render(request,'news/index.html')
	
def detail(request, Article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'news/article.html', {'article': article})