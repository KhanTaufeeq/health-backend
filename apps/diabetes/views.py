from django.shortcuts import render
from . models import Diabetes
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def csrf(request):
  return JsonResponse({"csrfToken" : get_token(request)})

@csrf_exempt
def add_sugar(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      fasting_data = data.get('fasting_sugar')
      random_data = data.get('random_sugar')

      diabetes = Diabetes.objects.create(fasting_sugar = fasting_data, random_sugar = random_data)
      diabetes.save() 
      return JsonResponse({"message": "Data has been added successfully"}, status = 200)
    except json.JSONDecodeError:
      return JsonResponse({"error" : "Invalid JSON data"}, status = 400) 
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)
  

def list_data(request):
  if request.method == 'GET':
    items = Diabetes.objects.order_by('-created_at')
    data = list(items.values('id', 'fasting_sugar', 'random_sugar', 'created_at'))
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({'error': "Invalid request method"}, status = 405)
  

  
@csrf_exempt
def delete_sugar(request, sugar_id):
  if request.method == 'DELETE':
    data = Diabetes.objects.get(id = sugar_id)
    data.delete()
    items = Diabetes.objects.order_by('-created_at')
    ordered_items = list(items.values('id', 'fasting_sugar', 'random_sugar', 'created_at'))
    return JsonResponse(ordered_items, safe=False)
  else:
    return JsonResponse({"error" : "Invalid request method"}, status = 405) 
  

@csrf_exempt
def update_sugar(request, sugar_id):
  if request.method == 'PUT':
    try:
      data = json.loads(request.body)
      fasting_data = data.get('fasting_sugar')
      random_data = data.get('random_sugar') 

      sugar_object = Diabetes.objects.get(id = sugar_id) 

      if fasting_data:
        sugar_object.fasting_sugar = fasting_data 
      if random_data:
        sugar_object.random_sugar = random_data 
      sugar_object.save()
      return JsonResponse({"message" : "Diabetes data has been updated successfully"}, status = 200) 
    except sugar_object.DoesNotExist:
      JsonResponse({"error" : "There is no such Diabetes object"}, status = 404)
  else:
    return JsonResponse({"error" : "Invalid request method"}, status = 405)
