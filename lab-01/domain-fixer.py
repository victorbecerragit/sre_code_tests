import requests
import validators
from flask import jsonify

# domain-fixer.py
# Este script normaliza una lista de dominios, asegurando que tengan el protocolo correcto y
# verifica si están activos o no. Imprime el estado de cada dominio.

# Lista original de dominios
dominios = [
    "www.google.com",
    "news.ycombinator.com",
    "example.net",
    "https://www.programmax.net/",
    "pippo.pepe"
]


# Asegura que la URL tiene https:// al inicio
def normalizar_protocolo(dominio):
    if dominio.startswith("http://") or dominio.startswith("https://"):
        return dominio
    return "https://" + dominio

# Verifica si el dominio responde con un código válido
def verificar_dominio_activo(url):

    if not url:
        return jsonify(error="Missing 'url' parameter"), 400

    # 1) Validación de la URL
    if not validators.url(url):
        return jsonify(error="Invalid URL"), 400
    
    try:
        respuesta = requests.head(url, timeout=5, allow_redirects=True)
        if 200 <= respuesta.status_code <= 400:
            return f"Dominio ACTIVO ({respuesta.status_code})"
        else:
            return f"Dominio NO DISPONIBLE ({respuesta.status_code})"
    except requests.RequestException:
        return "Dominio NO EXISTE / ERROR"

# Procesamiento general
for dominio in dominios:
    url = normalizar_protocolo(dominio)
    estado = verificar_dominio_activo(url)
    print(f"{url} → {estado}")