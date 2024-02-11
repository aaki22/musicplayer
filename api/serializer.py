from rest_framework import serializers
from .models import room

class Room_Serializers(serializers.ModelSerializer):
    class Meta:
        model=room
        fields=('id','code','host','guest_can_pause','vote_to_skip','created_at')