from django.shortcuts import render

# Create your views here.

def index(request):
    data = {'myData': "Hello world more to come"}
    return render(request, 'homepage/index.html', data )