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
    'xlsx': 'Text',
    'unknown': 'Unknown', # TODO: we defined... is this correct?
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
    author_names = ['Franco', 'Pettygrove', 'Luke']
    (franco, pettygrove, luke) = create_authors(author_names)

    francodataset = create_experiment('FrancoDataSet', franco)
    pettygrovedataset = create_experiment('PettygroveDataSet', pettygrove)
    lukedataset = create_experiment('LukeDataSet', luke)




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


    file = Files.objects.create(experiment_ID = francodataset, path = "data/ImageData/FrancoDataSet/EAL-10230x", mimetype = 'Image', mimetype_type = 'png')
    file = Files.objects.create(experiment_ID = francodataset, path = "data/ImageData/FrancoDataSet/EAL-23000x", mimetype = 'Image', mimetype_type = 'png')
    file = Files.objects.create(experiment_ID = francodataset, path = "data/ImageData/FrancoDataSet/EDL-1430x", mimetype = 'Image', mimetype_type = 'png')
    file = Files.objects.create(experiment_ID = francodataset, path = "data/ImageData/FrancoDataSet/EDL-17700x", mimetype = 'Image', mimetype_type = 'png')

    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/CFU Counts 11-16", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Experiment", mimetype = 'Text', mimetype_type = 'lif')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Growth Data 11-16 v2", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Growth Data 11-16", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Patrol Data 11-16", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 1", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 2", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 3", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 4", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 5", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 5", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 6", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 6", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 7", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 7", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 8 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Pos 8", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-16-2017/Speed Data 11-16-2017", mimetype = 'Text', mimetype_type = 'xlsx')
    ######################################################
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/CFU Counts 11-28", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Experiment", mimetype = 'Text', mimetype_type = 'lif')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Growth Data 11-28", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Patrol Data 11-28", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 1", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 2", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 3", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 4", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 5", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 5 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 5", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 6", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 6 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 6", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 7", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 7", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 7 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 8 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 8", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 8", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Speed Data 11-28-2017", mimetype = 'Text', mimetype_type = 'xlsx')
    #################################################################
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/CFU Counts 12-5", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Experiment", mimetype = 'Text', mimetype_type = 'lif')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Growth Data 12-5-2017", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Patrol Data 12-5-2017", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 1", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 2", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 3", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 4", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 5", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 5 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 5 Green", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 6", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 6 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 6 Green", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 7", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 7 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 7 Green", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 8", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 8 Gray", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/12-5-2017/Pos 8 Green", mimetype = 'Video', mimetype_type = 'avi')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 5", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 6", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 7", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Pos 8", mimetype = 'Text', mimetype_type = 'xls')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Speed Data 12-5-2017", mimetype = 'Text', mimetype_type = 'xlsx')
    file = Files.objects.create(experiment_ID = pettygrovedataset, path = "data/ImageData/PettygroveDataSet/11-28-2017/Tile Data 12-5-2017", mimetype = 'Text', mimetype_type = 'xlsx')

    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R1", mimetype = 'Text', mimetype_type = 'fastq')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R2", mimetype = 'Text', mimetype_type = 'fastq')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/PKF9-QUALITY_PASSED_R2.fastq", mimetype = 'unknown', mimetype_type = 'zip')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/PKF9-READ_IDs.cPickle", mimetype = 'Text', mimetype_type = 'z')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/PKF9-STATS", mimetype = 'Text', mimetype_type = 'txt')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/LargeMetagenome/ziSWHTdA", mimetype = 'unknown', mimetype_type = 'unknown')
    ###########################################
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_a", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_b", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_c", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_d", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_e", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_f", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_g", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_h", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_i", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_j", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_k", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_l", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_m", mimetype = 'Image', mimetype_type = 'tif')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SEMImages/LM_Culture_2_2017_n", mimetype = 'Image', mimetype_type = 'tif')
    ################################################
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R1_001", mimetype = 'Text', mimetype_type = 'fastq')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R2_001", mimetype = 'Text', mimetype_type = 'fastq')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R1_001.fastq", mimetype = 'unknown', mimetype_type = 'gz')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/13_S1_L001_R2_001.fastq", mimetype = 'unknown', mimetype_type = 'gz')

    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/R1_pe", mimetype = 'unknown', mimetype_type = 'unknown')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/R1_se", mimetype = 'unknown', mimetype_type = 'unknown')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/R2_pe", mimetype = 'unknown', mimetype_type = 'unknown')
    file = Files.objects.create(experiment_ID = lukedataset, path = "data/OmicsData/LukeDataset/SmallMetagenome/R1_se", mimetype = 'unknown', mimetype_type = 'unknown')



    c_subt = create_file(
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
        text_file_ID=m_thermo)

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
