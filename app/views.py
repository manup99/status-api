from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Update
import json
from .mixins import JsonResponseMixin
class json_example_view(View):
    """Just a sample view for checking JSONresponse"""
    data={
        "count":1000,
        "content":"Some new content"
    }
    """Instead of using Json response earlier we used to do it with help of json dumps"""
    """json_data = json.dumps(data)
       return Httpreponse(json_data,content_type='application/json') 
    """
    def get(self,request):
        return JsonResponse(self.data)


class Json_example_using_mixin(JsonResponseMixin, View):
    def get(self,reuqest,*args,**kwargs):
        data = {
            "count":100,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)
