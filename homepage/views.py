from django.shortcuts import render

# Create your views here.
from homepage.models import Post


def index(request):
    data = {'myData': "Hello world more to come"}
    return render(request, 'homepage/index.html', data )
    
def contact(request):
    data = {'myData': "Hello world more is on the way"}
    return render(request, 'homepage/contact.html', data )

def portfolio(request):
    posts = Post.objects.order_by("updated_date")
    return render(request, 'homepage/portfolio.html', {'post': posts} )