import  requests
import  json
ENDPOINT='http://127.0.0.1:8000/restapi/single_crudl'

def do(method='get',data={},id=15):
    headers={}
    headers['content-type']='application/json'
    r=requests.request(method,ENDPOINT+'?id='+str(id),data=data,headers=headers)
    print(r.text)
    return r


do(data={'id':12})