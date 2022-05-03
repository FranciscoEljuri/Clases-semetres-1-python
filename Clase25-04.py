""" fact= 1
i= 1
numero=int(input("ingrese un numero: "))
while i <= numero:
    fact=fact*i
    i=i+1

print(f"el factorial de {numero} es: {fact} ") """






""" #actividad 2

i = 1
cont = 0
while i <= 5:
    numero=int(input(f"ingrese nunmero {i} : "))
    cont = cont + numero
    i = i + 1

print(f"el resultado de los numeros sumados son: {cont}")
 """

numero=int(input("ingrese un numero un numero positivo entre 103 y 987"))
resulta=(numero/10)%10
resulta1=numero%20
resulta2=numero%30

print(f"{resulta}")
print(f"{resulta1}")
print(f"{resulta2}")

