total_cantidad_placa= 0
i= 0
total_compra=0
while i <= 1:
    tipo_plca=int(input("que tipo de placa desea:\t 1)pequeña $3.500\t 2)mediana $4.500\t 3)grande $5.500\t"))
    if tipo_plca == 1:
        cantidad_placa=int(input("indique cuantas placas quiere:  "))
        total_compra= total_compra + (cantidad_placa * 3500)
        total_cantidad_placa= total_cantidad_placa + cantidad_placa
    elif tipo_plca == 2:
        cantidad_placa=int(input("indique cuantas placas quiere:  "))
        total_compra= total_compra + (cantidad_placa * 4500)
        total_cantidad_placa= total_cantidad_placa + cantidad_placa
    elif tipo_plca == 3:
        cantidad_placa=int(input("indique cuantas placas quiere:  "))
        total_compra= total_compra + (cantidad_placa * 5500)
        total_cantidad_placa= total_cantidad_placa + cantidad_placa
    else:
            print("informacion no valida")
          ###  total_cantidad_placa= total_cantidad_placa + 0
           ### total_compra= total_compra + 0

    i=int(input("1)seguir comprando\t  2)desea terminar su compra\t "))
    

if total_compra > 10000:
    print(f"su compra es superior a $10.000.- tiene despacho gratis\n El total de su compra es {total_compra} cantidad de productos: {total_cantidad_placa}")
elif total_compra <10000:
    print(f"su compra es inferior a $10.000.- no tiene despacho gratis\n El total de su compra es {total_compra} cantidad de productos: {total_cantidad_placa}")
elif total_compra <= 0:
    print("no compro nada")











