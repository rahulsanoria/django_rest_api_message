# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from serializers import DetailSerializer
from .models import detailmodel

class DetailViewSet(viewsets.ModelViewSet):
    
    queryset = detailmodel.objects.all()
    serializer_class = DetailSerializer


