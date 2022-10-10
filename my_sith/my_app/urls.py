from django.urls import path
from . import views


app_name = 'my_app'  # special variable
urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variables'),
]
