from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import BP
from django.middleware.csrf import get_token

# Create your views here.

def csrf(request):
  return JsonResponse({"csrfToken" : get_token(request)})

@csrf_exempt
def add_bp(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      bp_data1 = data.get('systolic')
      bp_data2 = data.get('diastolic')
      bp_timing = data.get('timing')

      bp = BP.objects.create(systolic = bp_data1, diastolic = bp_data2, timing = bp_timing)
      bp.save()
      return JsonResponse({"message" : "Data has been added successfully"}, status = 200)
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid json data"}, status = 400)
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405) 
  

def list_bp(request):
  if request.method == 'GET':
    items = BP.objects.order_by('-created_at')
    data = list(items.values('systolic','diastolic','timing', 'created_at'))
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse({"error": "Invalid request method"}, status = 405)