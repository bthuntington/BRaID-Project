from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.first_name

class Experiments(models.Model):
    experiment_name = models.CharField(max_length = 100)
    conditions = models.CharField(max_length = 1000, null = True)
    author_ID = models.ForeignKey(Author, on_delete=models.CASCADE)

class Files(models.Model):
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

    experiment_ID = models.ForeignKey(Experiments, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)
    mimetype = models.CharField(
        choices=MIMETYPE, max_length=20, default='Text'
    )
    mimetype_type = models.CharField(
        choices=MIMETYPE_TYPE, max_length=20, default='txt'
    )


class TextFeatures(models.Model):
    number_of_A = models.IntegerField()
    number_of_C = models.IntegerField()
    number_of_G = models.IntegerField()
    number_of_T = models.IntegerField()
    text_file_ID = models.ForeignKey(Files, on_delete=models.CASCADE)

class ImageFeatures(models.Model):
    upto_fifty = models.IntegerField()
    fifty_to_hundred = models.IntegerField()
    hundred_to_one_fifty = models.IntegerField()
    one_fifty_to_two_hundred = models.IntegerField()
    two_hundred_to_two_fifty_five = models.IntegerField()
    image_file_ID = models.ForeignKey(Files, on_delete=models.CASCADE)
