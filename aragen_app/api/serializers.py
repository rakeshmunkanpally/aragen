from rest_framework import serializers
from aragen_app.models import operation_lookup
from rest_framework import serializers

 
       
 
        
        
        
class operationserializer(serializers.ModelSerializer):
    class Meta:
        model=operation_lookup
        fields='__all__'           
        
