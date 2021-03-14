from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import uuid
import boto3
from .models import Mogwai, Toy, Photo
from .forms import FeedingForm, MogwaiForm
from datetime import date, time
from django.contrib import messages

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'cat-collector-sei-bp'

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


@login_required
def mogwais_index(request):
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
  mogwai = Mogwai.objects.get(id=mogwai_id)
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
  hour = request.POST.get('time')
  hour = int(hour[0:2])
  after_midnight = hour < 5  
  if form.is_valid() and not after_midnight:
    new_feeding = form.save(commit=False)
    new_feeding.mogwai_id = mogwai_id
    new_feeding.save()
    return redirect('detail', mogwai_id=mogwai_id)
  else:
    messages.warning(request, "YOU ARE IN SERIOUS DANGER, It's too late to feed the Mogawai!!!") 
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

@login_required
def add_photo(request, mogwai_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        # Assign to mogwai_id or mogwai (if you have a mogwai object)
        photo = Photo(url=url, mogwai_id=mogwai_id)
        photo.save()
    except:
        print('An error occurred uploading file to S3')
  return redirect('detail', mogwai_id=mogwai_id)
