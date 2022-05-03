""" #Ejercicio 01
mensaje =  "Bienvenido al mundo de la programacion"
print (f"{mensaje}")

print ("Bienvenido al mundo de la programacion") """

##ejercicio 01 B y 02A

""" nom=input("ingresa tu nombre : ")
print(f"Bievenido {nom}") """

##Ejercicio 03
""" 
x = int(input("Ingresa valor para resolver la ecuacion (X^2 + 3x + 1)/4: "))
resultado = (x**2 + 3*x + 1)/4
print(f"El resultado de la ecuacion con el numero {x} es igual a {resultado}")
 """

##Ejercicio

""" nombre = input ("Ingrese su nombre :")
rut = int(input ("ingrese su rut sin digito verificador (DV) :"))
dv = input("ingrese digito verificador :")
correo = input("Ingrese su correo : ") 
celular = int(input ("Ingrese numero telefonico :"))
print("----------RESUMEN----------")
print(f"Tu nombre es: {nombre}\n RUT: {rut} \n DV: {dv} \n CORREO: \n Celular: {celular} ")
print("---------------------------") """

#sintasis if, elif y else
""" edad = int(input("Ingrese su edad"))
if edad >= 18 :
    print("Usted es mayor de edad")
elif edad <18 and edad < 0:
    print("Usted es menor de edad")
else:
    print("No existe edad, ingrese de nuevo") """

#ejercicio 2 if
""" user01 = "Pedro"
pass01 = 4.25
user02 = "Angel"
pass02 = 32.4


user0 = input("Ingrese nombre de usuario")
pass0 = int(input("Ingrese clave de usuario"))

if user0 == user01 and pass0  == pass01:
    print("Bienvenido Pedro")
elif user0 == user02 and pass0 == pass02 :
    print("Bienvenido Angel")
else :
    print("credenciales incorrectas")
 """

##ejercicio 3

""" nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))

promedio = round((nota1 + nota2 + nota3)/3,1)

if promedio >= 4.0 :
    print(f"Felicitaciones, esta aprobado con una nota de {promedio}")
else :
    print(f"Lo siento, esta reprobado con una nota de {promedio}")
     """
