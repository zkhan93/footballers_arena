# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Footballer
from rest_framework import viewsets
from .serializers import FootballerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Footballer to be viewed or edited.
    """
    queryset = Footballer.objects.all().order_by('-rating')
    serializer_class = FootballerSerializer
