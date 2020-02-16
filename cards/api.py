from .models import Card,Category
from .serializers import CardSerializer,CategorySerializer

from rest_framework import generics
from rest_framework.response import Response

class CardAPI(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
class CategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer