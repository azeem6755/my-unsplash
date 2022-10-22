from django.urls import path
from .views import CreateProfile


urlpatterns = [
    path('create/', CreateProfile.as_view(), name='api for creating profile')
]
