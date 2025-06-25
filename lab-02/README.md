
Como seria el pseudocodigo para el siguiente problema:

Tengo que analizar el codigo de una aplicacion que genera demasiadas peticiones get cada minuto.
Como crearia un programa para filtrar estas peticiones ?


###
Cómo funciona
- Cada petición llama a manejarGET().
- Si ya pasaron 60 s desde inicioVentana, reseteamos contador y ventana.
- Incrementamos cuenta y, si se pasa de 60, devolvemos un error 429; si no, dejamos pasar la petición.

```yaml

# Parámetros
MAX_PETICIONES ← 60        # máximo GETs permitidos por ventana
VENTANA_SEG ← 60           # tamaño de ventana en segundos

# Variables de estado
cuenta ← 0                 # contador de peticiones en la ventana actual
inicioVentana ← ahora()    # timestamp del inicio de la ventana

# Se ejecuta en cada petición GET
función manejarGET():
    actual ← ahora()

    # Si la ventana de 60s caducó, la reiniciamos
    si actual - inicioVentana ≥ VENTANA_SEG:
        inicioVentana ← actual
        cuenta ← 0
    fin si

    # Contamos y comprobamos
    cuenta ← cuenta + 1
    si cuenta > MAX_PETICIONES:
        devolver BLOQUEAR_CON_429()   # Too Many Requests
    sino:
        devolver PROCESAR_PETICIÓN()
    fin si
fin función


Si quieres el mismo filtro por IP, basta con cambiar cuenta e inicioVentana por un diccionario que use la IP como clave:


mapaContadores ← {}   # clave: IP → { cuenta, inicioVentana }

función manejarGET_porIP(ip):
    si ip no existe en mapaContadores:
        mapaContadores[ip] ← { cuenta:0, inicioVentana:ahora() }

    datos ← mapaContadores[ip]
    # … luego igual al ejemplo global, pero usando datos.cuenta y datos.inicioVentana …

```
