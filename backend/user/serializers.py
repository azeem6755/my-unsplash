from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import Profile
from PIL import Image


class AddProfileSerializer(serializers.ModelSerializer):

    # password = serializers.Field()

    class Meta:
        model = Profile
        fields = '__all__'
