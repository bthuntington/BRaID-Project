from django.core.management.base import BaseCommand

from experiments.models import (
    Author, Experiment, File, ImageFeature, TextFeature
)

def clean_db():
    Author.objects.all().delete()
    Experiment.objects.all().delete()
    File.objects.all().delete()
    ImageFeature.objects.all().delete()
    TextFeature.objects.all().delete()

# do I need to do this or is there already a library??
MIME_TYPES = {
    'tif': 'Image',
    'png': 'Image',
    'xlsx': 'Text',
    'xls': 'Text',
    'lif': 'Text',
    'fastq': 'Text',
    'z' : 'Text',
    'txt' : 'Text',
    'avi': 'Video',
    'unknown': 'Unknown', # TODO: we defined... is this correct?
    'zip' : 'Unknown',
    'gz' : 'Unknown',
}


def create_author(first_name):
    return Author.objects.create(first_name=first_name)


def create_authors(first_names):
    return [create_author(first) for first in first_names]


def create_experiment(name, author):
    return Experiment.objects.create(name=name, author=author)


def create_file(experiment, path, mimetype_type):
    return File.objects.create(
        experiment=experiment,
        path=path,
        mimetype=MIME_TYPES[mimetype_type],
        mimetype_type=mimetype_type)


def create_genome_file(experiment, path, mimetype_type,
                       num_A, num_C, num_G, num_T):
    f = create_file(experiment, path, mimetype_type)
    TextFeature.objects.create(
        number_of_A=num_A,
        number_of_C=num_C,
        number_of_G=num_G,
        number_of_T=num_T,
        text_file=f)
    return f


def create_image_file(experiment, path, mimetype_type,
                      bin0, bin50, bin100, bin150, bin200):
    f = create_file(experiment, path, mimetype_type)
    ImageFeature.objects.create(
        upto_fifty=bin0,
        fifty_to_hundred=bin50,
        hundred_to_one_fifty=bin100,
        one_fifty_to_two_hundred=bin150,
        two_hundred_to_two_fifty_five=bin200,
        image_file=f)
    return f

def init_experiment(author_name, name, data):
    author = create_author(author_name)
    experiment = create_experiment(name, author)
    for entry in data:
        f = create_file(experiment, entry[0], entry[1])
    return author, experiment

def create_data():
    init_experiment(
        'Camilleri',
        'CamilleriDataSet',
        (
            ('data/ImageData/CamilleriDataSet/co-culture-confocal-T600-LC', 'tif'),
            ('data/ImageData/CamilleriDataSet/example co-culture biofilm-LC', 'xlsx'),
        )
    )
    init_experiment(
        'Franco',
        'FrancoDataSet',
        (
            ('data/ImageData/FrancoDataSet/EAL-10230x', 'png'),
            ('data/ImageData/FrancoDataSet/EAL-23000x', 'png'),
            ('data/ImageData/FrancoDataSet/EDL-1430x', 'png'),
            ('data/ImageData/FrancoDataSet/EDL-17700x', 'png'),
        )
    )
    init_experiment(
        'Pettygrove',
        'PettygroveDataSet',
        (
            ('data/ImageData/PettygroveDataSet/11-16-2017/CFU Counts 11-16','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Experiment','lif'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Growth Data 11-16 v2','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Growth Data 11-16','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Patrol Data 11-16','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 1','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 2','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 3','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 4','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 5','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 5','xls'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 6','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 6','xls'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 7','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 7','xls'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 8 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Pos 8','avi'),
            ('data/ImageData/PettygroveDataSet/11-16-2017/Speed Data 11-16-2017','xlsx'),
            ######################################################
            ('data/ImageData/PettygroveDataSet/11-28-2017/CFU Counts 11-28','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Experiment','lif'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Growth Data 11-28','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Patrol Data 11-28','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 1','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 2','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 3','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 4','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 5','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 5 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 5','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 6','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 6 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 6','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 7','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 7','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 7 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 8 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 8','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 8','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Speed Data 11-28-2017','xlsx'),
            #################################################################
            ('data/ImageData/PettygroveDataSet/12-5-2017/CFU Counts 12-5','xlsx'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Experiment','lif'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Growth Data 12-5-2017','xlsx'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Patrol Data 12-5-2017','xlsx'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 1','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 2','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 3','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 4','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 5','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 5 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 5 Green','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 6','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 6 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 6 Green','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 7','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 7 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 7 Green','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 8','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 8 Gray','avi'),
            ('data/ImageData/PettygroveDataSet/12-5-2017/Pos 8 Green','avi'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 5','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 6','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 7','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Pos 8','xls'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Speed Data 12-5-2017','xlsx'),
            ('data/ImageData/PettygroveDataSet/11-28-2017/Tile Data 12-5-2017','xlsx'),
        )
    )

    (luke, luke_experiment) = init_experiment(
        'Luke',
        'LukeDataSet',
        (
            ('data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R1','fastq'),
            ('data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R2','fastq'),
            ('data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R2.fastq','zip'),
            ('data/OmicsData/LukeDataset/LargeMetagenome/PKF9-READ_IDs.cPickle','z'),
            ('data/OmicsData/LukeDataset/LargeMetagenome/PKF9-STATS','txt'),
            ('data/OmicsData/LukeDataset/LargeMetagenome/ziSWHTdA','unknown'),
            ###########################################
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_c','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_d','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_e','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_f','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_g','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_h','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_i','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_j','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_k','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_l','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_m','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_n','tif'),
            ################################################
            ('data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R1_001','fastq'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R2_001','fastq'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R1_001.fastq','gz'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R2_001.fastq','gz'),

            ('data/OmicsData/LukeDataset/SmallMetagenome/R1_pe','unknown'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/R1_se','unknown'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/R2_pe','unknown'),
            ('data/OmicsData/LukeDataset/SmallMetagenome/R1_se','unknown'),

        )
    )

    # create some text features
    create_genome_file(
        luke_experiment,
        'data/OmicsData/LukeDataset/SmallMetagenome/Csubt_wholegenome',
        'unknown',
        num_A = 837918,
        num_C = 505786,
        num_G = 504663 ,
        num_T = 841082)

    create_genome_file(
        luke_experiment,
        'data/OmicsData/LukeDataset/SmallMetagenome/Mthermo_wholegenome',
        'unknown',
        num_A=439339,
        num_C=433130 ,
        num_G=434571,
        num_T=444338)

    # create some image features
    create_image_file(
        luke_experiment,
        'data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_a',
        'tif',
        bin0=202303 ,
        bin50=104534,
        bin100=44775,
        bin150=23009,
        bin200=9871)

    create_image_file(
        luke_experiment,
        'data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_b',
        'tif',
        bin0=202303,
        bin50=104534,
        bin100=44775,
        bin150=23009,
        bin200=9871)


def view():
    print(Author.objects.all())
    print(Experiment.objects.all())
    print(File.objects.all())


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clean_db()
        create_data()
        view()


