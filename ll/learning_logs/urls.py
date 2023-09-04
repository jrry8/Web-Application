# Defines URL patterns for learning_logs

from django.urls import path, re_path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    re_path(r'^$', views.index, name='index'),
    # show all topics
    re_path(r'^topics/$', views.topics, name='topics'),
    # detail page for a single topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # page for adding a new topic
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    # page for adding a new entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')
]