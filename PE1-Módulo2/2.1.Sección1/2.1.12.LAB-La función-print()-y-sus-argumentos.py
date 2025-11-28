'''
Escenario
Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, 
para que se obtenga la salida esperada. Emplea dos funciones print() en el editor.

No cambies nada en la segunda invocación del print().

print("Programming","Essentials","in")
print("Python")

Salida Esperada
Output
Programming***Essentials***in...Python
'''

print("Programming","Essentials","in", sep="***", end="...")
print("Python")