# inicimos el proyecto salpicon con el menu  
print ("***Salpicon***")
print ("*****")
print ("0. Salir")
print ("1. Registrar Frutas")
print ("2. Costo Total Salpicon")
print ("3. Mostrar Frutas por Precio de mayor a menor")
print ("4. Mostrar Cual es la fruta mas cara, y la mas barata")

print ("******")

opcion=90
salpicon=[]

while (opcion != 0):
  
  opcion=int(input("Digita una opcion: "))
  #registar frutas 
  if opcion == 1:
    cantidad = int(input("Ingrese la cantidad de frutas: "))
    for fruta in range(cantidad):
      frutas={}
      frutas["nombre"] = input("ingrese el nombre de la fruta: ")
      frutas["id"] = input("ingrese el id: ")
      frutas["precio"] = int(input("ingrese el precio unitario: "))
      frutas["cantidad"] = int(input("ingrese la cantidad: "))
      salpicon.append(frutas)
      
  elif opcion==2 :
    #costo total salpicon
    precioSalpicon = 0
    for fruta in salpicon:
      precioFruta = (fruta['cantidad']*(fruta['precio']))
      precioSalpicon += precioFruta
    print ("El precio total del salpicon es: ", precioSalpicon)
      
  elif opcion == 3:
    #mostrar frutas por precio de mayor a menor 
    ordenar = sorted(salpicon, key=lambda x: x["precio"], reverse=True)
    for fruta in ordenar:
        print(f"Nombre: {fruta['nombre']}, Precio: {fruta['precio']}")

    #mostrar cual es la fruta mas cara, y la mas barata    
  elif opcion == 4:
    maximo = max(salpicon, key=lambda x: x["precio"])
    minimo =  min(salpicon, key=lambda x: x["precio"])

    print (f"Fruta mas cara: ", maximo['nombre'], "Fruta mas barata: ", minimo['nombre'])