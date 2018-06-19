# model analysis controls
def set_analysis_options(file_type):
    type_list = []
    if 'csv' in file_type.lower():
        type_list = ['Bayesian Network']

    return type_list
