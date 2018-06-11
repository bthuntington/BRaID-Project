from django.test import TestCase
from .models import Author, Experiment, File

def create_test_objects():
    print("Do something!!!")
    author_1 = Author(first_name='Jane', last_name='Doe')
    author_1.save()
    experiment_1 = Experiment(name='Metagenome',condition='acidic',author=author_1)
    experiment_1.save()
# 

# Create your tests here.
