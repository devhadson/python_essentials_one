#_______________argumento end=""____________________________
print("Mi nombre es", "Hadson.", end=" ")
print("Learning Python.")

#Si miras con atención, verás que hemos usado el argumento end, pero la cadena que se le asignó está vacía (no contiene ningún carácter).
print("Mi nombre es ", end="")
print("Learning Python.")

#Conclusión end="": La cadena asignada al argumento de palabra clave end puede ser de cualquier longitud.

#_______________argumento sep=""____________________________
# El argumento de palabra clave que puede hacer esto se denomina sep (como en separador).

print("Mi", "nombre", "es", "Hadson.", sep="-")
print("Mi", "nombre", "es", "Hadson.", sep=" ")

#Ambos argumentos de palabra clave pueden mezclarse en una invocación, como aquí en la ventana del editor.
print("Mi", "nombre", "es", "Hadson.", sep="_", end="*")
print("Learning", "Python", "para", "Inteligencia Artificial", sep="*", end="*\n")