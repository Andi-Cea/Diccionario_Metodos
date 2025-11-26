import psycopg2
import os
from dotenv import load_dotenv

# Cargar .env si existe
load_dotenv()

# Leer configuración desde variables de entorno o usar valores por defecto
CONN = {
    "dbname": os.getenv("PGDATABASE", "postgres"),
    "user": os.getenv("PGUSER", "postgres"),
    "password": os.getenv("PGPASSWORD", "1234"),
    "host": os.getenv("PGHOST", "localhost"),
    "port": os.getenv("PGPORT", "5432")
}

def get_connection():
    return psycopg2.connect(**CONN)

# ===========================================
# CREAR TABLA (conceptos)
# ===========================================
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS conceptos (
            id SERIAL PRIMARY KEY,
            termino TEXT UNIQUE NOT NULL,
            definicion TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# ===========================================
# INSERTAR / UPSERT
# ===========================================
def insert_definicion(termino, definicion):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO conceptos (termino, definicion)
        VALUES (%s, %s)
        ON CONFLICT (termino) DO UPDATE
        SET definicion = EXCLUDED.definicion;
    """, (termino, definicion))
    conn.commit()
    cur.close()
    conn.close()

# ===========================================
# OBTENER TODAS LAS DEFINICIONES
# ===========================================
def get_definicions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, termino, definicion FROM conceptos ORDER BY termino ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# ===========================================
# ELIMINAR DEFINICIÓN POR TÉRMINO
# ===========================================
def delete_definicion(termino):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM conceptos WHERE termino = %s;", (termino,))
    conn.commit()
    cur.close()
    conn.close()

# ===========================================
# ACTUALIZAR DEFINICIÓN POR TÉRMINO
# ===========================================
def update_definicion(termino, definicion):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE conceptos
        SET definicion = %s
        WHERE termino = %s;
    """, (definicion, termino))
    conn.commit()
    cur.close()
    conn.close()

