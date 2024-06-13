import csv
import random

def leer_zonas(archivo):
    zonas = {}
    with open(archivo, mode='r', encoding='latin-1') as archivo:
        reader = csv.reader(archivo)
        next(reader)  
        for row in reader:
            region, zona = row
            if zona not in zonas:
                zonas[zona] = []
            zonas[zona].append(region)
    return zonas

def mostrar_menu(zonas):
    print("Zonas disponibles:")
    for i, zona in enumerate(zonas.keys(), 1):
        print(f"{i}. {zona}")
    print(f"{len(zonas)+1}. Salir")
    opcion = int(input("Seleccione una zona (número): "))
    if opcion==len(zonas)+1:
        return  None
    return list(zonas.keys())[opcion - 1]

def ingresar_sismos(regiones):
    sismos = {}
    for region in regiones:
        print(f"Ingresar magnitud de tres sismos para la región {region}:")
        sismos_region = []
        for i in range(3):
            magnitud = random.uniform(1.0, 10.0)
            print(f"Magnitud del sismo {i+1} para {region}: {magnitud:.2f}")
            sismos_region.append(magnitud)
        sismos[region] = max(sismos_region)
    return sismos

def main():
    archivo_zonas = 'Zonas.csv'
    zonas = leer_zonas(archivo_zonas)
    while True:
        zona_seleccionada = mostrar_menu(zonas)
        if zona_seleccionada is None: 
            print("Saliendo del programa...")
            break
        print(f"Zona seleccionada: {zona_seleccionada}")

        regiones_seleccionadas = zonas[zona_seleccionada]
        sismos = ingresar_sismos(regiones_seleccionadas)

        print("\nSismos con mayor intensidad registrados por región:")
        for region, magnitud in sismos.items():
            print(f"{region}: {magnitud:.2f} Richter")

if __name__ == "__main__":
    main()
