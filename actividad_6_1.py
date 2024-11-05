#mi_archivo = open('texto.txt')

#print(mi_archivo.read())

# una_linea= mi_archivo.readline()
# print(una_linea)

#  

# una_linea= mi_archivo.readline()
# print(una_linea.splitlines())

# for l in mi_archivo:
#     print("Aqui dice: "+l)

# todas = mi_archivo.readlines()
# print(todas)
# todas = todas.pop()
# print(todas)

# mi_archivo.close()



# Práctica Abrir y Manipular Archivos 1
# Abre el archivo texto.txt e imprime su contenido.

# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
# archivo = open('texto.txt',"r")
# print(archivo.read())
# archivo.close()

# Práctica Abrir y Manipular Archivos 2
# Imprime la primera línea del archivo texto.txt

# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
# archivo = open('texto.txt')
# primer_linea= archivo.readline()
# print(primer_linea.strip())
# archivo.close()

# Práctica Abrir y Manipular Archivos 3
# Abre el archivo texto.txt e imprime únicamente la segunda línea.
 
# segunda_linea= archivo.readline()
# print(una_linea.splitlines())

#-----------------------------------------------------


# archivo = open('prueba.txt','r')
# archivo = open('prueba_nueva.txt','w')
# archivo = open('prueba.txt')
# archivo.write('hola\n')
# archivo.write('mundo')

# archivo.write('''hola 
#               mundo
#               soy 
#               programador de
#               python''')

# archivo.writelines(['hola','como','estas','?'])
# archivo.write('mundo')

# archivo = open('prueba.txt','a') 
# archivo.write("esta va a ser la ultima linea")
# archivo.close()



# Práctica Crear y Escribir Archivos 1
# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
# archivo = open("mi_archivo.txt","w")
# archivo.write("nuevo texto")
# archivo = open("mi_archivo.txt","r")
# print(archivo.read())



# Práctica Crear y Escribir Archivos 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

# Imprime el contenido completo de "mi_archivo.txt" al finalizar.

# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
#archivo = open("mi_archivo.txt","w")


# archivo = open("mi_archivo.txt","a")
# archivo.write("nuevo inicio de sesion")
# archivo = open("mi_archivo.txt","r")
# print(archivo.read())

 



# Práctica Crear y Escribir Archivos 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Imprime el contenido completo de "registro.txt" al finalizar.

# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt","a")
archivo.writelines([f"{item}\t" for item in registro_ultima_sesion])
archivo.write("\n")
archivo = open("registro.txt","r")
print(archivo.read())