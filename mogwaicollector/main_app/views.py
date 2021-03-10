from django.shortcuts import render, redirect
from .models import Mogwai
from .forms import FeedingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
  return render(request, 'about.html')
  # return HttpResponse('<h1>About the CatCollector</h1>')

def mogwais_index(request):
  # retrieves all cats from DB
  mogwais = Mogwai.objects.all()
  return render(request, 'mogwais/index.html', {'mogwais': mogwais})

def mogwais_detail(request, mogwai_id):
  # retrieve a single cat using the ID
  mogwai = Mogwai.objects.get(id=mogwai_id)
  context = {
    'mogwai': mogwai,
    'feeding_form' : FeedingForm()
  }
  return render(request, 'mogwais/detail.html', context)

def add_feeding(request, mogwai_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.mogwai_id = mogwai_id
    new_feeding.save()
  return redirect('detail', mogwai_id=mogwai_id)