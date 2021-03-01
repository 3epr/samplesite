from django.shortcuts import render

from .models import Bb

def index(request):
 bbs = Bb.object.all()
 return render(request, 'bboard/index.html', {'bbs': bbs})