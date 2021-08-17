from django.shortcuts import render

def index(request):
    return render(request, 'sndApp/index.html')
    #return render(request, 'index.html')
