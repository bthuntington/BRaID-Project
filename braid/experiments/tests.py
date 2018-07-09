from django.test import TestCase
from . import models
import factory


class CreateAuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Author

    first_name = 'Jane'
    last_name = 'Doe'


class CreateExperimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Experiment

    name = 'Test'
    condition = 'test'
    author = factory.SubFactory(CreateAuthorFactory)


# class CreateFileFactory(factory.django.DjangoModelFactory):

# class FileUploadTests(TestCase):

# class FileMimetypeTests(TestCase):

# TODO: Test file mimetypes correctly identified
# TODO: Test uploaded file has all fields and saves
