from rest_framework.views import APIView
from aragen_app.models import operation_lookup
from .serializers import operationserializer
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from rest_framework import status
from rest_framework.decorators import api_view
# Define the User viewset
class operationViewSet(viewsets.ModelViewSet):
    queryset =operation_lookup.objects.all()
    serializer_class =operationserializer












        
        

 
 
        
        
        
      
        
        
        







