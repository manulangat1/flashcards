from rest_framework import serializers
from .models import Card,Category


class CategorySerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = (
            'id',
            'course',
            'cards'
        )
    def get_cards(self,obj):
        return CardsSerializer(obj.courses.all(),many=True).data
class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            # 'course',
            'title',
            'desc',
        )
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        # fields = '__all__'
        fields = (
            'id',
            'course',
            'title',
            'desc',
        )