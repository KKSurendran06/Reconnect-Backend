from rest_framework import serializers
from .models import EventPage , RaiseHand , RequestInsitute , InstituteDetails , EditProfile


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPage
        fields = '__all__'

class RaiseHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaiseHand
        fields = '__all__'

class RequestInsituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInsitute
        fields = '__all__'

class InstituteDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteDetails
        fields = '__all__'

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditProfile
        fields = '__all__'
