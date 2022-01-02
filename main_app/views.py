from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Tama, Toy
from django.contrib import admin
from .forms import FeedingForm

admin.site.register(Tama)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tamas_index(request):
  tamas = Tama.objects.all()
  return render(request, 'tamas/index.html', {'tamas': tamas})

def tamas_detail(request, tama_id):
  tama = Tama.objects.get(id=tama_id)
  feeding_form = FeedingForm()
  return render(request, 'tamas/detail.html', {
    'tama': tama, 'feeding_form': feeding_form
  })

def add_feeding(request, tama_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.tama_id = tama_id
    new_feeding.save()
  return redirect('tamas_detail', tama_id=tama_id)

class TamaCreate(CreateView):
  model = Tama
  fields = '__all__'
  success_url = '/tamas/'
  
class TamaUpdate(UpdateView):
  model = Tama
  fields = '__all__'

class TamaDelete(DeleteView):
  model = Tama
  success_url = '/tamas/'
  
class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'