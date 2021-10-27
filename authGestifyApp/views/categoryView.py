from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

class CategoryView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        categories = {
            1: ('Beb', 'Bebidas'),
            2:('Mas', 'Para_Mascotas'),
            3: ('Beb', 'Para_Bebés'),
            4: ('AP',  'Aseo_Personal'),
            5: ('Lim', 'Limpieza'),
        }
        
        return Response(categories,status=status.HTTP_200_OK)