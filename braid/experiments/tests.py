from django.test import TestCase
from django.core.files import File as DjangoFile
#from . import models
from . import models
import factory


TEST_PATH = 'experiments/test_files/'  # '/home/britney/braid/repos/braid/braid/experiments/test_files'


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


class CreateCsvFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.File

    document = DjangoFile(open(TEST_PATH + 'test.csv'))
    name = document.name
    mimetype = 'Text'
    mimetype_type = 'csv'
    description = 'A test csv file'
    experiment = factory.SubFactory(CreateExperimentFactory)


class CreateFastaFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.File

    document = DjangoFile(open(TEST_PATH + 'test.fasta'))
    name = document.name
    mimetype = 'Text'
    mimetype_type = 'fasta'
    description = 'A test fasta file'
    experiment = factory.SubFactory(CreateExperimentFactory)


# class FileUploadTests(TestCase):

# class FileMimetypeTests(TestCase):

# TODO: Test file mimetypes correctly identified
# TODO: Test uploaded file has all feilds and saves
