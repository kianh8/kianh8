import resume_parser
from utils_config import load_params
import pprint


def main_resume(path):
    # get the right data structure
    list_resume = resume_parser.get_format_res(path)
    # remove all headers
    list_resume = resume_parser.remove_headers(list_resume)

    # remove what follows when done with it
    print(item_compliance(list_resume))

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
#print(output_dict)
pprint.pprint(output_dict, sort_dicts=False)
