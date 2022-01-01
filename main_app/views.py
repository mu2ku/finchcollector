from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Tama:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

tamas = [
  Tama('Mametchi', 'Playful but mischevious', 3),
  Tama('Kuchipatchi', 'Talks a lot', 0),
  Tama('Lovelin', 'Petty and venegeful', 4),
  Tama('Haputchi', 'Does not like interacting with others', 6)
]

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def tamas_index(request):
  return render(request, 'tamas/index.html', {'tamas': tamas})