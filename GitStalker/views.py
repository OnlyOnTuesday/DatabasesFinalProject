from django.http import HttpResponse
from django.shortcuts import render
from GitStalker.models import Repo, User

def index_view(request):
    return HttpResponse('<h1>This is working, see?</h1>')

def home_page(request):
    repo_list = Repo.objects.all()
    user_list = User.objects.all()

    my_context = {'wm_list': repo_list, 'user_list': user_list}
    
    return render(request, 'index.html', context=my_context)


def getWmView(request, wm_name):
    return HttpResponse('<h1> Ta Da </h1>')

def getUserView(request, usr_email):
    return HttpResponse('<h1>Ta Da X 2</h1>')
