
""" 
x = range(1,10,2)
for n in x:
    print(n)
     """
""" 
frase = "hola mundo"
for caracter in frase:
    print(caracter)
 """

 
suma_mayor0=0
suma_menor0=0
suma_igual0=0
i=1
while i <= 5:
    num=int(input(f"ingrese el {i} numero:\t "))
    
    if num > 0:
        suma_mayor0 = suma_mayor0 + 1
    elif num < 0:
        suma_menor0 = suma_menor0 + 1
    else:
        suma_igual0 = suma_igual0 + 1

    i=i+1 

print(f"de los 5 numeros, {suma_mayor0} son mayores a 0")
print(f"de los 5 numeros, {suma_menor0} son menor a 0")    
print(f"de los 5 numeros, {suma_igual0} son igual a 0")

 



