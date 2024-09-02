from django.contrib import admin

from dog_api.models import Breed, Dog

admin.site.register(Dog)
admin.site.register(Breed)
