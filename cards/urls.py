from django.urls import path
from .api import CardAPI,CategoryAPI,CategoryDetailAPI

urlpatterns = [
    path('',CardAPI.as_view(),name='cards'),
    path('category/',CategoryAPI.as_view(),name='category'),
    path('category/<pk>/',CategoryDetailAPI.as_view(),name='category_detail'),
]