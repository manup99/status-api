import  requests
import  json
ENDPOINT='http://127.0.0.1:8000/restapi/single_crudl'

def do(method='get',data={},id=15):
    headers={}
    headers['content-type']='application/json'
    data=json.dumps(data)
    r=requests.request(method,ENDPOINT+'?id='+str(id),data=data,headers=headers)
    print(r.text)
    return r


do(method='post',data={'content':'My name is Lakhan','user':1})