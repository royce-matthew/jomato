# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jsec.models import Stall, Review, Rating
from jsec.serializers import StallSerializer,ReviewSerializer,RatingSerializer
from rest_framework import status
# Create your views here.

def index(request):
	return render(request, 'index.html', context=None)

def single(request):
	return render(request, 'single.html', context=None)


@api_view(['GET', 'POST'])
def stall_list(request):
    if request.method == 'GET':
        stalls = Stall.objects.all()
        serializer = StallSerializer(stalls, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def stall_detail(request, pk):
    try:
        stall = Stall.objects.get(pk=pk)
    except Stall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StallSerializer(stall)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StallSerializer(stall, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@csrf_exempt
def stall_reviews(request, pk, format=None):
    
    review = Review.objects.all().filter(stall_id=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
