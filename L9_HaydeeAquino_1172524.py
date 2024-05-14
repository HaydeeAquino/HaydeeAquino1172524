print("ejercicio 1: operaciones aritméticas")

n1=int(input("Ingrese el primer número:"));
n2=int(input("Ingrese el segundo número:"));

suma=n1+n2
resta=n1-n2
mult=n1*n2
divReal= n1/n2
divEntera= n1//n2
divModular= n1%n2

print(n1,"+",n2,"=",suma)
print(n1,"-",n2,"=",resta)
print(n1,"*",n2,"=",mult)
print(n1,"/",n2,"=",divReal)
print(n1,"//",n2,"=",divEntera)
print(n1,"%",n2,"=",divModular)

print("Ejercicio 2: operaciones booleanas")

igualad= n1==n2
diferentes=n1!=n2
menor= n1<n2

mayor=n1>n2

print(n1,"==",n2,"=",igualad)
print(n1,"!=",n2,"=",diferentes)
print(n1,"<",n2,"=",menor)
print(n1,">",n2,"=",mayor)

print("Ejercicio 3: jerarquia de operadores")
a=int(input("Ingrese el primer valor:"));
b=int(input("Ingrese el segundo valor:"));
c=int(input("Ingrese el tercer valor:"));

print("i.",(a*b)+c)
print("ii.",a*(b+c))
print("iii.",a/(b+c))
print("iv.",((3*a)+(2*b))/(c**2))

print("Actividad 3: ejercicio 1")
metro1=int(input("Ingrese metros:"));

km=metro1/1000
millas=km/1.69
pies1=metro1*3.28
pulg=pies1*12
print("Millas:",millas)
print("kilometros:",km)
print("Pies:",pies1)
print("Pulgadas:",pulg)

print("Actividad 3: ejercicio 2")
metro2=int(input("Ingrese metros:"));

yarda=metro2//0.9144
modyarda= metro2%0.9144
pies2=modyarda//0.33333
modpies=modyarda%0.33333
pulg2=modpies//0.0833333
modpulg=modpies%0.0833333

print("yardas:",yarda,"pies:",pies2,"pulgadas:", pulg2)

