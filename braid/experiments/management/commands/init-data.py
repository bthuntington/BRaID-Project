from django.core.management.base import BaseCommand

from experiments.models import Author, Experiments, Files, ImageFeatures, TextFeatures

def clean_db():
    Author.objects.all().delete()
    Experiments.objects.all().delete()
    Files.objects.all().delete()
    ImageFeatures.objects.all().delete()
    TextFeatures.objects.all().delete()

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
    return Experiments.objects.create(experiment_name=name, author_ID=author)


def create_file(experiment, path, mimetype_type):
    return Files.objects.create(
        experiment_ID=experiment,
        path=path,
        mimetype=MIME_TYPES[mimetype_type],
        mimetype_type=mimetype_type)


def init_experiment(author_name, experiment_name, data):
    author = create_author(author_name)
    experiment = create_experiment(experiment_name, author)
    for entry in data:
        f = create_file(experiment, entry[0], entry[1])
        # TODO: can I do feature extraction here? create_features(...)

def create_data():
    #author_names = ['Pettygrove', 'Luke']
    #(pettygrove, luke) = create_authors(author_names)

    #pettygrovedataset = create_experiment('PettygroveDataSet', pettygrove)
    #lukedataset = create_experiment('LukeDataSet', luke)

    # set camilleri data
    # TODO: decide if this is a good abstraction
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

    init_experiment(
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
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_a','tif'),
            ('data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_b','tif'),
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



"""     c_subt = create_file(
        lukedataset,
        'data/OmicsData/LukeDataset/SmallMetagenome/Csubt_wholegenome',
        'unknown')
    m_thermo = create_file(
        lukedataset,
        'data/OmicsData/LukeDataset/SmallMetagenome/Mthermo_wholegenome',
        'unknown')



    TextFeatures.objects.create(
        number_of_A = 837918,
        number_of_C = 505786,
        number_of_G = 504663 ,
        number_of_T = 841082,
        text_file_ID=c_subt)

    TextFeatures.objects.create(
        number_of_A=439339,
        number_of_C=433130 ,
        number_of_G=434571,
        number_of_T=444338,
        text_file_ID=m_thermo) """

def view():
    print(Author.objects.all())
    print(Experiments.objects.all())
    print(Files.objects.all())


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clean_db()
        create_data()
        view()


 ###########################################################

#
# #done on LukeDataSet smallmetagenome
# #####################################################################
# fileA = Files.objects.get(pk = 9)
# fileB = Files.objects.get(pk = 10)
# fileC = Files.objects.get(pk = 11)
# fileD = Files.objects.get(pk = 12)
# file2 = imageFeatures(uptoFifty = 202303 , fiftyToHundred = 104534, hundredToOneFifty = 44775 , oneFiftyToTwoHundred=23009, twoHundredToTwoFiftyFive = 9871, imageFileID = fileA)
# file2.save()
# file3 = imageFeatures(uptoFifty = 257836, fiftyToHundred =  54207, hundredToOneFifty =  27406 , oneFiftyToTwoHundred = 17229, twoHundredToTwoFiftyFive =  10867, imageFileID = fileB)
# file3.save()
# file4 = imageFeatures(uptoFifty = 121029 , fiftyToHundred = 199729, hundredToOneFifty =  58192, oneFiftyToTwoHundred =  5234, twoHundredToTwoFiftyFive= 308, imageFileID = fileC)
# file4.save()
# file5 = imageFeatures(uptoFifty = 177237, fiftyToHundred = 95153 , hundredToOneFifty = 65569 , oneFiftyToTwoHundred = 27916, twoHundredToTwoFiftyFive =  3044, imageFileID = fileD)
# file5.save()
# #done on FrancoDataSet
