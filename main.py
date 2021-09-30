# !pip3 install pandas
# !pip3 install pprintpp
# !pip install numpy
# !pip install os
# !pip install argparse
# !pip install ast

import resume_parser
from parser_display import display_parsed_cv
from utils_config import load_params
import pandas as pd
import numpy as np
import pprint


def main_resume(path):
    #path = path_pdf.split(".")[0] + ".pdf"
    # get the right data structure
    list_resume = resume_parser.get_format_res(path)
    # remove all headers
    list_resume = resume_parser.remove_headers(list_resume)

    # remove what follows when done with it
    #print(item_compliance(list_resume))

    # get categories data
    resume_personal = resume_parser.get_category_data(list_resume, "personal")
    resume_education = resume_parser.get_category_data(list_resume, "education")
    resume_experience = resume_parser.get_category_data(list_resume, "experience")
    resume_knowledge = resume_parser.get_category_data(list_resume, "knowledge")
    resume_languages = resume_parser.get_category_data(list_resume, "languages")
    # resume_others = resume_parser.get_category_data(list_resume, "others")
    # get format data for education and experience
    dict_education = resume_parser.e_processing(resume_education)
    dict_experience = resume_parser.e_processing(resume_experience)
    # get format data for languages and knowledge
    dict_languages = resume_parser.fill_ls_template(resume_languages)
    dict_knowledge = resume_parser.fill_ls_template(resume_knowledge)
    # get format data for personal
    dict_personal = resume_parser.fill_personal_template(resume_personal)
    return {"personal": dict_personal,
            "education": dict_education,
            "experience": dict_experience,
            "languages": dict_languages,
            "knowledge": dict_knowledge}


def item_compliance(item_list):
    that_is_not_good = list()
    for item in item_list:
        if len(item) != 3:
            that_is_not_good.append(item)
    return that_is_not_good


params = load_params("./config.yml")
output_dict = main_resume(params["input_file"])
# print(output_dict)
# pprint.pprint(output_dict, sort_dicts=False)


df_dict = pd.DataFrame({ key:pd.Series(value) for key, value in output_dict.items() })
df_dict = df_dict.replace(np.nan, '', regex=True)
#df_dict


display_parsed_cv(output_dict)


# the code below was intended to print the dictionary using html

# dict_table = []
# for (key, value) in zip(output_dict.keys(), output_dict.values()):
#     temp = []
#     temp.extend([key,value])  #Note that this will change depending on the structure of your dictionary
#     dict_table.append(temp)