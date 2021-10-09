from authGestifyApp.models.producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto 
        fields = ['code', 'prov_name', 'p_name', 'quantity','movement','price','category','description']
        
        
    