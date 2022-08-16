datos = {"codigo": ["001", "002", "003", "004", "005"],
          "nombre": ["Daniel", "Lucas", "Mateo", "Carlos", "Mario"],
         "curso": ["Diseño Web 1", "Algoritmo 2", "Desarrollo Personal 3", "Laboratorio 4","Soporte TI 5"]}
nota_ = []
respuesta = "s"
while respuesta == "s":
    codigo = input("Ingresar el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    notan1 = int(input("Ingrese la primera nota del alumno: "))
    notan2 = int(input("Ingrese la segunda nota del alumno: "))
    notan3 = int(input("Ingrese la tercera nota del alumno: "))
    notan4 = int(input("Ingrese la cuarta nota del alumno: "))
    x = 0
    for i in datos["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = datos["nombre"][x]
            porcentaje = (notan1 + notan2 + notan3 + notan4)/4
            lista = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Promedio: " + str(porcentaje) + " | " +"Nota 1: " + str(notan1) + "| " + "Nota 2: " + str(notan2) + " | " + "Nota 3: " + str(notan3) + " | " + "Nota 4: " + str(notan4)]
            f = open("examen_final.txt", "a")
            cadena = "".join(lista)
            f.write("\n" + cadena)
            f.close()
        x += 1
    respuesta = input("¿Desea seguir?s/n: ")
    f = open("examen_final.txt")
    print(f.read())
    f.close()