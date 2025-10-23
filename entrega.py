productos = []

while True:
    print("0. MENÚ DE OPCIONES")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por número")
    print("5. Salir")

    elegir = (input("Elegí una opción: "))

    if not elegir.isdigit():
        print("Opción no válida. Elegí un número entre el 1 al 5.")
        continue

    elegir = int(elegir)


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
        if not productos:
            print("No hay productos cargados.")
        else:
            contador = 1
            for producto in productos:
                print(f"{contador}. Nombre: {producto[0]}, Categoria: {producto[1]}, Precio: ${producto[2]}")
                contador += 1


    elif elegir == 3:
        if not productos:
            print("No hay productos cargados.")
        else: 
            busqueda = input("Ingrese el producto a buscar: ").capitalize()
            busqueda = busqueda.strip()
            encontrado = ""

            for producto in productos:
                if (producto [0] == busqueda):
                    encontrado = producto
                    break
            print("buscando....")

        if(encontrado != ""):
                print(f"Producto encontrado: {encontrado[0]}, Categoría: {encontrado[1]}, Precio ${encontrado[2]}")
        else:
                print("Producto inexistente")
        
    elif elegir == 4:
        if not productos:
            print("No hay productos cargados.")
        else:
            producto_busqueda = input("Ingrese el producto que desea eliminar: ").strip().capitalize()
            encontrado = False  
        for producto in productos:
            if producto[0] == producto_busqueda:
                productos.remove(producto)
                print(f"El producto '{producto[0]}' fue eliminado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print("No existe el producto ingresado.")


    elif elegir == 5:
        print("Saiendo del programa...")
        break
    else:
        print("Opción no válida. Elegí un número entre el 1 al 5.")


