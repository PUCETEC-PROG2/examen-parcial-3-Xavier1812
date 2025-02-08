from django.shortcuts import render
from django.template import loader
from .models import Album, Artist
from django.http import HttpResponse

def index(request):
    albums = Album.objects.all()
    artists = Artist.objects.all()
    template = loader.get_template('index.html')

    context = {
        'albums': albums,
        'artists': artists,
    }
    
    return HttpResponse(template.render(context, request))

