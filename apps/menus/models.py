from turtle import title
from django.db import models
from django.contrib.auth.models import User
import uuid


class Menu(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    menu_day = models.DateField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    options = models.ManyToManyField('MenuOption', blank=True)

    def __str__(self):
        return str(self.title)


class MenuOption(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    option_title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.option_title
