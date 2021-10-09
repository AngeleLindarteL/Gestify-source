from django.db import models

class Proveedor(models.Model):
    
    p_name = models.CharField('Suplier', max_length=30, primary_key=True)
    p_telephone = models.CharField('Telephone', max_length = 10)
    p_email = models.CharField('Email', max_length = 100)
    
    
    
    
    
    
