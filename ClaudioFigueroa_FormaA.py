diccionario = {
    "usuarios" : []
}

def validar_opcion():
    while True:
        try:
            print("MENU PRINCIPAL")
            print("[1] Ingresar usuario.")
            print("[2] Buscar usuario.")
            print("[3] Eliminar usuario.")
            print("[4] Salir.")

            opcion = int(input("Ingrese opción: "))

            if opcion < 1:
                print("Ingrese un número entero mayor que 0.\n")
            else:
                return opcion

        except Exception:
            print("Ingrese como opción un número entero.\n")

def lista_de_nombres(diccionario_a_iterar):
    lista = []
    if len(diccionario_a_iterar) != 0:
        for i in diccionario_a_iterar:
            lista.append(i["nombre"])
    return lista

def ingresar_nombre(mensaje):
     while True:
        nombre = input(mensaje)
        if nombre in lista_nombres:
            print("El usuario ya se encuentra registrado. Pruebe con otro nombre.")
        else:
            return nombre

def ingresar_sexo(mensaje):
    while True:
        sexo = input(mensaje)
        if (sexo != "M") and (sexo != "F"):
            print("Debe ingresar M o F solamente. Intente de nuevo.")
        else:
            return sexo
    
def ingresar_contrasena(mensaje):
    while True:
        contrasena = input(mensaje)
        if (len(contrasena) < 8) or (" " in contrasena):
            print("Contraseña no válida. Intente otra.")
        else:
            print("Contraseña válida.")
            return contrasena

def ingresar_usuario(nombre, sexo, contrasena):
    usuario = {
            "nombre": nombre,
            "sexo": sexo,
            "contraseña": contrasena
        }
    
    diccionario["usuarios"].append(usuario)

    print("Usuario ingresado con éxito!!\n")

def recuperar_indice(lista,nombre):
    if nombre in lista:
        i = 0
        while i < len(diccionario["usuarios"]):
            if nombre == diccionario["usuarios"][i]["nombre"]:
                indice = i
                return indice
            else:
                i += 1

def buscar_usuario(lista,nombre):
    if nombre in lista:
        indice = recuperar_indice(lista,nombre)
        print(f"El sexo del usuario es: {diccionario["usuarios"][indice]["sexo"]} y la contraseña es: {diccionario['usuarios'][indice]["contraseña"]}\n")
    else:
        print("El usuario no se encuentra.\n")

def eliminar_usuario(lista,nombre):
    if nombre in lista:
        indice = recuperar_indice(lista,nombre)
        diccionario["usuarios"].remove(diccionario["usuarios"][indice])
        print("Usuario eliminado con éxito!\n")
    else:
        print("No se pudo eliminar usuario!\n")


#Main o código principal

while True:
    
    opcion = validar_opcion()

    if opcion == 1:
        lista_nombres = lista_de_nombres(diccionario["usuarios"])
        nombre = ingresar_nombre("Ingrese nombre de usuario: ")
        sexo = ingresar_sexo("Ingrese sexo (M/F): ")
        contrasena = ingresar_contrasena("Ingrese contraseña: ")
        ingresar_usuario(nombre, sexo, contrasena)

    elif opcion == 2:
        lista_nombres = lista_de_nombres(diccionario["usuarios"])
        if len(lista_nombres) == 0:
            print("No hay usuarios registrados.\n")
        else:
            nombre = input("Ingrese usuario a buscar: ")
            buscar_usuario(lista_nombres,nombre)

    elif opcion == 3:
        lista_nombres = lista_de_nombres(diccionario["usuarios"])
        if len(lista_nombres) == 0:
            print("No hay usuarios registrados.\n")
        else:
            nombre = input("Ingrese usuario a buscar: ")
            eliminar_usuario(lista_nombres,nombre)

    elif opcion == 4:
        print("Programa terminado...")
        break
    
    else:
        print("Debe ingresar una opción válida!!\n")