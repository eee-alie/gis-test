from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import LocationsSeraizlier, LocationDetailSerializer
from .models import Incidences


# Create your views here.
def home(request):
    return render(request, "gis/index.html")


class LocationAPIView(generics.ListAPIView):
    serializer_class = LocationsSeraizlier

    def get_queryset(self):
        qs = Incidences.objects.all()
        return qs

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class LocationDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = LocationDetailSerializer

    def get_object(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        name = self.get_object()
        qs = Incidences.objects.filter(name=name)
        return qs

    def get(self, request, *args, **kwargs):
        # try :

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    # except:
    #    return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')
