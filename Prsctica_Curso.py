""" print("Ingrese los siguientes datos")

nombre1=input("ingrese el nombre de producto")
precio1=int(input("ingrese el precio "))

nombre2=input("ingrese el nombre de producto")
precio2=int(input("ingrese el precio "))


BONIFIFACION=20
precio_compra_total = precio1 + precio2 
comparar = precio1 > precio2
cabecera = "mensaje numero 1: {0}. mensaje numero dos: {1}."
print(cabecera.format(nombre1, nombre2))


precio_compra_total += BONIFIFACION 
print(f"precion de la compra total + la bonificacion es: {precio_compra_total} " )
 """

""" nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))
promedio = round((nota1 + nota2 + nota3)/3,1)


if promedio >= 7:
    print(f"promediado, su promedio es: {promedio}")
elif promedio >= 4 and promedio <= 6:
    print(f"regular, su promedio es: {promedio}")
else:
    print(f"reprobado, su promedio es: {promedio} ") """




""" 

cantidad = 0
i = 1
n = int(input("ingrese la cantidad de piezas va a cargar: "))
while i<=n:
    largo=float(input("ingrese la medida de la pieza : "))
    if largo>=1.2 and largo<=2.0:
        cantidad=cantidad+1
    i=i+1

   
   
print(f"la cantidad de piezas a llevar son: {cantidad}")
 """
""" 
for x in range (20,31):
    print(f"{x}")

     """


""" mi_lista = ['juan', 'pablo', 'jose', 'jesus']
for nombre in mi_lista:
    print(f"{nombre}")
 """



""" lista=[]
for i in range (5):
    lista.append(input("introduce los datos de la lista: "))
    
print(f"{lista}")

valor=int(input("ingrece el numero de lista que quiere cambiar"))
nuevo=input("ingrese el nuevo nombre agregar a la lista")
lista[valor]= nuevo
print(f"la nueva lista es: {lista}")
nuevo=input("introcude el valor a buscar: ")
resultado=(nuevo in lista)
if resultado:
    print(f"existe el elemento a buscar en la lista y su indice es: { lista.index(nuevo)}")
else:
    print("no existe ese elemento")

 """

###ejercicio 1 de la clase
""" nombre=input("ingrese su nombre: ")
edad=int(input(f"porfavor introduce tu edad {nombre}: "))

if edad >= 18: 
    print(f"{nombre} usted es mayor de edad, puede pasar")

elif edad >= 0 and edad <= 17:
    print(f"{nombre} uated es menor de edad")

else:
    print(f"{nombre} ingrese de nuevo su edad, nopuede ingresar")
 """

""" puntaje=0.0
animal=int(input("¿cual de los siguientes animales vive bajo el agua: \n 1.-perro\n 2.-cocodrilo\n 3.-conejo\n 4.-tiburon ")) 
if animal == 4:
    puntaje=puntaje+1.0
    print("respuesta correcta")
elif animal == 2:
    puntaje=puntaje+0.5
    print("respuesta regular")
else:
    print("usted no obtuvo ningun puntaje, respuesta incorrecta")    

print(f"su puntaje obtenido es: {puntaje}") """

""" from re import I

puntaje=0
i=1
jugdores=int(input("Bienvanidos, cuantos jugadores son: "))
print("----------------------")
print("okey. las intrucciones son las siguientes:\n 1.- el que tenga mas puntos gana(respuestacorrecta)\n 2.- ninguna mas jajajaja ")
print("----------------------")
while i <= jugdores:
    
    print(f"okey, jugador {i} es su turno. suerte :)")
    print("----------------------")
    pregunta1=int(input("pregunta 1\n en cual casa te meti por primera vez el pene.\n 1.- donde tu mama\n 2.- donde tu papa\n 3.- casa francisco\n 4.- en la calle"))
    if pregunta1 == 2:
            print("respuesta correcta")
            puntaje=puntaje+1
    else:
            print("respuesta incorrecta")
            puntaje=puntaje
    print("----------------------")

    pregunta2=int(input("pregunta 2\n al paulo le gusta tragarse a leche.\n 1.- si\n 2.- no\n 3.- tal vez\n 4.-nika"))
    if pregunta2 == 1:
                print("respuesta correcta")
                puntaje=puntaje+1
    else:
                print("respuesta incorrecta")
                puntaje=puntaje
    print("----------------------")
    pregunta3=int(input("pregunta 3\n vamos a tener sexo hoy\n 1.- no\n 2.- puede ser\n 3.- nika\n 4.- si,con chupada"))
    if pregunta3 == 4:
                print("respuesta correcta")
                puntaje=puntaje+1
    else:
                print("respuesta incorrecta")
                puntaje=puntaje
    print("----------------------")
    pregunta4=int(input("pregunta 4\n que vamos hacer ahora\n 1.- jugar\n 2.- ver que vamos a comer\n 3.- nada\n 4.- jugar con el pito mio"))
    if pregunta4 == 2:
                print("respuesta correcta")
                puntaje=puntaje+1
    else:
            print("respuesta incorrecta")
            puntaje=puntaje    
    print("----------------------")
    print(f"el total de punto son {puntaje}")
    i=i+1
    
 """



