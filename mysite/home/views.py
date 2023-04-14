from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home_view(request):
    template = loader.get_template('home.html')
    context = {
        "abc": "abc"
    }
    
    return HttpResponse(template.render(context, request))
