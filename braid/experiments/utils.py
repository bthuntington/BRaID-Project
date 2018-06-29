from Bio import SeqIO
import magic


# model analysis controls
'''
def set_analysis_options(file_type):
    # TODO: Make dictionary to control what is assigned
    # mimetype_type will be key, analysis will be value
    type_list = 'no analysis'
    list_content = []
    if 'csv' in file_type.lower():
        list_content = ['Bayesian Network']
        type_list = 'csv'

    return list_content
'''
#Attempt at dictionary
#check to see if value is in dict and if it is then return value(list)


def set_analysis_options(file_type):
	analysis_dictionary = {'csv' : ("Bayesian Network"), 'txt' : (), 'fasta' : ("Frequented Regions")}
	if file_type in analysis_dictionary:
		return analysis_dictionary[file_type]
	else:
		return ('None. No Analysis Possible')
	

def is_plain_text(path):
    mimetype_type = 'unknown'

    # 'extension' : (MIMETYPE_TYPE, boolean to verify extension)
    is_type = {'.csv': ('csv', True), '.txt': ('txt', True),
               '.fasta': ('fasta', check_if_fasta(path))}

    # get file extension, assume follows last .
    if len(path.split('.')) > 1:
        extension = '.' + path.split('.')[-1].lower()

    # determine if it is a known extension
    if extension in is_type:
        if is_type[extension][1]:
            mimetype_type = is_type[extension][0]

    return mimetype_type


def check_if_fasta(text_file_path):
    # parse fasta file using Biopython and return false if
    # anything does not fit
    with open(text_file_path, 'rU') as handle:
        return any(SeqIO.parse(handle, "fasta"))


def get_mimetype_fields(path, file_model):
    # get file mimetype/mimetype type
    magic_mimetype = magic.from_file(path, mime=True)
    mimetype = magic_mimetype.split('/')[0].capitalize()
    # set as unknown and change otherwise
    final_mimetype = "Unknown"
    final_mimetype_type = "unknown"

    # check if mimetype matches a known mimetype
    if (mimetype, mimetype) in file_model.MIMETYPE:
        final_mimetype = mimetype

    mimetype_type = magic_mimetype.split('/')[1].lower()
    # check if type exists in list
    if (mimetype_type, mimetype_type) in file_model.MIMETYPE_TYPE:
        final_mimetype_type = mimetype_type
    elif 'text' in final_mimetype.lower():
        # check for other type text if necessary
        if 'plain' in mimetype_type:
            text_type = is_plain_text(path)
            if (text_type, text_type) in file_model.MIMETYPE_TYPE:
                final_mimetype_type = text_type
        elif 'jpeg' in mimetype_type:
            # catch images where jpeg not jpg
            final_mimetype_type = 'jpg'

    return final_mimetype, final_mimetype_type
