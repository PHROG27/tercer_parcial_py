lecturas = int(input("¿Cuántas lecturas de temperatura tienes? "))
c = 0
temperatura = 0
fuera_de_rango = 0

while c < lecturas:
      c += 1
      temperatura = float(input("Escribe la temperatura: "))
      if temperatura >= 10 and temperatura <= 40:
          pass
      else:
          fuera_de_rango += 1

print("Número de lecturas fuera del rango:", fuera_de_rango)
po = (fuera_de_rango * 100) / lecturas
print("Porcentaje de lecturas fuera del rango:", po)
