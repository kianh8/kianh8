def write_personal(dict_res, f):
    f.write("Personal informations: \n -------------------- \n")
    for key, value in dict_res.items():
        f.write(key + ':', value)
    f.write("--" * 10 + "\n")


def write_experience(dict_res, f):
    f.write("Professional experiences: \n --------------------\n")
    for exp_item in dict_res:
        f.write("Role: {} \n".format(exp_item["what"]))
        f.write("Company: {} \n".format(exp_item["where"]))
        f.write("Time working: {} \n".format(exp_item["date"]))
        f.write("Location: {} \n".format(exp_item["location"]))
        for item in exp_item["content"]:
            f.write("Achivements: {} \n".format(item))
        f.write("--" * 10 + "\n")


def write_education(dict_res, f):
    f.write("Professional experiences: \n --------------------\n")
    for exp_item in dict_res:
        f.write("Role: {} \n".format(exp_item["what"]))
        f.write("Institute: {} \n".format(exp_item["where"]))
        f.write("Time working: {} \n".format(exp_item["date"]))
        f.write("Location: {} \n".format(exp_item["location"]))
        for item in exp_item["content"]:
            f.write("Achivements: {} \n".format(item))
        f.write("--" * 10 + "\n")


def write_skills(dict_res, f):
    f.write("Skills: \n --------------------\n")
    for item in dict_res["content"]:
        f.write("Skill: {}".format(item))
    f.write("--" * 10 + "\n")


def write_languages(dict_res, f):
    f.write("Languages: \n --------------------\n")
    for item in dict_res["content"]:
        f.write("Language: {}".format(item))
    f.write("--" * 10 + "\n")


def write_parsed_cv(output_dict):
    with open('output.txt', 'w') as f:
        write_personal(output_dict['personal'], f)
        write_experience(output_dict['experience'], f)
        write_education(output_dict['education'], f)
        write_skills(output_dict['knowledge'], f)
        write_languages(output_dict['languages'], f)
