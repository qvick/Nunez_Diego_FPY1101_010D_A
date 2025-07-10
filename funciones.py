productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 

}


def menu():
    menusito="""
*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir."""
    while True:
        print(menusito)
        try:
            opc=str(input("Ingrese una Opción(1-4): "))
        except:
            print("Ingrese caracteres Validos!.")
        if opc=="1":
            marca=str(input("Ingrese Marca: "))
            stock_marca(marca)
        elif opc=="2":
            p_min=int(input("Ingrese Valor minimo: "))
            p_max=int(input("Ingrese Valor Maximo: "))
            búsqueda_precio(p_min, p_max)
        elif opc=="3":
                modelo=input("Ingrese modelo de nootebook: ")
                p = int(input("Ingrese nuevo Precio: "))
                actualizar_precio(modelo, p)
        elif opc=="4":
            print("Gracias por usar el sistema, Adios!.")
            break

def stock_marca(marca):
    compu = []
    models= []
    contador=0
    for k in productos:
        models=stock[k][1]
        compu = productos[k][0]
        if marca==compu:
            contador+=models
    print(f"Hay {contador} stock de {marca}")

def búsqueda_precio(p_min, p_max):
    precio=[]
    existencia=[]
    for k in stock:
        precio=p_min, p_max
        existencia=productos[k][0]
        if p_min < stock[k][0] and p_max > stock[k][0]:
            if precio!=k:
                print(f"Los notebooks entre los precios consultas son: {productos[k][0]}--{k} ")
                
def actualizar_precio(modelo, p):
    while True:
        for k in stock:
            if modelo==k:
                print("Precio actualizado.")
                opc1=input("¿Desea ingresar otro precio?(y/n):")
                if opc1=="y":
                    return
                elif opc1=="n":
                    return
            else:
                print("No se encontro el modelo!.")
                opc1=input("¿Desea ingresar otro precio?(y/n):")
                if opc1=="y":
                    return
                elif opc1=="n":
                    return
                

        

