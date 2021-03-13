from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Mogwai, Toy
from .forms import FeedingForm, MogwaiForm
from datetime import date, time
# Create your views here.


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')
  # return HttpResponse('<h1>About the CatCollector</h1>')

@login_required
def mogwais_index(request):
  # retrieves all cats from DB
  mogwais = Mogwai.objects.filter(user=request.user)
  return render(request, 'mogwais/index.html', {'mogwais': mogwais})

@login_required
def mogwais_new(request):
  mogwai_form = MogwaiForm(request.POST or None)
  if request.POST and mogwai_form.is_valid():
    new_mogwai = mogwai_form.save(commit=False)
    new_mogwai.user = request.user
    new_mogwai.save()
    return redirect('index')
  else:
    return render(request, 'mogwais/new.html', {'mogwai_form': mogwai_form})  

@login_required
def mogwais_edit(request, mogwai_id):
  mogwai = Mogwai.objects.get(id=mogwai_id)
  mogwai_form = MogwaiForm(request.POST or None, instance=mogwai)
  if request.POST and mogwai_form.is_valid():
    mogwai_form.save()
    return redirect('detail', mogwai_id= mogwai_id)
  else:
    return render(request, 'mogwais/edit.html', {'mogwai': mogwai, 'mogwai_form': mogwai_form})

@login_required
def mogwais_delete(request, mogwai_id):
  Mogwai.objects.get(id=mogwai_id).delete()
  return redirect('index')


@login_required
def mogwais_detail(request, mogwai_id):
  # retrieve a single cat using the ID
  mogwai = Mogwai.objects.get(id=mogwai_id)
  # print(date.today())
  # print(time)
  # print(mogwai.feeding_set.filter(date=date.today()).count())
  toys_mogwai_doesnt_have = Toy.objects.exclude(id__in = mogwai.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  context = {
    'mogwai': mogwai,
    'feeding_form' : FeedingForm(),
    'toys': toys_mogwai_doesnt_have
  }
  return render(request, 'mogwais/detail.html', context)

@login_required
def add_feeding(request, mogwai_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.mogwai_id = mogwai_id
    new_feeding.save()
  return redirect('detail', mogwai_id=mogwai_id)

@login_required
def assoc_toy(request, mogwai_id, toy_id):
  mogwai = Mogwai.objects.get(id=mogwai_id)
  mogwai.toys.add(toy_id)
  return redirect('detail', mogwai_id=mogwai_id)

@login_required
def remove_toy(request, mogwai_id, toy_id):
  mogwai = Mogwai.objects.get(id=mogwai_id)
  mogwai.toys.remove(toy_id)
  return redirect('detail', mogwai_id=mogwai_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
