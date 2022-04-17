from django.urls import path

from .views import home, LocationAPIView, LocationDetailsAPIView


urlpatterns = [
    path('', home, name='home'),
    path('location', LocationAPIView.as_view()),
    path('location/<str:pk>', LocationDetailsAPIView.as_view()),
]
