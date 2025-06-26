import sqlite3
from flask import Flask, request, redirect, jsonify
from hashlib import md5
import validators

DB_PATH = "url_shortener.db"

# ——— Helpers para SQLite ———
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS mapping (
            hash TEXT PRIMARY KEY,
            url  TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()

# ——— Configuración de la app ———
app = Flask(__name__)
init_db()

# ——— Endpoint para acortar URLs ———
@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json() or {}
    url  = data.get("url")
    if not url:
        return jsonify(error="Missing 'url' parameter"), 400

    # 1) Validación de la URL
    if not validators.url(url):
        return jsonify(error="Invalid URL"), 400

    # 2) Generar hash corto (5 chars)
    token = md5(url.encode()).hexdigest()[:5]

    db = get_db()
    try:
        # 3) Intentar insert; si choca, manejar colisión
        db.execute(
            "INSERT INTO mapping (hash, url) VALUES (?, ?)",
            (token, url)
        )
        db.commit()

    except sqlite3.IntegrityError:
        # Ya existe ese token
        existing = db.execute(
            "SELECT url FROM mapping WHERE hash = ?",
            (token,)
        ).fetchone()["url"]

        if existing == url:
            # Mismo par URL–hash, devolvemos sin error
            pass
        else:
            # Colisión: alargar a 8 chars y reintentar
            token = md5(url.encode()).hexdigest()[:8]
            try:
                db.execute(
                    "INSERT INTO mapping (hash, url) VALUES (?, ?)",
                    (token, url)
                )
                db.commit()
            except sqlite3.IntegrityError:
                db.close()
                return jsonify(error="Hash collision, please retry"), 500

    db.close()
    return jsonify(short_url=f"/r/{token}"), 201

# ——— Endpoint para redireccionar ———
@app.route("/r/<token>")
def redirect_short(token):
    db  = get_db()
    row = db.execute(
        "SELECT url FROM mapping WHERE hash = ?",
        (token,)
    ).fetchone()
    db.close()

    if not row:
        return "URL not found", 404

    return redirect(row["url"])

if __name__ == "__main__":
    app.run(debug=True)