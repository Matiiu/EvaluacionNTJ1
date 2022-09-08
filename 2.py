""" 2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
mismo tiempo en sentido inverso al ingresado+(1) """

print('*** SALPICON ***')



frutas = []

opcion = 0

while opcion < 2: 
    fruta = {}  
    opcion +=1
    fruta['nombre'] = input(f'Digite el nombre de la fruta {opcion}: ')
    fruta['color'] = input(f'Digite el color de la fruta {opcion}: ')
    fruta['precio'] = int(input(f'Digite el precio de la fruta {opcion}: '))
    frutas.append(fruta)
    frutas.reverse()

print(frutas)


   
   
    