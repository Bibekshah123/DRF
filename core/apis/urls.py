from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", SathiViewSet, basename='sathi')
urlpatterns = router.urls

# urlpatterns = [
#     path('sathi/', SathiLisCreateApiView.as_view(), name='sathi-list'),
#     path('sathi/<int:pk>/', SathiDetailApiView.as_view(), name='sathi-detail'),
# ]
