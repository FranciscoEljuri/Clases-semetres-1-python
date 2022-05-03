""" i=1
suma=0
num=int(input(" ingrese cuantos numeros positivo quiere sumar: "))

while i <= num:
    num2=int(input(f"{i}.)ingrese el numero: "))
    if num2 >= 0:
        suma = suma + num2
        i = i +1
    else:
        print("ingrese un numero positivo, porfavor.")

print=(f"los {num} numeros sumados son: {suma}")
 """
suma_totalpan=0
i=0
cantidad_pan=int(input("ingrese la cantidad de pan que va a comprar: "))

while i < cantidad_pan:
    tipo_pan=int(input("1) Amasado $1.500\t 2)Molde $1.000\t 3)Baguette $2.000\t 4)Integral $3.000\n "))
    if tipo_pan == 1:
        suma_totalpan = suma_totalpan + 1500
        print("usted lleva pan amasado")
    elif tipo_pan == 2:
        suma_totalpan = suma_totalpan + 1000
        print("usted lleva pan molde")
    elif tipo_pan == 3:
        suma_totalpan = suma_totalpan + 2000
        print("usted lleva pan baguette")
    elif tipo_pan == 4:
        suma_totalpan = suma_totalpan + 3000
        print("usted lleva pan integral")
    else:
        print("no existe ese tipo de pan")
    i=i+1
if suma_totalpan >= 5000:
    print("usted tiene enivo gratis")
    print(f"monto total a pagar: {suma_totalpan}")
else:
    
