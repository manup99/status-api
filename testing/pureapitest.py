import requests
import json

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
    r=requests.get(BASE_URL+'pure_single'+str(num))
    data = r.json()
    print(r.status_code)
    return data

def create_update():
    dict = {
        'user': "1",
        'content':"Another update",
    }
    # dict = json.dumps(dict)
    print(json.dumps(dict))
    # data = json.dumps(dict)
    #print(data)
    r = requests.post(BASE_URL+'pure_list',data=dict)
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
def try_put():
    new_data = {
        "content":"change kren ki koshish",
        "you":"right"
    }
    # print(json.dumps(data))
    # data = json.dumps(data)
    # print(json.loads(data))
    # #print(json.loads(data))
    res = requests.put(BASE_URL+'pure_single/'+str(1),data=json.dumps(new_data))
    print(res.headers)
    print(res.status_code)

    return (res.json())
def create():
    data = {
        "user":"1",
        "content":"yes bro"
    }
    r = requests.post(BASE_URL+'pure_list',data=json.dumps(data))
    return r.json()
def delete1():
    res = requests.delete(BASE_URL+'pure_single/'+str(15))
    return res.json()
#print(get_list())
# print(f'\n\n\n\n')
# print(get_obj(2))
# print(f'\n\n\n\n')
#print(create_update())
#print(try_put())
# print(f'\n\n\n\n')
#print(try_delete())
# print(f'\n\n\n\n')
#print(try_put())
print(create())
#print(delete1())