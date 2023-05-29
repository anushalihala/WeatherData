from django.urls import path
from . import views

urlpatterns = [
    path('region/<region>/start/<start>/end/<end>/', views.region_timespan, name='region_timespan'),
    path('region/<region>/', views.region_all, name='region_all'),
]