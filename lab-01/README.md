
Como seria el pseudocodigo para el siguiente problema: 

Dada una lista de dominios publicos de internet, 
agregar el protocolo https:// en los que falte, verificar si el dominio esta activo o no existe.


www.google.com , news.ycombinator.com , example.net , https://www.programmax.net/


# Pseudocodigo 

```yaml

#
# Lista inicial de dominios
dominios ← [
  "www.google.com",
  "news.ycombinator.com",
  "example.net",
  "https://www.programmax.net/"
]

# Función principal
función procesarDominios(listaDeDominios):
    para cada dominio en listaDeDominios:
        url ← normalizarProtocolo(dominio)
        estado ← verificarDominioActivo(url)
        imprimir(url + " → " + estado)
    fin para
fin función

# Asegura que la URL arranque con https:// (o http:// si prefieres)
función normalizarProtocolo(dominio):
    si dominio comienzaCon("http://") o dominio comienzaCon("https://"):
        retornar dominio
    sino:
        retornar "https://" + dominio
    fin si
fin función

# Verifica si el dominio/URL responde
función verificarDominioActivo(url):
    tratar:
        respuesta ← hacerPeticionHEAD(url)
        si respuesta.codigoHTTP ≥ 200 y respuesta.codigoHTTP < 400:
            retornar "ACTIVO (" + respuesta.codigoHTTP + ")"
        sino:
            retornar "NO DISPONIBLE (" + respuesta.codigoHTTP + ")"
        fin si
    capturar excepción:
        # Timeout, DNS no existe, certificado inválido, etc.
        retornar "NO EXISTE / ERROR"
    fin tratar
fin función

# Simula una petición HTTP de tipo HEAD
función hacerPeticionHEAD(url):
    # Aquí tu librería HTTP preferida debe:
    # - Enviar un HEAD (o GET ligero)
    # - Esperar un timeout corto (p.ej. 3s)
    # - Devolver un objeto { códigoHTTP, encabezados }
    # Si falla (host no existe, timeouts, SSL), lanzar excepción.
fin función

# Ejecutamos
procesarDominios(dominios)

```
