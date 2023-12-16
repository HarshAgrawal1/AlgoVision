import sys
from django.shortcuts import render,redirect
from .processing.csv_process import train_model 
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User,auth

def login(request):
  # template = loader.get_template('login.html')
  # return HttpResponse(template.render())

  return HttpResponse(request,'login.html')

def signup(request):
  if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        create_pass = request.POST['create_pass']
        confirm_pass=request.POST['confirm_pass']

        data = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=create_pass)
        data.save()
        return redirect('login')

  return render(request, 'signup.html')



def process_csv(request):
  model_name=""
  model_score=None
  if request.method == 'POST':
      if request.FILES.get('csv_file') and request.POST.get('target_value'):
        csv_file = request.FILES['csv_file']
        target_value = request.POST['target_value']
        model_name, model_score = train_model(csv_file, target_value)
        # return JsonResponse({'model_name': model_name, 'model_score': model_score})
        return render(request, 'index.html', {'model_name': model_name, 'model_score': model_score})
      else:
        return JsonResponse({'error': 'Missing CSV file or target value.'}, status=400)

    # Handle GET request or other cases here (if needed)
  return render(request, 'index.html', {'model_name': model_name, 'model_score': model_score})




