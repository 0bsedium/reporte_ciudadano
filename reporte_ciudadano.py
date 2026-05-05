# Vas a desarrollar un sistema en Python que permita a ciudadanos reportar incidentes (ej:
# luminarias dañadas, basura, ruidos molestos).

# Permita ingresar los siguientes datos:
# o Nombre del ciudadano
# o Correo electrónico
# o Tipo de incidente
# o Descripción
# o Ubicación
# Aplique:
# o Sanitización de todos los campos
# o Validaciones básicas (correo válido, texto limpio, etc.)
# Proteja los datos:
# o El nombre NO debe guardarse directamente
# o El correo debe anonimizarse
# o Se debe generar un ID único del reporte
# Almacene los reportes en una lista (simulación de base de datos)
# Permita mostrar los reportes registrados

import re, uuid

# arreglo para reclamos  ingresados
caja_reclamos = []
respaldos = []


def sanitizar_nombre(nombre):
    nombre = nombre.strip()
    # replace quita espacios para verificar que solo hayan letras
    # isalpha() devolvemos True si todos los caracteres son letras
    # en este caso busca el " " espacio en blanco y , "" para reemplazarlo con nada, o lo que contenga la segunda comilla
    if nombre.replace(" ", "").isalpha():
        return nombre
    return None

def sanitizar_email(email):
    email = email.strip()
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # re.match (patron de expresion regular que queremos validar)
    if re.match(patron, email):
        return email
    return None

def enmascarar_email(email):
    usuario, dominio = email.split("@")
    return f"{usuario[0]}***@{dominio}"

def sanitizar_tipo(tipo):
    tipo = tipo.lower().capitalize()
    # replace quita espacios para verificar que solo hayan letras
    # isalpha() devolvemos True si todos los caracteres son letras
    # en este caso busca el " " espacio en blanco y , "" para reemplazarlo con nada, o lo que contenga la segunda comilla
    if tipo.replace(" ", "").isalpha():
        return tipo
    return None

def sanitizar_descripcion(descripcion):
    descripcion = descripcion.strip().lower()
    patron = r'^[a-záéíóúüñA-ZÁÉÍÓÚÜÑ0-9\s.,]+$'
    if re.match(patron, descripcion) and len(descripcion) <= 30:
        return descripcion
    return None

def sanitizar_ubicacion(ubicacion):
    ubicacion = ubicacion.strip().lower()
    # replace quita espacios para verificar que solo hayan letras
    # isalpha() devolvemos True si todos los caracteres son letras
    # en este caso busca el " " espacio en blanco y , "" para reemplazarlo con nada, o lo que contenga la segunda comilla
    patron = r'^[a-záéíóúüñA-ZÁÉÍÓÚÜÑ0-9\s.,]+$'
    if re.match(patron, ubicacion):
        return ubicacion
    return None

# seudonimos para la variable que le pida
def seudonimizar(prefijo="ANON"):
    return f"{prefijo}_" + str(uuid.uuid4())[:8]

def registrar_reclamo(nombre, email, tipo, descripcion, ubicacion):
    nombre_valido = sanitizar_nombre(nombre)
    email_valido = sanitizar_email(email)
    tipo_valido = sanitizar_tipo(tipo)
    descripcion_valida = sanitizar_descripcion(descripcion)
    ubicacion_valida = sanitizar_ubicacion(ubicacion)

    if not all([nombre_valido, email_valido, tipo_valido, descripcion_valida, ubicacion_valida]):
        print("Datos inválidos, registro rechazado.")
        return  # <-- faltaba esto

    id_reclamo = str(uuid.uuid4())[:8]  # solo identificador, sin seudonimizar

    reclamo = {
     "usuario": seudonimizar("USUARIO"),  # nombre anonimizado directo
     "email": seudonimizar("EMAIL"),      # email anonimizado directo
     "tipo": tipo_valido,
     "descripcion": descripcion_valida,
     "ubicacion": ubicacion_valida,
     "id_reclamo": id_reclamo
    }

    respaldo = {
     "nombre_real": nombre_valido,
     "email_real": email_valido,
     "id_reclamo": id_reclamo  # para cruzar si necesitas recuperar datos reales
    }

    caja_reclamos.append(reclamo)
    respaldos.append(respaldo)
    print("Reclamo ingresado. ID:", id_reclamo)


while True:
    print("""
    =============== Sistema de reclamos ciudadanos =========|
    | 1. Registrar reclamo                                   |
    | 2. Mostrar reclamos                                    |
    | 3. Salir                                               |
    |========================================================|
    """)

    respuesta = input("Ingrese la opcion deseada (1-3): ")

    if respuesta == "1":
        nombre      = input("Nombre: ")
        email       = input("Email: ")
        tipo        = input("Tipo de incidente: ")
        descripcion = input("Descripcion (max 30 caracteres): ")
        ubicacion   = input("Ubicacion: ")
        registrar_reclamo(nombre, email, tipo, descripcion, ubicacion)

    elif respuesta == "2":
        if not caja_reclamos:
            print("No hay reclamos registrados.")
        else:
            for r in caja_reclamos:
                email_real = next(x["email_real"] for x in respaldos if x["id_reclamo"] == r["id_reclamo"])
                print(f"""
    ID:          {r["id_reclamo"]}
    Email:       {enmascarar_email(email_real)}
    Tipo:        {r["tipo"]}
    Descripcion: {r["descripcion"]}
    Ubicacion:   {r["ubicacion"]}
    {"-"*40}""")

    elif respuesta == "3":
        print("Saliendo...")
        break

    else:
        print("Opcion no válida.")