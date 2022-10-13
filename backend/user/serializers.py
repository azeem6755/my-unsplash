from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import Profile
from PIL import Image


class AddProfileSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    def save(self, **kwargs):
        super().save(**kwargs)
        img = Image.open(self.image.source)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.source)

    class Meta:
        models = Profile
        fields = '__all__'
