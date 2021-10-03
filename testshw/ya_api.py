from ya_api_test import *

class TestYa:

    def test_creating_folder(self):
        assert create_folder('name') == 'Folder name created'

    def test_inv_token(self):
        assert create_folder('name') == 'Error code: 401'