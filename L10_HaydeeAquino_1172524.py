print("Semana No.10: Ejercicio 1")
mesEntrada=int(input("Ingrese un número del 1-12:"))
mesSalida = ""

match mesEntrada:
    case 1:
        mesSalida = "Enero"
    case 2:
        mesSalida = "Febrero"
    case 3:
        mesSalida = "Marzo"
    case 4:
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6:
        mesSalida = "Junio"
    case 7:
        mesSalida = "Julio"
    case 8:
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11:
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    case _:
        print("Error: El número a ingresar debe estar contenido entre 1 y 12")

print(f"MES:{mesSalida}")

#Actividad 2
print("Semana No. 10: Ejercicio 2")

#Entradas
a=int(input("Ingrese el primer número mayor a cero:"))
b=int(input("Ingrese el segundo número mayor a cero:"))
c=int(input("Ingrese el tercer número mayor a cero:"))

#Validación
print("El número mayor es:")
if a<=0 or b<=0 or c<=0:
    print("Error: El número debe ser mayor a cero")

#Diagrama
if a>b:
    if a>c:
        print(a)
    else: 
        if a==c:
            print(a,"y",c)
        else:
            print(c)
elif a==b:
    if a>c :
        print(a,"y",b)
    elif a==c:
        print(a,b,"y",c)
else:
        print(c)
if b>c:
    print(a,"y",b)
elif b==c:
    print(a,b,"y",c)  
else:
    print(c)

#Actividad 3
print("Semana No. 10: Ejercicio 3")

#Encabezado
print("Nombre: Haydee Aquino")    
print("No. de carné: 1172524")  

#Entradas
dia=int(input("Ingrese día de nacimiento:"))
mes=int(input("Ingrese mes de nacimiento:"))
año=int(input("Ingrese año de nacimiento:"))

print("Su Signo Zodiacal es:")
if (mes==3 and dia>=21)or(mes==4 and dia<=19):
    print("Aries")
elif (mes==4 and dia>=20)or(mes==5 and dia<=20):
    print("Tauro")
elif (mes==5 and dia>=21)or(mes==6 and dia<=20):
    print("Géminis")
elif (mes==6 and dia>=21)or(mes==7 and dia<=22):
    print("Cancer")
elif (mes==7 and dia>=23)or(mes==8 and dia<=22): 
    print("Leo")
elif (mes==8 and dia>=23)or(mes==9 and dia<=22):
    print("Virgo")
elif (mes==9 and dia>=23)or(mes==10 and dia<=22):
    print("Libra")
elif (mes==10 and dia>=23)or(mes==11 and dia<=21):
    print("Escorpio")
elif (mes==11 and dia>=22)or(mes==12 and dia<=21):
    print("Sagitario")
elif (mes==12 and dia>=21)or(mes==1 and dia<=19):
    print("Capricornio")
elif (mes==1 and dia>=20)or(mes==2 and dia<=20):
    print("Acuario")
elif (mes==2 and dia>=19)or(mes==2 and dia<=19):
    print("Piscis")



        
