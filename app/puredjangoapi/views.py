from app.models import *
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin
import json
"""Using a custom mixin to remove csrf validation"""
class UpdateModelDetailAPIView(CSRFExemptMixin,View):
    """Here we will retrieve, update, delete single object"""
    def get(self,request,*args,**kwargs):
        obj = Update.objects.get(id=kwargs['id'])
        json_data = obj.serialize1()
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        return HttpResponse({}, content_type='application/json')

    def put(self,request,*args,**kwargs):
        return HttpResponse({}, content_type='application/json')

    def delete(self,request,*args,**kwargs):
        return HttpResponse({}, content_type='application/json')

"""Using a custom mixin to remove csrf validation"""
class UpdateModelListView(CSRFExemptMixin, View):
    """Here we will play with whole model"""
    def get(self,request,*args,**kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize1()
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        data = json.dumps({
            "message":"Ho gaya save"
        })
        return HttpResponse(data, content_type='application/json')

    def delete(self,request,*args,**kwargs):
        data = json.dumps({
            "message":"Sorry you cannot delete"
        })
        return HttpResponse(data,content_type='application/json')