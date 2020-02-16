from django.test import TestCase
from .models import Card
# Create your tests here.ard

## Unit tests
class CardTestClass(TestCase):
    def setUp(self):
        self.manu = Card(
            title='manu',
            desc = 'This is just but a test class'
            )
    def test_instance(self):
        self.assertTrue(isinstance(self.manu,Card))
    def test_save_instance(self):
        self.manu.save()
        cards = Card.objects.all()
        self.assertTrue(len(cards) > 0)
