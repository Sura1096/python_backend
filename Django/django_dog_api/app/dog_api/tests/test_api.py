import json

from breed_api.models import Breed
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from dog_api.models import Dog
from dog_api.serializers import DogSerializer


class DogListApiTestCase(APITestCase):
    def setUp(self):
        self.breed = Breed.objects.create(
            name='Golden Retriever',
            size='Medium',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=4,
        )

        self.dog = Dog.objects.create(
            name='Buddy',
            age=3,
            breed=self.breed,
            gender='Male',
            color='Golden',
            favorite_food='Bones',
            favorite_toy='Tennis ball',
        )

        self.client = APIClient()

    def test_get_dog_list(self):
        response = self.client.get('/api/dogs/')
        serializer_data = DogSerializer([self.dog], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_post_dog_object(self):
        self.assertEqual(1, Dog.objects.all().count())
        new_dog_object = {
            'name': 'Vega',
            'age': 3,
            'breed': self.breed.id,
            'gender': 'Male',
            'color': 'Golden',
            'favorite_food': 'Bones',
            'favorite_toy': 'Tennis ball',
        }
        json_data = json.dumps(new_dog_object)

        response = self.client.post(
            '/api/dogs/',
            data=json_data,
            content_type='application/json',
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(2, Dog.objects.all().count())


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

        self.dog = Dog.objects.create(
            name='Vega',
            age=3,
            breed=self.breed,
            gender='Male',
            color='Golden',
            favorite_food='Bones',
            favorite_toy='Tennis ball',
        )

        self.client = APIClient()

    def test_get_dog_by_id(self):
        dog_obj = Dog.objects.get(pk=self.dog.id)
        response = self.client.get(f'/api/dogs/{self.dog.id}')
        serializer = DogSerializer(dog_obj).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer, response.data)

    def test_put_dog_obj_by_id(self):
        update_dog_obj = {
            'name': 'Vegas',
            'age': 3,
            'breed': self.breed.id,
            'gender': 'Male',
            'color': 'Golden',
            'favorite_food': 'Bones',
            'favorite_toy': 'Tennis ball',
        }
        json_data = json.dumps(update_dog_obj)
        response = self.client.put(
            f'/api/dogs/{self.dog.id}',
            data=json_data,
            content_type='application/json',
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.dog.refresh_from_db()
        self.assertEqual('Vegas', self.dog.name)

    def test_delete_dog_obj_by_id(self):
        response = self.client.delete(f'/api/dogs/{self.dog.id}')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(Dog.objects.filter(pk=self.dog.id).exists())
