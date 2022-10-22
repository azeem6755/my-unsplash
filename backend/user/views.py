from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.db import transaction
from .serializers import AddProfileSerializer
from .utils import create_profile_helper
# Create your views here.


class CreateProfile(GenericAPIView):

    serializer_class = AddProfileSerializer

    @transaction.atomic()
    def post(self, request):
        try:
            response = create_profile_helper(self, request)
            print(response)
            return response
        except Exception:
            pass
