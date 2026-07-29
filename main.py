from inventario import Inventario

inventario = Inventario()

while True:
    print("\n" + "-" *50)
    print("SISTEMA DE REGISTROS")
    print("\n" + "-" *50)
    print("1. Agregar Productos ")
    print("2. Ver todos los productos ")
    print("3. Buscar productos ")
    print("4. Eliminar producto ")
    print("5. Valor total del inventario ")
    print("6. Reporte por categoria ")
    print("8. Guardar y salir ")
    print("-" * 50)
    try:
        cliente = int(input("ingresa una opcion "))
    except ValueError:
        print(" Ingresa un número válido")
        continue

    if cliente==1:
        nombre = input("ingresa nombre del producto ")
        categoria = input("ingresa categoria del producto ")
        precio = int(input("ingresa precio del producto "))
        cantidad = int(input("ingresa cantidad del producto "))
        producto = inventario.agregar(nombre, categoria, precio, cantidad)
        print(f"Producto agregado con ID: {producto.id}")    

    elif cliente==2:
        producto = inventario.listar()
        print("ID    Nombre         Precio     Cantidad   Categoría")
        print("----  -------------  ---------  ---------  ----------")
        for prod in producto:
            print(f"{prod.id:<5} {prod.nombre:<15} ${prod.precio:<10.2f} {prod.cantidad:<10} {prod.categoria:<10}")

    elif cliente ==3: 
        id = int(input("ingrese el ID del producto "))      
        producto = inventario.buscar(id)
        print(f"El producto es : {producto}")
    elif cliente ==4:
        id = int(input("ingrese el ID del producto a eliminar "))        
        producto = inventario.eliminar(id)
        print(f"El producto con Id: {id} se elimino correctamente")
    elif cliente ==5:  
        valorTotal = inventario.valor_total()
        print(f"Valor total del inventario es de: ${valorTotal}")      
    elif cliente ==6:
        reporte = inventario.reporte_categoria()
        if not reporte:
            print("No hay productos")
        else:
            print("\n=== REPORTE POR CATEGORÍA ===")
            for categoria,producto in reporte.items():
               print(f"{categoria}")

    elif cliente ==8:
        estado = inventario.guardar()
        print("Inventario guardado correctamente")


    else:
        print("Opción inválida")