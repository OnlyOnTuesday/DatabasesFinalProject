from django.http import HttpResponse
from django.shortcuts import render
from GitStalker.models import Repo, User, WorksOn, Commits

def home_page(request):
    repo_list = Repo.objects.all()

    if request.GET.get('search'):
        user_list_1 = User.objects.filter(authorname__icontains=request.GET.get('search'))
        user_list_2 = User.objects.filter(authoremail__icontains=request.GET.get('search'))
        user_list = user_list_1 | user_list_2
    else:
        user_list = User.objects.all()

    my_context = {'wm_list': repo_list, 'user_list': user_list}
    
    return render(request, 'index.html', context=my_context)


def getWmView(request, wm_name):
    # Get the list of users who work on this project
    # This is a join (between user and workson), the syntax hides that
    if request.GET.get('search'):
        user_list_1 = User.objects.filter(authorname__icontains=request.GET.get('search'), workson__reponame=wm_name)
        user_list_2 = User.objects.filter(authoremail__icontains=request.GET.get('search'), workson__reponame=wm_name)
        user_list = user_list_1 | user_list_2
    else:
        user_list = User.objects.filter(workson__reponame=wm_name)
    
    wm = wm_name

    my_context = {'user_list': user_list, 'wm_name': wm}

    return render(request, 'wm_template.html', context=my_context)

def getUserView(request, usr_name):
    user = User.objects.filter(authorname=usr_name)
    user = user[0]
    commits = Commits.objects.filter(authoremail=user.authoremail)
    works_on = WorksOn.objects.filter(authoremail=user.authoremail)
    my_context = {'user': user, 'commits': commits, 'projects': works_on}
    return render(request, 'user_template.html', context=my_context)

