cliente= str(input("Entra un cliente? (si/no):"))
clientequecompro = 0
contador = 0
totalclientes = 0
nocompraron = 0
quecompraron = 0
varitasauco = 0
varitaespino = 0
varitasauce = 0
varitaacebo = 0
while cliente == "si": 
  c = str(input("Compra algo?  (si/no): "))
  if c == "si":
     clientequecompro += 1
     quecompraron = str(input("Que compro?  Varita de sauco [1] varita de espino [2]  varita de sauce [3]  varita de acebo [4]" ))

     if quecompraron == "1":
       varitasauco += 1
     elif quecompraron == "2":
       varitaespino += 1
     elif quecompraron == "3":
       varitasauce += 1
     elif quecompraron == "4":
       varitaacebo += 1
     cliente = str(input("Entro un cliente? (si/no): "))
     totalclientes += 1
     nocompraron = totalclientes - clientequecompro
     print(f"Los clientes que compraron son {clientequecompro}")
     print(f"Los clientes que no compraron {nocompraron}")
     print(f"El total de clientes es {totalclientes}")
     print(f"Las varitas de sauco son {varitasauco}, las varitas de espino son {varitaespino}, las varitas de sauce son {varitasauce}, las varitas de acebo son {varitaacebo}")
