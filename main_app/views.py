from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Tama, Toy
from django.contrib import admin
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def tamas_index(request):
  tamas = Tama.objects.filter(user=request.user)
  return render(request, 'tamas/index.html', {'tamas': tamas})

@login_required(login_url='/')
def tamas_detail(request, tama_id):
  tama = Tama.objects.get(id=tama_id)
  toys_tama_doesnt_have = Toy.objects.exclude(id__in = tama.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'tamas/detail.html', {
    'tama': tama, 'feeding_form': feeding_form, 'toys': toys_tama_doesnt_have
  })
  
@login_required(login_url='/')
def assoc_toy(request, tama_id, toy_id):
  Tama.objects.get(id=tama_id).toys.add(toy_id)
  return redirect('tamas_detail', tama_id=tama_id)

@login_required(login_url='/')
def add_feeding(request, tama_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.tama_id = tama_id
    new_feeding.save()
  return redirect('tamas_detail', tama_id=tama_id)

class Home(LoginView):
  template_name = 'home.html'

class TamaCreate(LoginRequiredMixin, CreateView):
  model = Tama
  fields = ['name', 'description', 'age']
  success_url = '/tamas/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TamaUpdate(LoginRequiredMixin, UpdateView):
  model = Tama
  fields = ['name', 'description', 'age']

class TamaDelete(LoginRequiredMixin, DeleteView):
  model = Tama
  success_url = '/tamas/'
  
class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'
  
class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy
  
class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'