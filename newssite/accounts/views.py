from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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

