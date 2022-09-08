""" 1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1) """

mult2 = 0
mult3 = 0
x = True
cont = 0

while x != False: 
    cont += 1  
    num = int(input(f'Ingrese numero {cont}: '))    
    if(num % 2 == 0):
        mult2 +=1
    if(num % 3 == 0):
        mult3 += 1
    pregunta = input ('¿Ingresara otro valor? s/n ')
    if(pregunta == 'n'):
     x = False




print(f'Hay {mult2} multiplos de 2')
print(f'Hay {mult3} multiplos de 3')




