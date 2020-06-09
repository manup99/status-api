from app.models import *
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin
import json
from app.forms import UpdateForm
from django.core.exceptions import ObjectDoesNotExist
from .utils import is_json
"""Using a custom mixin to remove csrf validation"""
class UpdateModelDetailAPIView(CSRFExemptMixin,View):
    """Here we will retrieve, update, delete single object"""
    def get(self,request,*args,**kwargs):
        try:
            obj = Update.objects.get(id=kwargs['id'])
        except ObjectDoesNotExist:
            error_data =json.dumps({"message":"Object not found"})
            return HttpResponse(error_data, content_type="application/json",status=404)
        json_data = obj.serialize1()
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        return HttpResponse({}, content_type='application/json')

    def put(self,request,*args,**kwargs):
        print(json.loads(request.body))
        try:
            obj = Update.objects.get(id=kwargs['id'])
            data = obj.serialize1()
            valid_json = is_json(request.body)
            if not valid_json:
                data = json.dumps({"message":"not in json format"})
                return HttpResponse(data,content_type="application/json")
            return HttpResponse(data, content_type='application/json')
        except:
            json_data = json.dumps({
                "sorry":"no object exists"
            })
            return HttpResponse(json_data, content_type='application/json',status=404)
    def delete(self,request,*args,**kwargs):
        try:
            obj = Update.objects.get(id=kwargs['id'])
            obj.delete()
            data = json.dumps({
                "message": "deleted successfully"
            })
            return HttpResponse(data,content_type="application/json", status=200)
        except Update.DoesNotExist:
            data = json.dumps({
                "message":"Object with this id does not exts"
            })
            return HttpResponse(data,content_type='application/json', status=200)


"""Using a custom mixin to remove csrf validation"""
class UpdateModelListView(CSRFExemptMixin, View):
    """Here we will play with whole model"""
    def get(self,request,*args,**kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize1()
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        #print(json.loads(request.body))
        form = UpdateForm(json.loads(request.body))
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize1()
            return HttpResponse(obj_data,content_type="application/json",status=200)
        json_data = json.dumps({
            "message":"sorry bro"
        })
        return HttpResponse(json_data, content_type='application/json', status=200)
    def delete(self,request,*args,**kwargs):
        try:
            obj = Update.objects.get(id=kwargs['id'])
            obj.delete()
            data = json.dumps({
                "message": "deleted successfully"
            })
            return HttpResponse(data,content_type="application/json", status=200)
        except ObjectDoesNotExist:
            data = json.dumps({
                "message":"Object with this id does not exts"
            })
            return HttpResponse(data,content_type='application/json', status=200)