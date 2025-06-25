import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración
MAX_PETICIONES = 60      # Límite por IP
VENTANA_SEGUNDOS = 60    # Tamaño de la ventana

# Diccionario para registrar las IPs y sus contadores
registro = {}  # clave: IP → [inicio_ventana, conteo]

@app.route("/recurso")
def recurso_protegido():
    ip = request.remote_addr
    ahora = time.time()

    if ip not in registro:
        registro[ip] = [ahora, 1]
    else:
        inicio, cuenta = registro[ip]
        if ahora - inicio > VENTANA_SEGUNDOS:
            # Reiniciamos ventana y contador
            registro[ip] = [ahora, 1]
        else:
            if cuenta >= MAX_PETICIONES:
                return jsonify({"error": "Demasiadas peticiones"}), 429
            registro[ip][1] += 1

    return jsonify({"mensaje": "Petición aceptada"})

if __name__ == "__main__":
    app.run(debug=True)
