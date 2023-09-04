from django.urls import path, re_path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # home page
    re_path(r'^$', views.index, name='index')
]
