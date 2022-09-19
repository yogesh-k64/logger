from dataclasses import fields
from rest_framework import serializers
from .models import Log

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields=['id','latitude','longitude','checked_in']