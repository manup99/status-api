from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions,mixins
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

class HelloView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request):
        content={
            "message":"hello User"
        }
        data=json.dumps(content)
        return HttpResponse(data,content_type='application/json')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class AuthView(APIView):
    permission_classes=()
    authentication_classes=()
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return Response({"message":"You are already loggedin"})
        # print(request.body)
        # print(request.data)
        # print(request.POST)
        user=authenticate(username=request.data['username'],password=request.data['password'])
        qs = get_user_model().objects.filter(
            Q(username__iexact=request.data['username'])|
            Q(password__iexact=request.data['password'])
        )
        if qs.count()==1:
            obj=qs.first()
            if obj.check_password(request.data['password']):

                obj=get_tokens_for_user(qs.first())
                print(obj['refresh'])
                print(obj['access'])
                return Response({'refresh':obj['refresh'],
                                 'access':obj['access'],
                                 'user':user.username})
            else:
                return Response({"Error":'Wrong Password'})
        else:
            return Response({"ERROR":"No user with given credetials"})


class RegisterAuth(APIView):
    permission_classes=()
    def post(self,request):
        if request.user.is_authenticated:
            return Response({"detail":"user is already logged in"})
        data = request.data
        username=data['username']
        email=data['email']
        password1=data['password1']
        password2=data['password2']
        qs=get_user_model().objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=email)
        )
        if qs.count()>=1:
            return Response({'error':"User with this credential already exists"})
        elif password1 != password2:
            return Response({'error':'Password does not match'})
        else:
            user=get_user_model().objects.create(username=username,email=email,password=password1)
            user.set_password(password1)
            user.save()
            obj = get_tokens_for_user(user)
            print(obj['refresh'])
            print(obj['access'])
            return Response({'refresh': obj['refresh'],
                             'access': obj['access'],
                             'user': user.username})
