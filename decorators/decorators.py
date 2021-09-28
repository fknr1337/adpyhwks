import time
import datetime
import requests

#--first task--
def decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        time = str(datetime.datetime.now())
        with open('log.txt' , 'w') as f:

            f.writelines(f'{time}\n')
            f.writelines(f'Called function {function.__name__} with arguments: {args}, {kwargs}, returned '
                         f'result: {result}')
        return result
    return wrapper

@decorator
def test(x):
    x += 15
    return x

test(15)

#--second task--
def fabric_decorator(path):
    def second_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            time = str(datetime.datetime.now())
            with open(f'{path}' , 'w') as f:

                f.writelines(f'{time}\n')
                f.writelines(f'Called function {function.__name__} with arguments: {args}, {kwargs}, returned '
                             f'result: {result}')
            return result
        return wrapper
    return second_decorator

@fabric_decorator(path)
def test_1(x):
    x += 15
    return x

test_1(20)

#--third task--



@fabric_decorator(path)
def find_id_hero(name):
    token = 'token'
    url = (f'https://superheroapi.com/api/{token}/search/{name}')
    res = requests.get(url)
    a = res.json()
    for i in a['results']:
        if name in i.values():
            return(i['id'])
find_id_hero('Hulk')