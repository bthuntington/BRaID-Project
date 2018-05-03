from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.first_name

class Experiment(models.Model):
    experiment_name = models.CharField(max_length = 100)
    conditions = models.CharField(max_length = 1000, null = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

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
