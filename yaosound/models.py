from django.db import models
from mongoengine import *


class MachineModel(Document):

    name =StringField(max_length=16)
    numbers = IntField(default=0)
# Create your models here.
