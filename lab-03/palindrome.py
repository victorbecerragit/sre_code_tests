
# Versión sencilla usando slice
# y comprensión de listas

def es_palindromo(palabras):
    """
    Toma una lista de palabras y devuelve dos listas:
    - palindromas: las que sí son palíndromos
    - no_palindromas: las que no lo son
    """
    palindromas = []
    no_palindromas = []

    for palabra in palabras:
        txt = palabra.strip().lower()  # Normaliza: trim, minúsculas
        # Comprueba si es igual al revés y añade a la lista correspondiente si es palíndromo o no
        if txt == txt[::-1]:
            palindromas.append(palabra)
        else:
            no_palindromas.append(palabra)

    return palindromas, no_palindromas


# Ejemplo de uso
palabras = ["abajaba", "pepito", "vegetal", "rodador", "somos", "seres", "luz"]
pal, no_pal = es_palindromo(palabras)

print("Palíndromas:", pal)
print("No palíndromas:", no_pal)
