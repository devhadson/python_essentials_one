# Pregunta 1: ¿Cuál es la salida del siguiente programa?
print("Mi\nnombre\nes\nParedes.", end=" ")
print("Hadson Paredes.")

# Pregunta 2: ¿Cuál es la salida del siguiente programa?
print(sep="&", "fish", "chips")

'''
File "main.py", line 1
    print(sep="&", "fish", "chips")
                  ^
SyntaxError: positional argument follows keyword argument
Recuerda: Los argumentos de palabras clave deben pasarse después de cualquier argumento posicional requerido
'''
#Pregunta 3: ¿Cuál de las siguientes print() invocaciones de función generarán un SyntaxError?

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')
      
'''La línea 5 generará un SyntaxError, porque el símbolo ' en la cadena Greg's book. requiere un carácter de escape.'''