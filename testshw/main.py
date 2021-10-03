import pytest
import unittest
import builtins
import mock
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def check_document_existance():
    user_doc_number = input('Введите номер документв: ')
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_doc_owner_name():
    user_doc_number = input('Введите номер документа - ')
    print()
    doc_exist = check_document_existance()
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                return current_document['name']


def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)


def remove_doc_from_shelf():
    doc_number = input('Номер документа для удаления с полки: ')
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break
    return directories


def add_new_shelf(shelf_number=''):
    if not shelf_number:
        shelf_number = input('Введите номер полки - ')
    if shelf_number not in directories.keys():
        directories[shelf_number] = []

    return directories


def append_doc_to_shelf():
    doc_number = input('Номер документа: ')
    shelf_number = input('Номер полки: ')
    add_new_shelf(shelf_number)
    directories[shelf_number].append(doc_number)
    return directories


def delete_doc():
    user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance()
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf()
        return documents


def get_doc_shelf():
    user_doc_number = input('Введите номер документа - ')
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number


def move_doc_to_shelf():
    user_doc_number = input('Введите номер документа - ')
    user_shelf_number = input('Введите номер полки для перемещения - ')
    remove_doc_from_shelf(user_doc_number)
    append_doc_to_shelf(user_doc_number, user_shelf_number)
    print('Документ номер "{}" был перемещен на полку номер "{}"'.format(user_doc_number, user_shelf_number))


def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    return ('{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name))


def show_all_docs_info():
    print('Список всех документов:\n')
    docs = []
    for current_document in documents:
         docs.append(show_document_info(current_document))

    return docs



def add_new_doc():
    new_doc_number = input('Введите номер документа - ')
    new_doc_type = input('Введите тип документа - ')
    new_doc_owner_name = input('Введите имя владельца документа- ')
    new_doc_shelf_number = input('Введите номер полки для хранения - ')
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    documents.append(new_doc)
    append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
    return new_doc_shelf_number



