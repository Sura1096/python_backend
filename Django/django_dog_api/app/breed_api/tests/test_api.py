import json

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from breed_api.models import Breed
from breed_api.serializers import BreedSerializer


class BreedListApiTestCase(APITestCase):
    def setUp(self):
        self.breed = Breed.objects.create(
            name='Golden Retriever',
            size='Medium',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=4,
        )

        self.client = APIClient()

    def test_get_breed_list(self):
        response = self.client.get('/api/breeds/')
        serializer_data = BreedSerializer([self.breed], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_post_breed_object(self):
        self.assertEqual(1, Breed.objects.all().count())
        new_breed_object = {
            'name': 'Shepherd',
            'size': 'Large',
            'friendliness': 5,
            'trainability': 5,
            'shedding_amount': 5,
            'exercise_needs': 5,
        }
        json_data = json.dumps(new_breed_object)

        response = self.client.post(
            '/api/breeds/',
            data=json_data,
            content_type='application/json',
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(2, Breed.objects.all().count())


class DogDetailApiTestCase(APITestCase):
    def setUp(self):
        self.breed = Breed.objects.create(
            name='Golden Retriever',
            size='Medium',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=4,
        )

        self.client = APIClient()

    def test_get_breed_by_id(self):
        breed_obj = Breed.objects.get(pk=self.breed.id)
        response = self.client.get(f'/api/breeds/{self.breed.id}')
        serializer = BreedSerializer(breed_obj).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer, response.data)

    def test_put_breed_obj_by_id(self):
        update_breed_obj = {
            'name': 'Doberman',
            'size': 'Large',
            'friendliness': 5,
            'trainability': 5,
            'shedding_amount': 5,
            'exercise_needs': 5,
        }
        json_data = json.dumps(update_breed_obj)
        response = self.client.put(
            f'/api/breeds/{self.breed.id}',
            data=json_data,
            content_type='application/json',
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.breed.refresh_from_db()
        self.assertEqual('Doberman', self.breed.name)

    def test_delete_breed_obj_by_id(self):
        response = self.client.delete(f'/api/breeds/{self.breed.id}')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(Breed.objects.filter(pk=self.breed.id).exists())
