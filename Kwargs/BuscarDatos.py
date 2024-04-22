def buscar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key", key, "value", value)
        for k, v in value.items():
            print("k", k, "v", v)

# Base de datos de personas
# Base de datos de personas
database = {
    "1": {  # Cambié la clave de 1 a "1"
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    "2": {  # Cambié la clave de 2 a "2"
        "nombre1": "Elio",
        "apellido1": "Anci"
    },
    "3": {  # Cambié la clave de 3 a "3"
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    }
}


# Ejemplo de uso
resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
print(resultado)  # Salida esperada: 1
