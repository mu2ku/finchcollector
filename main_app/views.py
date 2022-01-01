from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tama
from django.contrib import admin

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
  return render(request, 'tamas/detail.html', { 'tama': tama })

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