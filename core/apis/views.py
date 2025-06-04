from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from api import models
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class SathiListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Sathi.objects.all()
    serializer_class = SathiSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
class SathiUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Sathi.objects.all()
    serializer_class = SathiSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



# class SathiViewSet(viewsets.ModelViewSet):
#     queryset = models.Sathi.objects.all()
#     serializer_class = SathiSerializer

# class SathiListCreateApiView(APIView):
#     def get(self, request):
#         sathi = Sathi.objects.all()
#         serializer = SathiSerializer(sathi, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = SathiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class SathiDetailApiView(APIView):
#     def get(self,request, pk):
#         sathi = get_object_or_404(Sathi, pk=pk)
#         serializer = SathiSerializer(sathi)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         sathi = get_object_or_404(Sathi, pk=pk)
#         serializer = SathiSerializer(sathi, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         sathi = get_object_or_404(Sathi, pk=pk)
#         sathi.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    # class SathiList(generics.ListCreateAPIView):
#     queryset = models.Sathi.objects.all()
#     serializer_class = SathiSerializer
    
# class SathiDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Sathi.objects.all()
#     serializer_class = SathiSerializer
