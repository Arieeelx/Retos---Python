from collections import Counter
#Ejercicio: FizzBuzz
"""
Descripción:
Escribe una función que imprima los números del 1 al 100, pero con las siguientes condiciones:
Si el número es divisible por 3, imprime "fizz".
Si el número es divisible por 5, imprime "buzz".
Si el número es divisible por ambos (3 y 5), imprime "fizzbuzz".
Si no es divisible ni por 3 ni por 5, imprime el número.
"""
def fizzBuzz():
  for index in range(1, 101):
    if index % 3 == 0 and index % 5 == 0:
      print("fizzbuzz")
    elif index % 3 == 0:
      print("fizz")
    elif index % 5 == 0:
      print("buzz")
    else:
      print(index)
#fizzBuzz

#Desafío: "WoofMeow"
"""
Haz una función que recorra los números del 1 al 100.
Si el número es múltiplo de 4, imprime "woof".
Si el número es múltiplo de 6, imprime "meow".
Si el número es múltiplo de ambos (4 y 6), imprime "woofmeow".
Si no cumple ninguna de esas condiciones, imprime el número.
"""
def woofMeow():
  for i in range(1,101):
    if i % 4 == 0 and i % 6 == 0:
      print("woofmeow")
    elif i % 4 == 0:
      print("woof")
    elif i % 6 == 0:
      print("meow")
    else:
      print(i)
#woofMeow()

#Desafío: "¿Es un anagrama?"
"""
Escribe una función que reciba dos palabras y retorne V o F según sean o no anagramas.
Un anagrama consiste en formar una palabra reordenando TODAS las letras de la palabra inicial.
No hace falta comprobar que ambas palabras existan.
Dos palabras iguales no son anagramas.
"""
def anagrama(palabra1, palabra2):
  palabra1 = palabra1.replace(" ", "").lower()
  palabra2 = palabra2.replace(" ", "").lower()
  if palabra1 == palabra2:
    return False
  elif Counter(palabra1) == Counter(palabra2):
    return True
  else:
    return False
#print(anagrama(input("Ingrese una palabra: "), input("Ingrese otra palabra: ")))

#Desafío: la sucesión de Fibonacci
"""
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando de 0.
- La serie se compone por una sucesión de números en la que el siguiente es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci(x, y):
  lista = []
  for i in range(25):
    lista.append(x)
    lista.append(y)
    x = y + x
    y = x + y
  return lista
"""resultado = fibonacci(
  int(input("Bienvenido a Fibonacci!\n¿Desde qué número comenzamos?\n"
  )), 
  int(input("¿Y el siguiente número?\n"
  ))
  )
print(resultado)
"""
#resultado Fibonacci

#Desafío: ¿Es un número primo?
"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def numPrimos():
  for i in range(2, 101):
    primo = True
    for x in range(2, i):
      if i % x == 0:
        primo = False
      break
    if primo:
      print(f"{i} || Es número primo")
    else:
      print(f"{i} || No lo es")
#numPrimos()