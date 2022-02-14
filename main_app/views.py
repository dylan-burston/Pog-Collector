from django.shortcuts import render

from .models import Pog

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return render(request, 'home.html') 

# def index(request):
#     pogs = Pog.objects.all()
#     return render(request, 'index.html', { 'pogs': pogs }) 

def show(request, pog_id):
    pog = Pog.objects.get(id=pog_id)
    return render(request, 'show.html', {'pog': pog})

class PogList(ListView):
  model = Pog

class PogCreate(CreateView):
  model = Pog
  fields = '__all__'
  success_url = '/pogs/'

class PogUpdate(UpdateView):
  model = Pog
  fields = ['name', 'color']
  success_url = '/pogs/'

class PogDelete(DeleteView):
  model = Pog
  success_url = '/pogs/'