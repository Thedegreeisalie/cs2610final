from django.shortcuts import render

# Create your views here.

def index(request):
    data = {'myData': "Hello world more to come"}
    return render(request, 'homepage/index.html', data )
    
def contact(request):
    data = {'myData': "Hello world more is on the way"}
    return render(request, 'homepage/contact.html', data )

def portfolio(request):
    data = {'myData': "Hello world more in the works"}
    return render(request, 'homepage/portfolio.html', data )