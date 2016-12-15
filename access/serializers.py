from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    user_first_name = serializers.CharField(source='user.first_name',
                                            read_only=True)
    user_last_name = serializers.CharField(source='user.last_name',
                                           read_only=True)
    user_level = serializers.CharField(source='user.user_profile.level',
                                       read_only=True)
    can_open_doors = serializers.BooleanField(
        source='user.user_profile.level.can_open_doors',
        read_only=True)

    class Meta:
        model = Card
        fields = ('user', 'user_first_name', 'user_last_name',
                  'user_level', 'can_open_doors',
                  'serial_number',
                  'pin_code')
