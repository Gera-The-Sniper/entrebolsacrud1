from django.db import models

class Cliente(models.Model):
    name_client=models.CharField(max_length=250,primary_key=True,verbose_name="Nombre") 

    def __str__(self):
        return self.name_client 

class Minimarket(models.Model):
    name_mini=models.CharField(max_length=250,primary_key=True,verbose_name="Nombre")
    phone_mini=models.CharField(max_length=15,verbose_name="Telefono")
    rubro=models.CharField(max_length=50)
    address=models.CharField(max_length=100,verbose_name="Direccion")
    image=models.ImageField(upload_to='minimarket')
    client=models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="Dueño")

    def __str__(self):
        return self.name_mini

class Categoria(models.Model):
    name_cat=models.CharField(max_length=50,primary_key=True,verbose_name="Nombre")

    def __str__(self):
        return self.name_cat

class Producto(models.Model):
    codigo=models.CharField(max_length=100,primary_key=True,verbose_name="Codigo")
    name_prod=models.CharField(max_length=50,verbose_name="Nombre")
    brand=models.CharField(max_length=50,verbose_name="Marca")
    price=models.IntegerField(verbose_name="Precio")
    image=models.ImageField(upload_to='productos')
    client=models.ForeignKey(Cliente,on_delete=models.CASCADE,verbose_name="Cliente")
    category=models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name="Categoria")

    def __str__(self):
        return self.name_prod

class Reporte(models.Model):
    id=models.IntegerField(primary_key=True)
    category=models.CharField(max_length=50,verbose_name="Categoria/Asunto")
    detail=models.TextField(verbose_name="Detalle")

    def __str__(self):
        return self.id
