from django.shortcuts import render

from rest_framework import generics
from .serializers import RecordSerializer
from .models import Record

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all().order_by('id')
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all().order_by('id')
    serializer_class = RecordSerializer
