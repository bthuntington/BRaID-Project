from django.db import models
from django.dispatch import receiver
from . import utils
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.last_name

class Experiment(models.Model):
    name = models.CharField(max_length = 100)
    condition = models.CharField(max_length = 1000, null = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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
    mimetype = models.CharField(
        choices=MIMETYPE, max_length=20, default='txt'
    )
    mimetype_type = models.CharField(
        choices=MIMETYPE_TYPE, max_length=20, default='txt'
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # save location based on MEDIA_URL and MEDIA_ROOT in ../braid/settings.py
    document = models.FileField()

    def get_absolute_url(self):
        return reverse('experiments:analysis_info', kwargs={'pk': self.pk})

    def print_data(self):

        print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
            \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
            \n\tfile: {}".format(self.experiment, self.path, self.mimetype,
                                 self.mimetype_type, self.name,
                                 self.file_description, self.document))

@receiver(models.signals.post_delete, sender=File)
def post_delete_file(sender, instance, *args, **kwargs):
    instance.document.delete(save=False)

#Checking If working
class Feature_BayesianNetwork(models.Model):
	network_file = models.FileField(default=1)
	BN_files = models.ManyToManyField(File, default=1)


class Feature_FrequentedRegions(models.Model):
	FR_files = models.ManyToManyField(File, default=1)






