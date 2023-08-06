from django.urls import path, include
from .views import *

app_name = 'landingpage'

urlpatterns = [
    path('', home_view, name='index'),
    path('portfolio/', portfolio_view, name='portfolio'),
    #path('', about_view, name='about'),
    #path('', resume_view, name='resume'),
    #path('', services_view, name='services'),
    #path('', portfolio_view, name='portfolio'),
    #path('', contact_view, name='contact'),
    
]