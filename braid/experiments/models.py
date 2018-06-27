from django.db import models
from django.dispatch import receiver
from . import utils
from django.urls import reverse

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
    analysis_option = models.CharField(max_length=30)
    analysis_type = models.CharField(max_length=10)
    parent_file_id = models.IntegerField()

    def __str__(self):
        return self.analysis_option


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
        choices=MIMETYPE, max_length=20, default='Text'
    )
    mimetype_type = models.CharField(
        choices=MIMETYPE_TYPE, max_length=20, default='txt'
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # save location based on MEDIA_URL and MEDIA_ROOT in ../braid/settings.py
    file_file = models.FileField()

    def get_analysis_types(self):
        # TODO: Change structure analysis are stored in
        """
        content,type_list = utils.set_analysis_options(self.mimetype_type)
        for t in content:

            temp_analysis = Analysis.objects.filter(analysis_option=t,
                                       analysis_type=type_list,
                                       parent_file_id=self.pk)
            # no analysis object exists
            if temp_analysis.count() == 0:
                # make a new one for this file
                temp_analysis = Analysis(analysis_option=t,
                                         analysis_type=type_list,
                                         parent_file_id=self.pk)
            else:
                # TODO: Write test to make sure only one Analysis object is
                # returned
                temp_analysis = temp_analysis[0]
                temp_analysis.save()

            self.analysis_information.add(temp_analysis)
        """
        pass
    def get_absolute_url(self):
        return reverse('experiments:analysis_info', kwargs={'pk': self.pk})

    def print_data(self):

        print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
            \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
            \n\tfile: {}".format(self.experiment, self.path, self.mimetype,
                                 self.mimetype_type, self.name,
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
