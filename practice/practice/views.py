from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt

def random_page(request):
    return render(request, 'random.html')

def generate_random(request):
    random_number = random.randint(1, 100)
    return HttpResponse(random_number)

def area_page(request):
    return render(request, 'area.html')

@csrf_exempt
def calculate_area(request):
    if request.method == 'POST':
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        print(a,b)
        area = a * b
        return HttpResponse(area)
    
    
