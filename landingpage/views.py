from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'website/index.html')


def portfolio_view(request):
    return render(request, 'website/portfolio-details.html')


def about_view(request):
    return render(request, 'website/about.html')


def resume_view(request):
    return render(request, 'website/resume.html')


def services_view(request):
    return render(request, 'website/services.html')


def portfolio_view2(request):
    return render(request, 'website/portfolio.html')


def contact_view(request):
    return render(request, 'website/contact.html')

