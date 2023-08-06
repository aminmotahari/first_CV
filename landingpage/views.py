from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'index.html')


def portfolio_view(request):
    return render(request, 'portfolio-details.html')
