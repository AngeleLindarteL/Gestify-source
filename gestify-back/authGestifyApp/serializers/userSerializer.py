from rest_framework import serializers
from authGestifyApp.models.user import User
from authGestifyApp.models.producto import Producto
from authGestifyApp.serializers.productoSerializer import ProductoSerializer

class UserSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'producto']
        
def create(self, validated_data):
    productData = validated_data.pop('producto')
    userInstance = User.objects.create(**validated_data)
    Producto.objects.create(user=userInstance, **productData)
    return userInstance

def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    producto = Producto.objects.get(user=obj.id)
    return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'producto': {
                    'code': producto.code,
                    'prov_name': producto.prov_name,
                    'p_name': producto.p_name,
                    'quantity': producto.quantity,
                    'movement': producto.movement,
                    'price': producto.price,
                    'category': producto.category,
                    'description': producto.description
                    }
                }