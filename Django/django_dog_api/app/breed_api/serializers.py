from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from breed_api.models import Breed


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

    def validate_friendliness(self, value: int) -> int:
        if not 1 <= value <= 5:
            msg = 'Friendliness must be between 1 and 5.'
            raise serializers.ValidationError(msg)
        return value

    def validate_trainability(self, value: int) -> int:
        if not 1 <= value <= 5:
            msg = 'Trainability must be between 1 and 5.'
            raise serializers.ValidationError(msg)
        return value

    def validate_shedding_amount(self, value: int) -> int:
        if not 1 <= value <= 5:
            msg = 'Shedding amount must be between 1 and 5.'
            raise serializers.ValidationError(msg)
        return value

    def validate_exercise_needs(self, value: int) -> int:
        if not 1 <= value <= 5:
            msg = 'Exercise needs must be between 1 and 5.'
            raise serializers.ValidationError(msg)
        return value
