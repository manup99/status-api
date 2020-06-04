from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from .models import Update
import json
from .mixins import JsonResponseMixin
from django.core.serializers import serialize
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
    """class for checking our custom mixin"""
    def get(self,reuqest,*args,**kwargs):
        data = {
            "count":100,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)
class Serialized_UpdateClass_View(JsonResponseMixin, View):
    """Converting a model object into JSON withour using mixin"""
    def get(self,request):
        obj = Update.objects.get(id=1)
        data = {
            "user":obj.user.id,
            "content":obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    """Serializing whole model in JSON using serialize method provided by django"""
    def get(self,request):
        qs = Update.objects.all()
        """we can also add fields here in serializer after qs"""
        """data = serialize("json",qs,fields=(' ',' ')"""
        data = serialize("json", qs)
        print(data)
        return HttpResponse(data,content_type='application/json')


class Serialize_single_Object(View):
    def get(self,request):
        obj=Update.objects.get(id=1)
        """when serializing single object you need to use list"""
        data = serialize("json",[obj,])
        print(data)
        return HttpResponse(data,content_type='application/json')


class SerializeList_using_update_manager(View):
    """Here we are serializing whole model using update manager"""
    def get(self,request):
        data = Update.objects.all().serialize()
        return HttpResponse(data,content_type='application/json')

class SerializeSingleObject_using_update_manager(View):
    """Here we are serializing a single object using the update manager"""
    def get(self,request):
        obj=Update.objects.get(id=1)
        data = obj.serialize()
        return HttpResponse(data,content_type='application/json')


class Serialize_Only_UsefulData_Using_Update_Manager(View):
    def get(self,request):
        obj=Update.objects.get(id=1)
        data = obj.serialize1()
        return HttpResponse(data, content_type='application/json')

class SerializeList_Only_UsefulData_Using_Update_Manager(View):
    def get(self,request):
        data=Update.objects.all().serialize1()
        return HttpResponse(data, content_type='application/json')