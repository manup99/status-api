import requests


BASE_URL = "http://127.0.0.1:8000/"

def get_list():
    r = requests.get(BASE_URL+'pure_list')
    """.json method converts json data into list"""
    data = r.json()
    for obj in data:
        print(obj['content'])
    print(r.status_code)
    return r.json()

def get_obj(num):
    r=requests.get(BASE_URL+'pure_single/'+str(num))
    data = r.json()
    print(r.status_code)
    return data

def create_update():
    dict = {
        'user': 1,
        'content':"Another update"
    }
    r = requests.post(BASE_URL+'pure_list', data=dict)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
def try_delete():
    data = {
        "user": 1,
        'content':'sjdiu'
    }
    r = requests.delete(BASE_URL+'pure_list',data=data)
    data = r.json()
    print(r.status_code)
    return data
print(get_list())
print(f'\n\n\n\n')
print(get_obj(2))
print(f'\n\n\n\n')
print(create_update())
print(f'\n\n\n\n')
print(try_delete())