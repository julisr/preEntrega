productos = []

while True:
    print("0. MENÚ DE OPCIONES")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por número")
    print("5. Salir")

    elegir = int(input("Elegí una opción: "))


    if elegir == 1:
        nombre = input("Nombre del producto: ").strip().capitalize()
        categoria = input("Categoría del producto: ").strip().capitalize()
        while True:
            precio = input("Precio (sin centavos): ").strip()
            if precio.isdigit():
                precio = int(precio)
                break
            else:
                print("Por favor, ingresá un número válido.")

        productos.append([nombre, categoria, precio])
        print(f"Producto '{nombre}' agregado correctamente.")

    elif elegir == 2:
        if productos == "":
            print("No hay productos cargados.")
        else:
            print(productos)
    elif elegir == 3:
        if productos == "":
            print("No hay productos cargados.")
        else: 
            busqueda = input("Ingrese el producto: ").capitalize()
            busqueda = busqueda.strip()
            encontrado = ""

            for nombre in productos:
                if (nombre == busqueda):
                    encontrado = nombre
                    break
            print("buscando....")

            if(encontrado != ""):
                print(f"Producto encontrado: {nombre}")
            else:
                 print("Producto inexistente")
                 
    elif elegir == 4:
        producto_busqueda = input ("Ingrese el procucto que desea eliminar: ")
        producto_busqueda = producto_busqueda.capitalize()

        if (producto_busqueda in productos ):

             for producto in productos:

                 if(producto_busqueda == producto):
                    productos.remove(producto_busqueda)
                    print(f"El producto: {producto} ha sido eliminado correctamente")
                    break
        else: 
         print ("No existe el producto ingresado")


    elif elegir == 5:
        print("👋 Saliendo del programa...")
        break
    else:
        print("⚠️ Opción no válida. Elegí entre 1 y 5.")

        
            


