from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # logout page
    re_path(r'^logout/$', views.logout_view, name='logout'),
]