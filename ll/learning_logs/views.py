from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# home page for learning log
def index(request):
    return render(request, 'learning_logs/index.html')

# display all topics
@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# show a single topic and all its entries
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

# add a new topic
def new_topic(request):
    # when the user intially requests this page, the browser will sent a GET request
    if request.method != 'POST':
        # no data submitted; create a blank form.
        form = TopicForm()
    # when the user submits the form, the browser will send a POST request
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            # save() writes the data from the form to the database
            form.save()
            # redirect the user's browser to the topics page
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# add a new entry for a particular topic
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # create new entry object but without saving to the database yet
            new_entry = form.save(commit=False)
            # save to database after updating the entry's topic attribute
            new_entry.topic = topic
            new_entry.save()
            # redirect to the relevant topic page
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# edit an existing entry
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)