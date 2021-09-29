import pandas as pd
import numpy as np
import os


def remove_all_occurrences(list_obj, value):
    clean_list = list()
    for item in list_obj:
        if item == value:
            pass
        else:
            clean_list.append(item)
    return clean_list


def get_format_res(path):
    resume = open(path, 'r', encoding='utf-8').read()
    list_resume = resume.split("\n")
    list_resume = remove_all_occurrences(list_resume, "")
    good_resume = list()
    for item in list_resume:
        item_list = item.split("\t")
        good_resume.append([item_list[1], item_list[0], item_list[2]])
    return good_resume


def get_category_data(good_list, category):
    list_result = list()
    for item in good_list:
        if item[0] == category:
            list_result.append(item)
    return list_result


def fill_e_template(liste):
    e_item = {'what': np.nan,
              'where': np.nan,
              'date': np.nan,
              'location': np.nan,
              'content': list()}

    items_to_delete = list()

    for i in range(len(liste)):
        if liste[i][1] == 'content':
            j = i
            while liste[j][1] == 'content':
                e_item["content"].append(liste[j][2])
                items_to_delete.append(liste[j])
                j += 1
                if j >= len(liste):
                    break
            break

    for i in range(len(liste)):
        if liste[i][1] == "where":
            e_item["where"] = liste[i][2]
            items_to_delete.append(liste[i])
            break

    for i in range(len(liste)):
        if liste[i][1] == "what":
            e_item["what"] = liste[i][2]
            items_to_delete.append(liste[i])
            break

    for i in range(len(liste)):
        if liste[i][1] == "date":
            e_item["date"] = liste[i][2]
            items_to_delete.append(liste[i])
            break

    for i in range(len(liste)):
        if liste[i][1] == "location":
            e_item["location"] = liste[i][2]
            items_to_delete.append(liste[i])
            break

    for item in items_to_delete:
        liste.remove(item)

    return e_item, liste


def e_processing(list_e):
    e_items = []
    while len(list_e) > 2:
        e_item, list_education = fill_e_template(list_e)
        e_items.append(e_item)
    return e_items


def fill_ls_template(liste):
    ls_item = {'content': list()}
    items_to_delete = list()

    for i in range(len(liste)):
        if liste[i][1] == 'header':
            items_to_delete.append(liste[i])

        if liste[i][1] == 'content':
            ls_item["content"].append(liste[i][2])
            items_to_delete.append(liste[i])

    for item in items_to_delete:
        liste.remove(item)

    return ls_item


def fill_personal_template(resume_personal):
    personal_item = {'name': np.nan,
                     'mail': np.nan,
                     'address': np.nan,
                     'number': np.nan}

    for i in range(len(resume_personal)):
        if resume_personal[i][1] == 'who':
            personal_item['name'] = resume_personal[i][2]

    for i in range(len(resume_personal)):
        if resume_personal[i][1] == 'name':
            personal_item['name'] = resume_personal[i][2]

    for i in range(len(resume_personal)):
        if resume_personal[i][1] == 'location':
            personal_item['address'] = resume_personal[i][2]

    for i in range(len(resume_personal)):
        if resume_personal[i][1] == 'mail':
            personal_item['mail'] = resume_personal[i][2]

    for i in range(len(resume_personal)):
        if resume_personal[i][1] == 'number':
            personal_item['number'] = resume_personal[i][2]

    return personal_item


def remove_headers(item_list):
    item_to_delete = list()
    for i in range(len(item_list)):
        if item_list[i][1] == 'header':
            item_to_delete.append(item_list[i])
    for item in item_to_delete:
        item_list.remove(item)
    return item_list
