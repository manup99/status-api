from django.shortcuts import render
from .serializers import StatusSerializer
from .models import Status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
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
