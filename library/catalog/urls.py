from django.urls import path
from .views import BookCreate, index, BookDetail


urlpatterns = [path('', index, name='index'), path(
    'create_book/', BookCreate.as_view(), name='create_book'), path('book_detail/<int:pk>', BookDetail.as_view(), name='book_detail'), ]
