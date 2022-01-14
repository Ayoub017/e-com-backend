from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed
from .models import Person, Product, Commande
class PersonSerializer(serializers.ModelSerializer):
    class Meta :
        model = Person
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        # person = serializers.CharField(source='person.person', read_only=True)

        model = Product
        fields = '__all__'
        depth = 1

class CommandeSerializer(serializers.ModelSerializer):
    class Meta :
        # person = serializers.CharField(source='person.person', read_only=True)

        model = Commande
        fields = '__all__'
        depth = 1