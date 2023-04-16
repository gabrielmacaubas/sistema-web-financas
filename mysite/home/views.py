from django.http import HttpResponse
from django.template import loader


def home_view(request):
    template = loader.get_template('home.html')
    context = {}
    
    return HttpResponse(template.render(context, request))
