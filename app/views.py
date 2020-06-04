from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Update
class update_model_detail_view(View):
    """Just a sample view for checking JSONresponse"""
    data={
        "count":1000,
        "content":"Some new content"
    }
    def get(self,request):
        return JsonResponse(self.data)
