from django.shortcuts import render

# home page for learning log
def index(request):
    return render(request, 'learning_logs/index.html')
