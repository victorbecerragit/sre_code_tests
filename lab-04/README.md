
Adapta el siguiente codigo existente para almacenar los short link generados en una DB.
Actualmente este codigo solo guarda los link en memoria en un diccionario "mapping" y se pierden al reiniciar la aplicacion.

### 
Cómo funciona

# Mapa global que asocia el hash corto con la URL original
mapping ← diccionario vacío

# ──────────────────────────────────────────────────────────────────────────
# Endpoint: POST /shorten
# Recibe JSON con clave "url", genera un hash corto y lo guarda en mapping
# ──────────────────────────────────────────────────────────────────────────
función shorten(request):
    payload ← request.json

    # 1. Validar que venga la URL
    si "url" no está en payload:
        retornar "Missing URL Parameter", 400

    # 2. Calcular MD5 de la URL y truncar a 5 caracteres
    hash_obj ← MD5()
    hash_obj.update(payload["url"].encode())
    digest ← hash_obj.hexdigest()[0:5]

    # 3. Almacenar o informar si ya existe
    si digest no está en mapping:
        mapping[digest] ← payload["url"]
        retornar "Shortened: r/" + digest, 200
    sino:
        # Aquí podríamos chequear colisiones, 
        # pero por simplicidad solo devolvemos el mismo token
        retornar "Already exists: r/" + digest, 200
fin función

# ──────────────────────────────────────────────────────────────────────────
# Endpoint: GET /r/<hash>
# Redirige a la URL almacenada o devuelve 404 si no existe
# ──────────────────────────────────────────────────────────────────────────
función redirect_(hash):
    si hash no está en mapping:
        retornar "URL Not Found", 404
    sino:
        redirigir(mapping[hash])
fin función

# ──────────────────────────────────────────────────────────────────────────
# Inicialización del servidor
# ──────────────────────────────────────────────────────────────────────────
iniciar_servidor():
    registrar_ruta("/shorten", método=POST, manejador=shorten)
    registrar_ruta("/r/<hash>", manejador=redirect_)
    arrancar_app(debug=True)
fin función

# ──────────────────────────────────────────────────────────────────────────
# Punto de entrada
# ──────────────────────────────────────────────────────────────────────────
si __name__ == "__main__":
    iniciar_servidor()

```shell

~/t/sre_code_tests   *…  lab-04  sqlite3 url_shortener.db                                                                                                                   Thu Jun 26 10:18:11 2025
SQLite version 3.45.1 2024-01-30 16:01:20
Enter ".help" for usage hints.
sqlite> .tables
mapping
sqlite> SELECT * from mapping;
a62a4|https://linkedin.com
c57db|https://mail.google.com
sqlite>

```

```yaml

from flask import Flask, redirect, request
from hashlib import md5

app = Flask("url_shortener")

mapping = {}

@app.route("/shorten", methods=["POST"])
def shorten():
    global mapping
    payload = request.json

    if "url" not in payload:
        return "Missing URL Parameter", 400

    # TODO: check if URL is valid

    hash_ = md5()
    hash_.update(payload["url"].encode())
    digest = hash_.hexdigest()[:5]  # limiting to 5 chars. Less the limit more the chances of collission

    if digest not in mapping:
        mapping[digest] = payload["url"]
        return f"Shortened: r/{digest}\n"
    else:
        # TODO: check for hash collission
        return f"Already exists: r/{digest}\n"


@app.route("/r/<hash_>")
def redirect_(hash_):
    if hash_ not in mapping:
        return "URL Not Found", 404
    return redirect(mapping[hash_])


if __name__ == "__main__":
    app.run(debug=True)

```