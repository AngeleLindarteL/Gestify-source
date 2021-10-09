from authGestifyApp.models.producto import Producto
from rest_framework import serializers

from authGestifyApp.models.proveedor import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor 
        fields = ['p_name', 'p_telephone', 'p_email']
        
         