from rest_framework.serializers import ModelSerializer

from dog_api.models import Dog


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
