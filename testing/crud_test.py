import  requests
import  json
ENDPOINT='http://127.0.0.1:8000/restapi/single_crudl'
ENDPOINT1='http://127.0.0.1:8000/restapi/double_crudl2'

def do(method='get',data={},id=15):
    headers={}
    headers['content-type']='application/json'
    data=json.dumps(data)
    r=requests.request(method,ENDPOINT+'?id='+str(id),data=data,headers=headers)
    print(r.text)
    return r


#do(method='post',data={'content':'My name is Lakhan','user':1})


def create():
    data={
        "content":"SDOSUD",
        "user":1
    }
    headers={
        "Content-type":'application/json',
        "Authorization":'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkzNjAyNzI4LCJqdGkiOiIxM2JlOTdlODdhOGI0MTllODhkOWRlNzJmYjM4MzEwNyIsInVzZXJfaWQiOjF9._kIr1O-3ViWqtePblRsEVpenIFoXgiVnNV1-0nMFmTE'
    }
    res=requests.post(ENDPOINT1,data=json.dumps(data),headers=headers)
    print(res.json())
    return res.json()

create()