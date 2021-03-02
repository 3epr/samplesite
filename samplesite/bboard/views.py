from django.shortcuts import render

from .models import Bb, Rublic

def index(request):
 bbs = Bb.objects.all()
 rublics = Rublic.objects.all()
 context = {'bbs': bbs, 'rublics': rublics}
 return render(request, 'bboard/index.html', context)
 return render(request, 'bboard/index.html', {'bbs': bbs})

def by_rublic(request, rublic_id):
 bbs = Bb.objects.filter(rublic=rublic_id)
 rublics = Rublic.objects.all()
 current_rublic = Rublic.objects.get(pk=rublic_id)
 context = {'bbs': bbs, 'rublics': rublics, 'current_rublic': current_rublic}
 return render(request, 'bboard/by_rublic.html', context)