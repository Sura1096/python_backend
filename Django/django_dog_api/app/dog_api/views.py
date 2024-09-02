from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from dog_api.models import Dog
from dog_api.serializers import DogSerializer


class DogList(APIView):
    """List all dogs, or create a new dog."""

    def get(self, request: Request) -> Response:
        dog_queryset = Dog.objects.all()
        serializer = DogSerializer(dog_queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """Retrieve, update or delete a dog instance."""

    def __get_object(self, pk: int):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        dog_obj = self.__get_object(pk)
        serializer = DogSerializer(dog_obj)
        return Response(serializer.data)

    def put(self, request: Request, pk: int):
        dog_obj = self.__get_object(pk)
        serializer = DogSerializer(dog_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        dog_obj = self.__get_object(pk)
        dog_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
