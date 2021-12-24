from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>This is working, see?</h1>')
