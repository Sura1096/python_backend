from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from breed_api.models import Breed
from breed_api.serializers import BreedSerializer


class BreedList(APIView):
    """List all breeds, or create a new breed."""

    def get(self, request: Request):
        breed_queryset = Breed.objects.all()
        serializer = BreedSerializer(breed_queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """Retrieve, update or delete a breed instance."""

    def __get_object(self, pk: int):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        breed_obj = self.__get_object(pk)
        serializer = BreedSerializer(breed_obj)
        return Response(serializer.data)

    def put(self, request: Request, pk: int):
        breed_obj = self.__get_object(pk)
        serializer = BreedSerializer(breed_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        breed_obj = self.__get_object(pk)
        breed_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
