import pandas as pd


def csv_personal(dict_res):
    dict_personal = {'keys': list(), 'values': list()}
    for key, value in dict_res.items():
        dict_personal['keys'].append(key)
        dict_personal['values'].append(value)
    return pd.DataFrame(dict_personal)


def csv_experience(dict_res):
    cmpt_id = 0
    dict_experience = {'keys': list(), 'values': list()}
    indexes = []
    for exp_item in dict_res:
        dict_experience['keys'].append("Role")
        dict_experience['values'].append(exp_item["what"])
        indexes.append((cmpt_id, 0))

        dict_experience['keys'].append("Company")
        dict_experience['values'].append(exp_item["where"])
        indexes.append((cmpt_id, 1))

        dict_experience['keys'].append("Time working")
        dict_experience['values'].append(exp_item["date"])
        indexes.append((cmpt_id, 2))

        dict_experience['keys'].append("Location")
        dict_experience['values'].append(exp_item["location"])
        indexes.append((cmpt_id, 3))

        cmpt_temp = 4
        for item in exp_item["content"]:
            dict_experience['keys'].append("Achivement")
            dict_experience['values'].append(item[1:])
            indexes.append((cmpt_id, cmpt_temp))
            cmpt_temp += 1
        cmpt_id += 1

    index = pd.MultiIndex.from_tuples(indexes, names=["first", "second"])

    return pd.DataFrame(dict_experience, index=index)


def csv_education(dict_res):
    cmpt_id = 0
    dict_education = {'keys': list(), 'values': list()}
    indexes = []
    for exp_item in dict_res:
        dict_education['keys'].append("Role")
        dict_education['values'].append(exp_item["what"])
        indexes.append((cmpt_id, 0))

        dict_education['keys'].append("Institute")
        dict_education['values'].append(exp_item["where"])
        indexes.append((cmpt_id, 1))

        dict_education['keys'].append("Time studing")
        dict_education['values'].append(exp_item["date"])
        indexes.append((cmpt_id, 2))

        dict_education['keys'].append("Location")
        dict_education['values'].append(exp_item["location"])
        indexes.append((cmpt_id, 3))

        cmpt_temp = 4
        for item in exp_item["content"]:
            dict_education['keys'].append("Achivement")
            dict_education['values'].append(item[1:])
            indexes.append((cmpt_id, cmpt_temp))
            cmpt_temp += 1
        cmpt_id += 1

    index = pd.MultiIndex.from_tuples(indexes, names=["first", "second"])

    return pd.DataFrame(dict_education, index=index)


def csv_skills(dict_res):
    dict_skills = {'keys': list(), 'values': list()}
    for key, value in dict_res.items():
        for val in value:
            dict_skills['keys'].append(key)
            dict_skills['values'].append(val)
    return pd.DataFrame(dict_skills)


def csv_languages(dict_res):
    print(dict_res.items())
    dict_languages = {'keys': list(), 'values': list()}
    for key, value in dict_res.items():
        for val in value:
            dict_languages['keys'].append(key)
            dict_languages['values'].append(val)
    return pd.DataFrame(dict_languages)


def csv_parsed_cv(output_dict):
    csv_per = csv_personal(output_dict['personal'])
    csv_exp = csv_experience(output_dict['experience'])
    csv_edu = csv_education(output_dict['education'])
    csv_sk = csv_skills(output_dict['knowledge'])
    csv_lang = csv_languages(output_dict['languages'])
    return [csv_per, csv_exp, csv_edu, csv_sk, csv_lang]