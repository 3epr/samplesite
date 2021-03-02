from django.shortcuts import render

from .models import Bb, Rublic

def index(request):
 bbs = Bb.objects.all()
 rublics = Rublic.objects.all()
 context = {'bbs': bbs, 'rublics': rublics}
 return render(request, 'bboard/index.html', context)