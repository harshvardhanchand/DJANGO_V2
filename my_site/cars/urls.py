from django.urls import path
from .import views

app_name = 'cars'


urlpatterns = [path('rental_review/', views.rental_view, name='rental_review'),
               path('thank_you/', views.thankyou_view, name='thank_you'), ]
