print("Menú")
print("1.Pikachu Roll- $4500")
print("2.Otaku Roll- $5000")
print("3.Pulpo Venenoso Roll- $5200")
print("4.Anguila Eléctrica Roll- $4800")
print("Seleccione su pedido. Cuando termine su orden presione '0'")
orden=0
pedido=[]
opc=5

while opc!=0:
    opc=int(input("Ingrese el número de su roll: "))

    if opc==1:
        orden+=4500
        pedido.append("Pikachu_Roll-$4500")
        print("Se ha agregado 1 orden de Pikachu Roll")
    elif opc==2:
        orden+=5000
        pedido.append("Otaku_Roll-$5000")
        print("Se ha agregado 1 orden de Otaku Roll")

    elif opc==3:
        orden+=5200
        pedido.append("Pulpo_Venenoso Roll-$5200")
        print("Se ha agregado 1 orden de Pulpo Venenoso Roll")

    elif opc==4:
       orden+=4800
       pedido.append("Anguila_Eléctrica roll-$4800")
       print("Se ha agregado 1 orden de Anguila Eléctrica Roll")
    
    elif opc==0:
       print("Saliendo del menú")

    else:
     print("Ingrese una opción válida del menú")
     break

descuento=0   
dcto="."
codigo="."
dcto=input("¿Posee un cupón de descuento?(si/no/x=salir): ")
if dcto=="si":
    while True:
     codigo=input("Ingrese su código de descuento: ")
     if codigo=="soyotaku":
      descuento=orden*0.1
      break
     else:
      print("Código inválido")
elif dcto=="no":
   print("No descuentos aplicados.")




total_final=orden-descuento
total_productos=len(pedido)
print("BOLETA")
print(f"TOTAL PRODUCTOS: {total_productos}")  
for i in range(total_productos):
   print(pedido[i]) 
print("*******************")
print(f"Subtotal por pagar: ${orden} ")
print(f"Descuento por código: ${descuento}")
print(f"TOTAL: ${total_final}")




