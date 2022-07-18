from django.shortcuts import render
from .models import Hero

# Create your views here.
def heroView(request):
    heros = Hero.objects.all()
    context = {'heros':heros}
    return render(request, 'hero/hero.html',context)