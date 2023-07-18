from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from entrebolsa.models import Producto, Cliente, Categoria, Minimarket

import random

def home(request):
    usuario=request.user.get_username()
    print(usuario)
    productos=Producto.objects.all().filter(client=usuario)
    mini=Minimarket.objects.all().filter(client=usuario)
    categ=Categoria.objects.all()
    return render(request,'core/home.html',{'productos':productos, 'minis':mini, 'categ':categ})

def agregarProd(request):
    codigo=request.POST['codigoform']
    nombre=request.POST['nombreform']
    cliente=request.user.username
    print(cliente)
    existe=Producto.objects.filter(name_prod=nombre,client_id=cliente).exists()
    print(existe)
    
    existec=Producto.objects.filter(codigo=codigo).exists()

    while existec==True:
        codigo=random.randint(0,999999)
        existec=Producto.objects.filter(codigo=codigo).exists()

    if existe==False:
        producto=Producto()
        producto.codigo=request.POST.get('codigoform')
        producto.name_prod=request.POST.get('nombreform')
        producto.price=request.POST.get('precioform')
        producto.brand=request.POST.get('marcaform')
        producto.client_id=request.user.get_username()
        producto.category_id=request.POST.get('catform')

        if len(request.FILES)!=0:
            producto.image=request.FILES['imageform']

        producto.save()
        messages.success(request, "Producto añadido satisfactoriamente")
        return redirect('/interfaz')
    else:
        messages.add_message(request=request, level=messages.WARNING, message="Ese nombre de producto ya existe, debe cambiar el nombre para que sean distinguibles")
        return redirect('interfaz')

    

def eliminarProd(request):
    nombre=request.POST['nombreform']
    cliente=request.user.username
    productoex = Producto.objects.filter(name_prod=nombre,client_id=cliente).exists()
    if productoex==True:
        producto = Producto.objects.get(name_prod=nombre,client_id=cliente)
        return render(request, "core/confirmarEli.html", {"producto":producto})
    else:
        messages.add_message(request=request, level=messages.WARNING, message="No existe el produto ingresado")
        return redirect('interfaz')

def eliminar(request, clave):
    cliente=request.user.username
    product = Producto.objects.get(name_prod=clave,client_id=cliente)
    product.delete()
    messages.add_message(request=request, level=messages.WARNING, message="Producto eliminado satisfactoriamente")
    return redirect('/interfaz')

def editarProd(request):
    categ=Categoria.objects.all()
    cliente=request.user.username
    nombre=request.POST['nombreform']
    productoex = Producto.objects.filter(name_prod=nombre,client_id=cliente).exists()
    if productoex==True:
        producto = Producto.objects.get(name_prod=nombre,client_id=cliente)
        return render(request, "core/edicionProducto.html", {"producto":producto, "nombre":nombre, "categ":categ})
    else:
        messages.add_message(request=request, level=messages.WARNING, message="No existe el produto ingresado")
        return redirect('interfaz')

def confirmarEdit(request):
    nombreantiguo=request.POST.get('nombreantiguoform')
    print(nombreantiguo)
    cliente=request.user.username
    nombre=request.POST['nombreform']
    precio=request.POST['precioform']
    marca=request.POST['marcaform']
    categoria=request.POST['catform']

    producto=Producto.objects.get(name_prod=nombreantiguo,client_id=cliente)
    producto.name_prod=nombre
    producto.price=precio
    producto.brand=marca
    if len(request.FILES)!=0:
        producto.image=request.FILES['imageform']
    producto.client_id=request.user.get_username()
    producto.category_id=categoria
   
    producto.save()
    messages.add_message(request=request, level=messages.SUCCESS, message="Producto modificado satisfactoriamente")
    return redirect('/interfaz')


def eliminar1(request, codigo):
    cliente=request.user.username
    product = Producto.objects.get(codigo=codigo)
    product.delete()
    messages.add_message(request=request, level=messages.WARNING, message="Producto eliminado satisfactoriamente")
    return redirect('/interfaz')

def modificar1(request, codigo):
    categ=Categoria.objects.all()
    cliente=request.user.username
    producto = Producto.objects.get(name_prod=codigo,client_id=cliente)
    return render(request, "core/edicionProducto.html", {"producto":producto, "categ":categ})

def interfaz(request):
    usuario=request.user.get_username()
    print(usuario)
    productos=Producto.objects.all().filter(client=usuario)
    mini=Minimarket.objects.all().filter(client=usuario)
    categ=Categoria.objects.all()
    print(productos)
    return render(request,'core/interfaz.html',{'productos':productos, 'minis':mini, 'categ':categ})

def search(request): #Funcion de nombre search.
    if request.method == "POST": #Si el metodo es POST, realiza la siguiente operacion.
        searched = request.POST['searched'] #Guarda en la variable searched, aquello obtenido del input del mismo nombre.
        productos = Producto.objects.filter(name_prod__contains=searched) #Guarda en la variable productos, aquellos productos de la base de datos que contengan la palabra indicada en la variable searched.
        return render(request,'core/busqueda.html',{'searched':searched,'productos':productos}) #Regresa la pagina de busqueda, y dos diccionario correspondientes a la variable searched y los datos de los productos encontrados.
    else: #En el caso que no se este efectuando el metodo POST.
        return render(request,'core/busqueda.html',{}) #Regresa la pagina de busqueda sin nada.

def comparison(request): #Funcion de nombre comparison.
    if request.method == "POST": #Si el metodo es POST, realiza la siguiente operacion.
        prodid1 = request.POST['prodid1'] #Guarda en la variable prodid1, aquello obtenido del input del mismo nombre.
        prodid2 = request.POST['prodid2'] #Guarda en la variable prodid1, aquello obtenido del input del mismo nombre.
        prod1 = Producto.objects.get(id=prodid1) #Guarda en la variable prod1, el producto con la id indicada en la variable prodid1.
        prod2 = Producto.objects.get(id=prodid2) #Guarda en la variable prod2, el producto con la id indicada en la variable prodid2.
        if prod1.price > prod2.price: #Si el precio del producto 1 es mayor al precio del producto 2, realiza la siguiente operacion.
            resta = prod1.price-prod2.price #Resta el precio del producto 2 al del producto 1.
        else: #En caso de que el precio del producto 1 no sea mayor que el del producto 2.
            resta = prod2.price-prod1.price #Resta el precio del producto 1 al del producto 2.
        return render(request,'backend/comparacion.html',{'prod1':prod1,'prod2':prod2,'resta':resta}) #Regresa la pagina de comparacion, y tres diccionario correspondientes a los datos del producto 1, los datos del producto 2, y el resultado de la diferencia del precio de los productos.
    else: #En el caso que no se este efectuando el metodo POST.
        return render(request,'backend/comparacion.html',{}) #Regresa la pagina de comparacion sin nada.

def comparar(request, nombre, codigo):
    prod_comp=Producto.objects.filter(codigo=codigo)
    terminos=nombre.split()
    lista_terminos=[]
    for i in range(len(terminos)):
        prod=Producto.objects.filter(name_prod__contains=terminos[i])
        lista_terminos.append(prod)

    print(lista_terminos)

    return render(request, 'core/comparacion.html', {'lista_terminos':lista_terminos,'prod_comp':prod_comp})