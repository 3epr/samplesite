from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb, Rublic
from .forms import BbForm

class BbCreateView(CreateView):
 template_name = 'bboard/create.html'
 form_class = BbForm
 success_url = reverse_lazy('index')

 def get_context_data(self, **kwargs):
  context = super().get_context_data(**kwargs)
  context['rublics'] = Rublic.objects.all()
  return context


def index(request):
 bbs = Bb.objects.all()
 rublics = Rublic.objects.all()
 context = {'bbs': bbs, 'rublics': rublics}
 return render(request, 'bboard/index.html', context)

def by_rublic(request, rublic_id):
 bbs = Bb.objects.filter(rublic=rublic_id)
 rublics = Rublic.objects.all()
 current_rublic = Rublic.objects.get(pk=rublic_id)
 context = {'bbs': bbs, 'rublics': rublics, 'current_rublic': current_rublic}
 return render(request, 'bboard/by_rublic.html', context)