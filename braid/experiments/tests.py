# from django.test import TestCase
from . import models


def create_test_objects():
    author_1 = models.Author.objects.create(first_name='Jane', last_name='Doe')
    models.Experiment.objects.create(name='Test', condition='test',
                                     author=author_1)
