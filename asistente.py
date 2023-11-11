nombre = input("Escribe el nombre: ")
p = nombre.split()
contador = p.count("Alexa")

if contador == 1:
    print("Dime cómo puedo ayudarte?")
elif contador > 1:
    print("¡Tranquilo, solo di mi nombre una vez!")
