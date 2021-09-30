def display_personal(dict_res):
    print("Personal informations: \n --------------------")
    for key, value in dict_res.items():
        print(key + ':', value)

def display_experience(dict_res):
    print("Professional experiences: \n --------------------")
    for exp_item in dict_res:
        print("Role: {} \n".format(exp_item["what"]))
        print("Company: {} \n".format(exp_item["where"]))
        print("Time working: {} \n".format(exp_item["date"]))
        print("Location: {} \n".format(exp_item["location"]))
        for item in exp_item["content"]:
            print("Achivements: {} \n".format(item))
        print("--"*10)

        
def display_education(dict_res):
    print("Professional experiences: \n --------------------")
    for exp_item in dict_res:
        print("Role: {} \n".format(exp_item["what"]))
        print("Institute: {} \n".format(exp_item["where"]))
        print("Time working: {} \n".format(exp_item["date"]))
        print("Location: {} \n".format(exp_item["location"]))
        for item in exp_item["content"]:
            print("Achivements: {} \n".format(item))
        print("--"*10)
        
def display_skills(dict_res):
    print("Skills: \n --------------------")
    for item in dict_res["content"]:
        print("Skill: {}".format(item))
        
def display_languages(dict_res):
    print("Languages: \n --------------------")
    for item in dict_res["content"]:
        print("Language: {}".format(item))


def display_parsed_cv(output_dict):
    display_personal(output_dict['personal'])
    display_experience(output_dict['experience'])
    display_education(output_dict['education'])
    display_skills(output_dict['knowledge'])
    display_languages(output_dict['languages'])
