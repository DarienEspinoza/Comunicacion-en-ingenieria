archivoAL = open('alumnos.txt', 'a')
archivoCAL = open('calificaciones.txt', 'a')

while True: 
    nombre = input("Escribe el nombre del alumno: ")
    if nombre == "-1":
        break
    archivoAL.write(nombre + '\n')

    calificacion = int(input("Escribe la calificación del alumno: "))
    if calificacion >= 0 and calificacion <= 100:
        archivoCAL.write(str(calificacion) + '\n')
    print()

archivoAL.close()    
archivoCAL.close()    
  

archivoAL = open('alumnos.txt', 'r')
archivoCAL = open('calificaciones.txt', 'r')
archivoLC = open('lista_calificaciones.txt', 'w')

#Escribir en lista calificaciones txt

while True:
    lineaAL = archivoAL.readline().rstrip('\n')
    lineaCAL = archivoCAL.readline().rstrip('\n')
    
    if lineaAL == "" and lineaCAL == "":
        break

    archivoLC.write(lineaAL + ": " + lineaCAL + '\n')

archivoLC.close()
archivoAL.close()
archivoCAL.close()

# Imprimir datos calificaciones txt

archivoLC = open('lista_calificaciones.txt', 'r')
print()
print(" CALIFICACIONES ")
print()

while True: 
    linea = archivoLC.readline()
    if linea == "":
        break
    print(linea)

archivoLC.close()
archivoAL.close()
archivoCAL.close()

#Lista y promedio

archivoCAL = open('calificaciones.txt', 'r')
calificaciones = []
contador = 0

while True:
    calificacion = archivoCAL.readline().rstrip('\n')
    if calificacion == "":
        break
    calificaciones.append(int(calificacion))
    contador += 1

promedio = sum(calificaciones) / contador

print(" PROMEDIO ")
print()
print("El promedio de las calificaciones es : ", promedio)