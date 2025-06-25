
Dado el siguiente problema genera el pseudocodigo :

De la siguiente lista de palabras, encuentra todas las palabras palindromas (capicua).

abajaba, pepito , vegetal, rodador, somos , seres , luz

###
Cómo funciona
- Se recorta y convierte cada palabra a minúsculas para evitar fallos por mayúsculas o espacios extras.
- La función invertirCadena construye la cadena al revés.
- Si la palabra normalizada coincide con su versión invertida, es palíndromo.


```yaml

# Lista de palabras a analizar
lista ← ["abajaba", "pepito", "vegetal", "rodador", "somos", "seres", "luz"]

# Lista donde guardaremos los palíndromos
palindromos ← []

# Función auxiliar: invierte una cadena
función invertirCadena(cadena):
    invertida ← ""
    para i desde longitud(cadena)−1 hasta 0 paso −1:
        invertida ← invertida + cadena[i]
    fin para
    retornar invertida
fin función

# Procesamiento principal
para cada palabra en lista:
    # 1. Normalizar: quitar espacios y pasar a minúsculas
    original ← minusculas(trim(palabra))
    
    # 2. Invertir la cadena
    invertida ← invertirCadena(original)
    
    # 3. Comparar original vs. invertida
    si original = invertida entonces
        palindromos.agregar(palabra)
    fin si
fin para

# Mostrar resultados
imprimir("Palíndromos encontrados: " + palindromos)


```