from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from news.models import Article, Comment
from .forms import RegisterForm

# Create your views here.
def register(request):
    # Check if GET or POST request
    if(request.method == "POST"):

        # We want to get the instance of the form from the request
        form = RegisterForm(request.POST)

        # Validate
        if(form.is_valid()):

            # Save
            form.save()

            # Get data from form
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            # Get user
            user = authenticate(email=email, password=password)
            login(request, user)

            # Redirect
            return redirect("/news/")
    else:
        # Since this is a GET request
        # We create an empty form
        form = RegisterForm()

    # We will only ever get to this return statement from a get request
    # Thus, we render the register.html file here, passing the form to it
    return render(request, "accounts/register.html", {"form": form})


# User page view, has form to change user details, shows comments / articles made by user
@login_required
def user(request):
    # Check if GET or POST request
    if(request.method == "POST"):
        # Get and change user values from form
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.phone_number = request.POST['phone_number']
        
        # Save edited data
        request.user.save()

        # Reload
        return redirect("/accounts/user/")

    else:
        
        # get user id
        user_id = request.user.id

        # Check for user articles
        user_articles = None
        if(request.user.is_contributor):
            user_articles = Article.objects.filter(author = user_id)

        # Check for user comments
        user_comments = Comment.objects.filter(user = user_id)

    return render(request, "accounts/user.html", {"user_articles": user_articles, "user_comments": user_comments})

    

