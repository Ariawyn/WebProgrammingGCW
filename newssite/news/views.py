from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Article, Comment

def index(request):
	latest_article_list = Article.objects.all()
	return render(request,'news/index.html', {'latest_article_list': latest_article_list})
	
def detail(request, article_id):
        if(request.method == "POST"):
                # Posting a comment on the article
                comment = Comment(
                        article=get_object_or_404(Article, pk=article_id),
                        user=request.user,
                        body=request.POST['body'],
                        published=timezone.now(),
                )
                comment.save()
                return redirect("/news/" + article_id)

        article = get_object_or_404(Article, pk=article_id)
        comments = Comment.objects.filter(article=article)
        return render(request, 'news/detail.html', {'article': article, 'comments': comments})

@login_required
def post(request):
        # Check if GET or POST request
        if(request.method == "POST"):
                if(request.user.is_contributor):
                        article = Article(
                                title=request.POST['title'],
                                body=request.POST['body'],
                                category=request.POST.get('category', "TE"),
                                author=request.user,
                                published=timezone.now(),
                        )
                        article.save()
                        return redirect("/news/")
                else:
                        return redirect("/news/")
        else:
                if(request.user.is_contributor):
                        return render(request, 'news/post.html', {'categories': Article.CATEGORIES})
                else:
                        return redirect("/news/")

def vote(request):
	vote_type = request.POST.get('type')
	page_id = get_object_or_404(Article, pk=article_id)
	
	if (vote_action == 'Like'):
		page_id.score += 1
	elif (vote_action == 'Dislike'):
		page_id.score -= 1
	else:
		return HttpResponse('There has been an Error, please try again.')
