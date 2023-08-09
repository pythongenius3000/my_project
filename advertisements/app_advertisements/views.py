from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Advertisements
def index(request):
    advertisements = Advertisements.objects.all() #результат - queryset(3)
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')