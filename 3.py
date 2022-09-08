""" 3.Construir un programa para ir de compras en un supermercado
que permita la construcción del siguiente MENU:

1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
2. Digitar 2 para mostrar todos los productos registrados (+0.4)
3. Digitar 3 para permitir buscar por código un producto y editar el precio
de este (+0.4)
4. Digitar 4 para permitir buscar por código un producto y eliminar el
producto (+0.4)
5. Digitar 0 para SALIR
Finalmente, versione y comparta el repositorio según las indicaciones
dadas+(1.4)
 """

print('1. Ingresar producto')
print('2. Mostrar productos')
print('3. Buscar producto y editarlo')
print('4. Buscar producto y eliminarlo')
print('0. Salir')

menu = 100

productos = []
while menu != 0:
      #DICCIONARIO
    producto = {}
    encontrado = False

    opcion = int(input('Elija una opcion: '))
    
    if opcion == 1:
        producto['codigo'] = input('Digite su código del producto: ')
        producto['nombre'] = input('Digite su nombre del producto: ')
        producto['precio'] = input('Digite el precio del producto: ')
        productos.append(producto)

    elif opcion == 2:
        print(productos)

    elif opcion == 3:
        codigo = input('Digite el código del producto ')
        for producto in productos:
            
            if(producto['codigo'] == codigo):
                producto['precio'] = input('Digite el precio del producto: ')  
                break        
            else:
             print(f"El producto con el código {codigo} no esta registrado")         

    elif opcion == 4:
          codigo = input('Digite el código del producto ')
          for i in  productos:
            
            if(i['codigo'] == codigo):
                productos.remove(i)    
                break

            else:
             print(f"El producto con el código {codigo} no esta registrado")                
               

    elif opcion == 0:
        print('BYE')
        break
    
    else:
        print('Digite una opción valida')

 