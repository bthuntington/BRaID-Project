from django.test import TestCase
from django.core.files import File as DjangoFile
from . import utils, models
import factory


# contains test.(extnsion) files for testing
TEST_PATH = 'experiments/test_files/'


# model factories
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


# test cases
class FileMimetypeTests(TestCase):

    """ Check to see that the util class is assigning mimetypes to files
    correclty """
    def test_csv_mimetype_util(self):
        # Check csv file
        csv = CreateCsvFileFactory()
        types = utils.get_mimetype_fields(csv.document.path, models.File)
        self.assertTrue(types[0] == csv.mimetype and
                        types[1] == csv.mimetype_type)

    def test_fasta_mimetype_util(self):
        # Check fasta file
        fasta = CreateFastaFileFactory()
        types = utils.get_mimetype_fields(fasta.document.path, models.File)
        self.assertTrue(types[0] == fasta.mimetype and
                        types[1] == fasta.mimetype_type)


# TODO: Test uploaded file has all fields and saves
