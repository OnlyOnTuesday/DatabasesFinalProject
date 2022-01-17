from django.http import HttpResponse
from django.shortcuts import render
from GitStalker.models import Repo, User, WorksOn, Commits

def index_view(request):
    return HttpResponse('<h1>This is working, see?</h1>')

def home_page(request):
    repo_list = Repo.objects.all()
    user_list = User.objects.all()

    my_context = {'wm_list': repo_list, 'user_list': user_list}
    
    return render(request, 'index.html', context=my_context)


def getWmView(request, wm_name):
    # Get the list of users who work on this project
    # This is a join, the syntax hides that
    user_list = User.objects.filter(workson__reponame=wm_name)
    
    my_context = {'user_list': user_list}

    return render(request, 'wm_template.html', context=my_context)

def getUserView(request, usr_name):
    user = User.objects.get(authorname=usr_name)
    commits = Commits.objects.filter(authoremail=user.authoremail)
    works_on = WorksOn.objects.filter(authoremail=user.authoremail)
    my_context = {'user': user, 'commits': commits, 'projects': works_on}
    return render(request, 'user_template.html', context=my_context)
