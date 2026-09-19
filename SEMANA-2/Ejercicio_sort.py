def ordenar_precios():
   
   n = int(input("Ingrese la cantidad de productos: "))
   if n <= 0:
       print("La cantidad de productos debe ser mayor a 0.")
       return
   
   precios = []
   print("\n--- Ingrese los precios ---")
   for k in range(n):
       precio = float(input(f"Precio del producto {k + 1}: "))
       precios.append(precio)
   
   print("Seleccione el tipo de ordenamiento")
   print("1. Ascendente (Menor a Mayor)")
   print("2. Descendente (Mayor a Menor)")
   opcion = input("Ingrese su opción (1 o 2): ")
 
   for i in range(1, n):
       clave = precios[i]
       j = i - 1
       
       while j >= 0 and precios[j] > clave:
           precios[j + 1] = precios[j]
           j = j - 1
       precios[j + 1] = clave
 
   if opcion == "2":
       precios.reverse()  
   elif opcion != "1":
       print("\n[!] Opción no válida. Se mostrará en orden ascendente por defecto.")
 
   print("\n--- Lista de Precios Ordenada ---")
   for idx, precio in enumerate(precios, 1):
       print(f"Producto {idx}: ${precio:.2f}")
 
ordenar_precios()
