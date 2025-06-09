from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('users/', UserApiView.as_view()),
    
    path('sathi/', SathiListApiView.as_view()),
    path('sathiRUD/<int:pk>/', SathiRUDApiView.as_view()),
]

