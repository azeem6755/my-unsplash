from rest_framework.response import Response
from rest_framework import status
from .models import Profile
import traceback
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def create_profile_helper(self, request):
    try:
        user_obj = Profile.objects.filter(username=request.data['username'])
        if user_obj.exists():
            return Response({
                'message': 'User already exists',
                'success': False,
                'data': None,
                'status': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            user_details = dict()
            user_details['is_superuser'] = 0
            user_details['first_name'] = serializer.validated_data['first_name']
            user_details['last_name'] = serializer.validated_data['last_name']
            user_details['username'] = serializer.validated_data['username']
            user_details['is_staff'] = 0
            user_details['is_active'] = 1
            user_details['date_joined'] = datetime.now()
            user_details['password'] = make_password(request.data['password'])
            user = User.objects.create(**user_details)
            instance.user = user
            instance.save()

            return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Profile Created',
                'data': {'user_id': serializer.data['id']}},
                status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': handle_errors(serializer.errors),
                'data': None},
                status=status.HTTP_400_BAD_REQUEST)

    except Exception:
        traceback.print_exc()


def handle_errors(serializer_errors):
    # print(serializer_errors)
    response = {}
    response['errors'] = []
    for key,value in serializer_errors.items():
        response["errors"].append('{} - {}'.format(key, value[0]))
    # print(response['errors'][0])
    return response['errors']