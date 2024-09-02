from rest_framework.serializers import ModelSerializer

from breed_api.models import Breed


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
