from rest_framework import serializers, viewsets
from .models import Room


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Room
        fields = ('id','title', 'description','n_to','s_to','w_to','e_to')