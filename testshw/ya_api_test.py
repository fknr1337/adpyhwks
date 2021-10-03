import requests



def create_folder(folder_name):
    token = 'token'
    params = {'path': folder_name}
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
    r = requests.put(url, headers=headers, params=params)
    if r.status_code != 201:
        return f'Error code: {r.status_code}'
    else:
        return f'Folder {folder_name} created'

