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
	
def vote(request):
	vote_type = request.POST.get('type')
	page_id = get_object_or_404(Article, pk=article_id)
	
	if (vote_action == 'Like'):
		page_id.score += 1
	elif (vote_action == 'Dislike'):
		page_id.score -= 1
	else:
		return HttpResponse('There has been an Error, please try again.')