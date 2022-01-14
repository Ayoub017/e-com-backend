from http import client
from itertools import product
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.relations import ManyRelatedField
from rest_framework.response import Response
from .serializers import PersonSerializer, ProductSerializer, CommandeSerializer
from .models import  Person, Product, Commande
from django.contrib.auth.models import AbstractUser, User 
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password,make_password
from rest_framework import status    
from django.views.decorators.csrf import csrf_exempt








# Create your views here.
@api_view(['GET'])
def getpersons(request):
    persons = Person.objects.all()
    serialization = PersonSerializer(persons,many=True)
    return Response(serialization.data)



@api_view(['GET'])
def getPersonByUsername(request,username):
   # id=request.GET.get('id');
    person = Person.objects.get(username=username)
    serialization = PersonSerializer(person)
    return Response(serialization.data)

@api_view(['POST'])
def addPersons(request):
    print(request.data[0]['password'])
    request.data[0]['password'] = make_password(request.data[0]['password'])
 
    serializer = PersonSerializer(data=request.data,many=True)
    if serializer.is_valid():
        serializer.save()
        # persons = Person.objects.all()
        # persons.last().password = make_password(persons.last().password)
        # persons.last().save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatePerson(request,id):
    person = Person.objects.get(id=id)
    serializer = PersonSerializer(instance = person, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePerson(request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return Response("Bien supprimée")


@api_view(['POST'])
def addProduct(request):
    # serializer = ProductSerializer(data=request.data,many=True)
    # if serializer.is_valid():
    #     serializer.save()
    # return Response(serializer.data)
  product= Product.objects.create(titre =request.data[0]['titre'] ,category =request.data[0]['category'], price=request.data[0]['price'] ,image = request.data[0]['image'], person =Person.objects.get(id=int(request.data[0]['person'])) );

  product.save()
  serialization = ProductSerializer(product)
  return Response(serialization.data)

@api_view(['GET'])
def getProducts(request):
     products = Product.objects.all()
     serialization = ProductSerializer(products,many=True)
     return Response(serialization.data)

@api_view(['GET'])
def authentication(request):
            username=request.GET.get('username');
            password=request.GET.get('password');
            type=request.GET.get('type');
            user = Person.objects.get(username=username,type=type)

            if check_password(password, user.password) or user.password == password :
                serializer = PersonSerializer(instance = user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def getCommandes(request):
     commandes= Commande.objects.all()
     serialization = CommandeSerializer(commandes,many=True)
     return Response(serialization.data)

@api_view(['GET'])
def getCommandesByIdClient(request,id):
     commandes= Commande.objects.filter(client_id=id)
     serialization = CommandeSerializer(commandes,many=True)
     return Response(serialization.data)

@api_view(['PUT'])
def updateCommandeStatus(request):
    id =request.GET.get('id');
    status =request.GET.get('status');
    commande = Commande.objects.get(id=id)
    commande.status = status
    commande.save()
    serializer = CommandeSerializer(instance = commande)
    return Response(serializer.data)