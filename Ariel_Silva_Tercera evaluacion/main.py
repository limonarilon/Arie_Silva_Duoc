from datetime import date, time, datetime
import csv
reclamos=[]
def menu():
    print("Programa Reclamos")
    print("1. Registrar Reclamo")
    print("2. Listar Reclamos")
    print("3. Respaldar Reclamos")
    print("4. Salir")


def registrar_reclamo():
    global reclamos
   
    rut=(input("Ingrese su rut: "))
    while True:
        try:
            monto=int(input("Ingrese el monto del reclamo: "))
            break
        except ValueError:
            print("Debes ingresar un monto válido como número entero.")
    reclamo_particular=input("Ingrese su reclamo: \n")
    fecha_actual=datetime.now()
    fecha=fecha_actual.strftime('%d-%m-%Y')
    reclamo={
        "rut":rut,
        "monto":monto,
        "reclamo":reclamo_particular,
        "fecha":fecha        
    }
    reclamos.append(reclamo)
    print("Su reclamos fue registrado correctamente.")
    
def listar_reclamos():
    print("RUT  |  MONTO  |  RECLAMO  |  FECHA ")
    for reclamo in reclamos:
        print(f"{reclamo["rut"]}  |  {reclamo["monto"]}  |  {reclamo["reclamo"]}  |  {reclamo["fecha"]}")

def respaldar_reclamos():
    with open("reclamos.csv","w", encoding="utf-8") as archivo:
        escritor_csv=csv.writer(archivo)
        escritor_csv.writerows([reclamos])

while True:
    menu()
    op=input("Seleccione una opción: ")
    if op=="1":
        registrar_reclamo()
    elif op=="2":
        listar_reclamos()
    elif op=="3":
        respaldar_reclamos()
    elif op=="4":
        print("Saliendo del programa...")
        break
    else:
        print("Debes ingresar una opción válida")

