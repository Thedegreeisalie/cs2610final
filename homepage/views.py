from django.shortcuts import render

# Create your views here.
from homepage.models import Post
from collection.forms import ContactForm

def index(request):
    data = {'myData': "Hello world more to come"}
    return render(request, 'homepage/index.html', data )
    
def contact(request):
    form_class=ContactForm
    return render(request, 'homepage/contact.html', {'form':form_class,})

def portfolio(request):
    posts = Post.objects.order_by("updated_date")
    return render(request, 'homepage/portfolio.html', {'post': posts} )