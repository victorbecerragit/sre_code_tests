import requests

# Lista original de dominios
dominios = [
    "www.google.com",
    "news.ycombinator.com",
    "example.net",
    "https://www.programmax.net/"
]

# Asegura que la URL tiene https:// al inicio
def normalizar_protocolo(dominio):
    if dominio.startswith("http://") or dominio.startswith("https://"):
        return dominio
    return "https://" + dominio

# Verifica si el dominio responde con un código válido
def verificar_dominio_activo(url):
    try:
        respuesta = requests.head(url, timeout=3, allow_redirects=True)
        if 200 <= respuesta.status_code < 400:
            return f"ACTIVO ({respuesta.status_code})"
        else:
            return f"NO DISPONIBLE ({respuesta.status_code})"
    except requests.RequestException:
        return "NO EXISTE / ERROR"

# Procesamiento general
for dominio in dominios:
    url = normalizar_protocolo(dominio)
    estado = verificar_dominio_activo(url)
    print(f"{url} → {estado}")
