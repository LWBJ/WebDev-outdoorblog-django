from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import mixins

from dataapis.models import OutdoorDate
from django.contrib.auth.models import User
from dataapis.serializers import OutdoorDateSerializer, UserSerializer, UserSerializerWithToken

from rest_framework import permissions
from dataapis.permissions import IsOwnerOnly

from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers, viewsets

class OutdoorDateViewSet(viewsets.ModelViewSet):
  queryset = OutdoorDate.objects.all()
  serializer_class = OutdoorDateSerializer
  parser_classes = (MultiPartParser, FormParser)
  
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOnly]
  
  def get_queryset(self):
    try:
      user = self.request.user
      queryset = OutdoorDate.objects.filter(owner=user)
      #queryset = OutdoorDate.objects.all()
      params = self.request.query_params
        
      try:
        queryset = queryset.filter(title__icontains=params['title'])
      except:
        pass
        
      try:
        queryset = queryset.filter(place__icontains=params['place'])
      except:
        pass
        
      try:
        queryset = queryset.filter(date__icontains=params['date'])
      except:
        pass

      return queryset
      
    except:
      return []
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


@api_view(['GET'])
def currentUserDetail(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
  
class UserList(mixins.CreateModelMixin, generics.GenericAPIView):

  queryset = User.objects.all()
  serializer_class = UserSerializerWithToken

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

