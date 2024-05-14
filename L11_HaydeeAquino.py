#Ejercicio 1
print ("Semana No.11: Ejercicio 1")

n = int(input("Ingrese un número mayor a cero:"))

#Declaración de variables
a=0
b=1
c=0
i=2
resultado=""
if (n>0):
    resultado = str(a)
    if(n>1):
        resultado += "," + str(b)
        
    while(i<n):
        c = a + b
        resultado += "," + str(c)
        a = b
        b = c
        i = i + 1
    print(resultado) 
else:
    print(resultado)

#Ejercicio 2
print ("Semana No.11: Ejercicio 2")
n = int(input("Ingrese un número mayor a cero:"))
if(n <= 0):
    print("Error: el número debe ser mayor a cero")
resultadoA = 0
for x in range (1, n+1):
    resultadoA += (1/x)

print("Inciso A:",resultadoA)

#Ejercicio 3
print ("Semana No.11: Ejercicio 3")

x = int(input("ingrese un numero: "))
a = int(input("ingrese otro numero: "))
n = int(input("ingrese el numero final: "))
k =0 
resultadoB= (x**k)*(a**(n-k))
for k in range (0, n+1):
    resultadoB+= (x**k)*(a**(n-k))
print("El resultado es:",resultadoB)