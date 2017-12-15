from django.conf.urls import url
from django.contrib import admin

# Import the default django authentication views for login / logout
from django.contrib.auth import views as authentication_views
from . import views

urlpatterns = [
    # example: /accounts/login/             goes to a login page, that when the form is submitted redirects to the profile page
    url(r'^login/$', authentication_views.login, {'template_name': 'accounts/login.html'}, name='login'),

    # example: /accounts/logout/            logs out the user and redirects to another page
    url(r'^logout/$', authentication_views.logout, {'next_page': '/news'}, name='logout'),

    # example: /accounts/register/
    url(r'^register/$', views.register, name="registration"),

    # example: /accounts/user/
    url(r'^user/$', views.user, name="user"),
]
