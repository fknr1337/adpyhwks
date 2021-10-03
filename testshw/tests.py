from main import *
import pytest
import unittest
import builtins
import mock


class TestFunctions():

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_doc_existance(self):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert check_document_existance() == True

    def test_doc_not_existance(self):
        with mock.patch.object(builtins, 'input', lambda _: '11-3'):
            assert check_document_existance() == True

    def test_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert get_doc_owner_name() == 'Аристарх Павлов'

    def test_get_all_docs_valid(self):
        assert show_all_docs_info() == ['passport "2207 876234" "Василий Гупкин"',
                                        'invoice "11-2" "Геннадий Покемонов"',
                                        'insurance "10006" "Аристарх Павлов"']

    def test_get_all_docs_invalid(self):
        assert show_all_docs_info() == ['passport "2207 876234" "Василий Гупкин"',
                                        'invoice "11-2" "Геннадий Покемонов"',
                                        'insurance "10006" "Максим Шаталин"']

    def test_remove_from_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert remove_doc_from_shelf() == {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': [],
    '3': []
}

    def test_delete_doc(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert delete_doc() == [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
]

    def test_add_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '13'):
            assert add_new_shelf() == {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': [],
    '13': []
}


