""" print("bienvenido al supermercado COOL-LTDA")
cliente_preferencial=0
productos=0
descuento=0.25
pago_total=0
cliente=int(input("Seleccione tipo de cliente:\t 1)Preferencial\t 2)No Preferencial "))
if cliente == 1:
    print("Usted es cliente preferencial, recibira un descuento en el total de la compra")    
    cliente_preferencial= descuento * pago_total
elif cliente == 2:
    print("Usted no es cliente preferencial")
    cliente_preferencial=2
else:
    print("ingrese bien el tipo de cliente ")

print("Seleccione los siguiente producto")
 """

""" 
descuento = 0
valor_total_compra =0
total_a_pagar = 0
print("bienvenido al supermercado de francisco")
nombre_usuario =input("ingrese su nombre: ")
tipo_cliente= int(input(f"{nombre_usuario} que tipo de cliente es: 1.) Preferencial\t 2.) No preferencial "))

if tipo_cliente == 1:
    print(f"{nombre_usuario} usted es cliente preferencial, sigamos con su compra :)")
    descuento = 0.25
elif tipo_cliente == 2:
    print(f"{nombre_usuario} usted es cliente no preferencial, sigamos con su compra :)")
else:
    print("ingrese bien el tipo de usuario")

print(f"{nombre_usuario} aca tenemos los mejores productos para ti, ve seleccionando y l final te saldra el resumen de tu compra: ")

agua =int(input("1.- Agua\n Valor: $600.-\n desea llevarlo: 1.) si\t 2.) no"))
if agua == 1:
    valor_total_compra = valor_total_compra + 600
elif agua == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

azucar =int(input("2.- Azucar\n Valor: $1200.-\n desea llevarlo: 1.) si\t 2.) no"))
if azucar == 1:
    valor_total_compra = valor_total_compra + 1200
elif azucar == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

aceite =int(input("3.- Aceite\n Valor: $1500.-\n desea llevarlo: 1.) si\t 2.) no"))
if aceite == 1:
    valor_total_compra = valor_total_compra + 1500
elif aceite == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

arroz =int(input("4.- Arroz\n Valor: $1250.-\n desea llevarlo: 1.) si\t 2.) no"))
if arroz == 1:
    valor_total_compra = valor_total_compra + 1250
elif arroz == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

fideos =int(input("5.- Fideos\n Valor: $790.-\n desea llevarlo: 1.) si\t 2.) no"))
if fideos == 1:
    valor_total_compra = valor_total_compra + 790
elif fideos == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

bebida =int(input("6.- Bebida\n Valor: $1780.-\n desea llevarlo: 1.) si\t 2.) no"))
if bebida == 1:
    valor_total_compra = valor_total_compra + 1780
elif bebida == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

chocolate =int(input("7.- Chocolate\n Valor: $2500.-\n desea llevarlo: 1.) si\t 2.) no"))
if chocolate == 1:
    valor_total_compra = valor_total_compra + 2500
elif chocolate == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")

pan =int(input("8.- pan\n Valor: $1340.-\n desea llevarlo: 1.) si\t 2.) no"))
if pan == 1:
    valor_total_compra = valor_total_compra + 1340
elif pan == 2:
    valor_total_compra = valor_total_compra
else:
    print("ingrese la eleccion bien, profavor")


total_a_pagar = valor_total_compra * descuento
print(f"{nombre_usuario} su resumen de compra es:")
print(f"valor compra: {valor_total_compra}\n valor descuento: {descuento}\n total a pagar:{total_a_pagar} ")
 """