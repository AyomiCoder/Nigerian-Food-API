from urllib import request
from django.http import JsonResponse
from .models import NigerianFood
from .serializers import NigerianFoodSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def naija_foods(request, format=None):

    if request.method == 'GET':
            naija_foods = NigerianFood.objects.all()
            serializer = NigerianFoodSerializer(naija_foods, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
            serializer = NigerianFoodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def food_details(request, id, format=None):

    try:
        nigerianfood = NigerianFood.objects.get(pk=id)
    except NigerianFood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = NigerianFoodSerializer(nigerianfood)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NigerianFoodSerializer(nigerianfood, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        nigerianfood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)