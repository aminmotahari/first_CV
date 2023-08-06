from django.urls import path, include
from .views import *

app_name = 'landingpage'

urlpatterns = [
    path('', home_view, name='index'),
    path('portfolio_2/', portfolio_view, name='portfolio'),
    path('about/', about_view, name='about'),
    path('resume/', resume_view, name='resume'),
    path('services/', services_view, name='services'),
    path('portfolio/', portfolio_view2, name='portfolio2'),
    path('contact/', contact_view, name='contact'),
    
]