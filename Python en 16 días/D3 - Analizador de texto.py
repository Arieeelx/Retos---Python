texto = input("Ingresar un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower()) #SE GUARDARÁ EN EL INDICE 0
letras.append(input("Ingresa la segunda letra: ").lower()) #SE GUARDARÁ EN EL INDICE 1
letras.append(input("Ingresa la tercera letra: ").lower()) #SE GUARDARÁ EN EL INDICE 2

print("\nCANTIDAD DE LETRAS")

cantidadLetras1 = texto.count(letras[0])
cantidadLetras2 = texto.count(letras[1])
cantidadLetras3 = texto.count(letras[2])

print(f"Cantidad de veces que se repite la letra '{letras[0]}': {cantidadLetras1}\n"
      f"Cantidad de veces que se repite la letra '{letras[1]}': {cantidadLetras2}\n"
      f"Cantidad de veces que se repite la letra '{letras[2]}': {cantidadLetras3}")

print("\nCANTIDAD DE PALABRAS")

palabras = texto.split()
print(f"La cantidad de palabras que hay en el texto es de: {len(palabras)}")

print("\nLETRAS DE INICIO Y DE FIN")

letraInicio = texto[0]
letraFinal = texto[-3]
print(f"La primera letra del texto es '{letraInicio}' y la última letra es '{letraFinal}'")

print("\nTEXTO INVERTIDO")

palabras.reverse()
textoInvertido = ' '.join(palabras)
print(f"Si ordenamos el texto al revés, será: '{textoInvertido}'")

print("\nBUSCANDO LA PALABRA PYTHON")

buscarPalabra = input("Ingresa la palabra a buscar: ")
resultadoPalabra = buscarPalabra in texto
dic = {True:"sí", False:"no"}
print(f"La palabra '{buscarPalabra}', {dic[resultadoPalabra]} se encuentra en el texto.")