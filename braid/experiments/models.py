from django.db import models

class Author(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20, null = True)

class Experiments(models.Model):
	experimentName = models.CharField(max_length = 100)
	conditions = models.CharField(max_length = 1000, null = True)
	authorID = models.ForeignKey(Author, on_delete=models.CASCADE)

class Files(models.Model):
	experimentID = models.ForeignKey(Experiments, on_delete=models.CASCADE)
	path = models.CharField(max_length = 100)

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

	mimetype = models.CharField(
        choices=MIMETYPE, max_length = 20, default = 'Text'
    )

	mimetype_type = models.CharField(
        choices=MIMETYPE_TYPE, max_length = 20, default = 'txt'
    )


class textFeatures(models.Model):
	numberOfA = models.IntegerField()
	numberOfC = models.IntegerField()
	numberOfG = models.IntegerField()
	numberOfT = models.IntegerField()
	textFileID = models.ForeignKey(Files, on_delete=models.CASCADE)

class imageFeatures(models.Model):
	uptoFifty = models.IntegerField()
	fiftyToHundred = models.IntegerField()
	hundredToOneFifty = models.IntegerField()
	oneFiftyToTwoHundred = models.IntegerField()
	twoHundredToTwoFiftyFive = models.IntegerField()
	imageFileID = models.ForeignKey(Files, on_delete=models.CASCADE)
