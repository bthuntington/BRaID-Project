# model analysis controls
def set_analysis_options(file_type):
    type_list = 'no analysis'
    list_content = []
    if 'csv' in file_type.lower():
        list_content = ['Bayesian Network']
        type_list = 'csv'

    return list_content, type_list
