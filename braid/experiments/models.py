from django.db import models
from django.dispatch import receiver
from . import utils

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.first_name

class Experiment(models.Model):
    name = models.CharField(max_length = 100)
    condition = models.CharField(max_length = 1000, null = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Analysis(models.Model):
    analysis_type = models.CharField(max_length=30)

    def __str__(self):
        return self.analysis_type


class File(models.Model):
    MIMETYPE = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Text', 'Text'),
        ('Unknown', 'Unknown'),
        ('Image', 'Image'),
    )

    MIMETYPE_TYPE=(
        ('jpg', 'jpg'),
        ('png', 'png'),
        ('gif', 'gif'),
        ('mp4', 'mp4'),
        ('tif', 'tif'),
        ('avi', 'avi'),
        ('fasta', 'fasta'),
        ('txt', 'txt'),
        ('csv', 'csv'),
        ('xls', 'xls'),
        ('unknown', 'unknown'),
    )

    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)
    mimetype = models.CharField(
        choices=MIMETYPE, max_length=20, default='Text'
    )
    mimetype_type = models.CharField(
        choices=MIMETYPE_TYPE, max_length=20, default='txt'
    )
    file_name = models.CharField(max_length=100)
    file_description = models.CharField(max_length=500)
    # save location based on MEDIA_URL and MEDIA_ROOT in ../braid/settings.py
    file_file = models.FileField()
    analysis_information = models.ManyToManyField(Analysis)

    def get_analysis_types(self):
        types = utils.set_analysis_options(self.mimetype_type)
        for t in types:
            temp_analysis = Analysis(analysis_type=t)
            temp_analysis.save()
            self.analysis_information.add(temp_analysis)

    def print_data(self):

        print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
            \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
            \n\tfile: {}".format(self.experiment, self.path, self.mimetype,
                                 self.mimetype_type, self.file_name,
                                 self.file_description, self.file_file))
@receiver(models.signals.post_delete, sender=File)
def post_delete_file(sender, instance, *args, **kwargs):
    instance.file_file.delete(save=False)

class TextFeature(models.Model):
    number_of_A = models.IntegerField()
    number_of_C = models.IntegerField()
    number_of_G = models.IntegerField()
    number_of_T = models.IntegerField()
    text_file = models.ForeignKey(File, on_delete=models.CASCADE)

class ImageFeature(models.Model):
    upto_fifty = models.IntegerField()
    fifty_to_hundred = models.IntegerField()
    hundred_to_one_fifty = models.IntegerField()
    one_fifty_to_two_hundred = models.IntegerField()
    two_hundred_to_two_fifty_five = models.IntegerField()
    image_file = models.ForeignKey(File, on_delete=models.CASCADE)
