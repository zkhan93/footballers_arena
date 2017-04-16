from .models import Footballer
from rest_framework import serializers


class FootballerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Footballer
        fields = ('name', 'nationality', 'national_position', 'national_kit')
