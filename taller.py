import os

titulo =f"""       Listado de vehiculos
{"-" * 75}
{"MARCA:<20"}{"AÑO:<20"}{"KILOMETRAJE:<10"}{"COSTO DE REPARACIÓN ESTIMADO:>10"}{"IMPUESTO DE SERVICO:>10"}{"COSTO TOTAL A PAGAR:>10"}
{"-" * 75}
"""

menu = """"
1. Registrar vehiculo
2. Listar todos los vehiculos
3. Imprimir orden de reparacion
4. Salir del programa
"""
vehiculos = []
marcas = ["toyota","ford","chevrolet","mazda","audi"]

def registarvehiculo():
    while True:
        try:
            marc = input("Marca: ").lower
            año = int(input("Año de fabricacion: "))
            kilom = int(input("Kilometraje: "))
            costo_repa = int(input("Costo de reparacion estimado: "))
            if marc in marcas or año>0 or kilom>0:
                impuest_serv = round(costo_repa * 0.08)   
                costo_total = round(costo_repa + impuest_serv) 
                vehiculos.append([marc,año,kilom,costo_repa,impuest_serv,costo_total])
                input("Vehiculo agregado con exito¡")
                break
            else:
                print("Algo ingreso mal... intente nuevamente")
        except Exception as e:
            print(f"Excepcion al registrar: {str(e)}")


def listartodoslosvehiculos():
    salida = titulo
    for t in vehiculos:
        salida += f"{t[0]:<20}"
        salida += f"{t[1]:<20}"
        salida += f"{t[2]:<10}"
        salida += f"{t[3]:>10}"
        salida += f"{t[4]:>10}"
        salida += f"{t[5]:>10}"
        salida +=  "\n"
    return salida
def listarxmarca(marc):
    salida = titulo
    for t in vehiculos:
        if t[2] == marc:
            salida += f"{t[0]:<20}"
            salida += f"{t[1]:<20}"
            salida += f"{t[2]:<10}"
            salida += f"{t[3]:>10}"
            salida += f"{t[4]:>10}"
            salida += f"{t[5]:>10}"
            salida +=  "\n"
        return salida
def imprimirordenreparacion():
    marc = input(f" marca {marcas}: ")
    if marc in marcas:
        with open(marc+".txt", "w") as archivo:
            archivo.write(listarxmarca(marcas))
    else:
        input("marca no corresponde") 


while True:
    try:
        opc = input(menu)
        if opc == "4":
            break
        elif opc == "1":
            registarvehiculo()
        elif opc == "2":
            print(listartodoslosvehiculos())
        elif opc == "3":
            imprimirordenreparacion()
    except Exception as e:
        input(f"Excepc menu: {str(e)}")