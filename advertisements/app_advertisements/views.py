from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
from .models import Advertisements
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisements.objects.all() #результат - queryset(3)
    context = {'advertisements': advertisements}
    return render(request, 'app_adv/index.html', context)

def top_sellers(request):
    return render(request, 'app_adv/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_adv/advertisement-post.html', context)

