import random
print("Semana No.16: Ejercicio 1")
lista =[]

for x in range (10):
    lista.append(random.randint(0,10))
opcion ="a"

while(opcion != "e"):
    print("Menú")
    print("a. Mostrar números","b. Promedio","c. Longitud","Encontrar y mostrar")
    opcion = input("Ingrese su opción:")
    match opcion:
        case "a":
            for x in range(len(lista)):
                print(f"No. {x}:{lista[x]}")
        case "b":
            print("Promedio")
            sumatoria=0
            for x in range(len(lista)):
                sumatoria += lista[x]
            promedio=sumatoria/len(lista)
            print(f"-----Promedio: {promedio}")
        case "c":
            print(f"Longitud de arreglo: {len(lista)}")

        case "d":
            for x in range(len(lista)):
                total=lista[x]%2
                if total==0:
                   print("") 
             
                

print("Semana No.12: Ejercicio 2")

cantFilas =int(input("Ingrese la cantidad de filas: "))
cantCols =int(input("Ingrese la cantidad de columnas: "))

matriz =[[0 for x in range(cantCols)]for y in range (cantFilas)]
mayor =0
menor = 0
for xFilas  in range (cantFilas):
    for xCols in range (cantCols):
        matriz[xFilas][xCols]= random.randint(0,1000)
        
        #Número mayor
        if(matriz[xFilas][xCols] > mayor):
            mayor = matriz[xFilas][xCols]
        #Número menor
        if(matriz[xFilas][xCols] < menor):
            menor = matriz[xFilas][xCols]
print(matriz)

print(f"El números mayor es : {mayor}")
print(f"El número menor es: {menor}")

