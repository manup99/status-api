from django.shortcuts import render
from .serializers import StatusSerializer
from .models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins
from django.shortcuts import get_object_or_404
import  json
"""Here we are Response and APIView to retrieve list and """
class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self,request,*args,**kwargs):
        qs = Status.objects.all()
        data = StatusSerializer(qs, many=True)
        return Response(data.data)

class StatusListSearchGeneric(generics.ListAPIView):
    """Here we are using generic ListAPIView for listing all objects"""
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def get_queryset(self):
        qs = Status.objects.all()
        q = self.request.GET.get('q')
        if q is not None:
            qs = qs.filter(content__icontains=q)
        return qs


class StatusCreateGeneric(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()


    def perform_create(self,serializer):
        if serializer.is_valid():
            print(serializer.validated_data)
        serializer.save()

class StatusRetrieveSerializer(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()
    lookup_field='id'


    def get_object(self):
        return Status.objects.get(id=self.kwargs['id'])

class StatusUpdateGeneric(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()
    lookup_field='id'


class StatusDeleteGeneric(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()
    lookup_field='id'


class StatusDeleteRetriveUpdateGeneric(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()
    lookup_field='id'


class StatusCreateListMixin(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()

    def get_queryset(self):
        qs=Status.objects.all()
        q=self.request.GET.get('q')
        if q is not None:
            qs=qs.filter(content__icontains=q)
        return qs
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class StatusCRUDL(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset= Status.objects.all()

    def get_queryset(self):
        qs=Status.objects.all()
        q=self.request.GET.get('q')
        if q is not None:
            qs=qs.filter(content__icontains=q)
        return qs


    def get_object(self):

        qs=self.get_queryset()
        data = self.request.GET.get('id',None)
        obj=None
        if data is not None:
            obj = get_object_or_404(qs,id=data)
            self.check_object_permissions(self.request,obj)
        return obj
    def post(self,request,*args,**kwargs):
        print(request.body)
        print(request.data)
        return self.create(request,*args,**kwargs)

    def perform_destroy(self,instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self,request,*args,**kwargs):
        data=json.loads(request.body)
        print(request.body)
        print(request.data)
        passed_id = request.GET.get('id')
        if passed_id is None:
            return super().get(request,*args,**kwargs)
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)