from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Log
from .serializers import AttendanceSerializer

# Create your views here.

class AttendanceLogsView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Log.objects.all().order_by('checked_in')
    serializer_class=AttendanceSerializer
