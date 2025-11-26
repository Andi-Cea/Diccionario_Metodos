import psycopg2
import streamlit as st

DB_URL = st.secrets["DB_URL"]

def get_conn():
    return psycopg2.connect(DB_URL)

def create_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS definicions (
            id SERIAL PRIMARY KEY,
            termino TEXT UNIQUE NOT NULL,
            definicion TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_definicion(termino, definicion):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO definicions (termino, definicion)
        VALUES (%s, %s)
        ON CONFLICT (termino)
        DO UPDATE SET definicion = EXCLUDED.definicion;
    """, (termino, definicion))
    conn.commit()
    cur.close()
    conn.close()

def get_definicions():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, termino, definicion FROM definicions ORDER BY termino;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_definicion(termino, definicion):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE definicions
        SET definicion = %s
        WHERE termino = %s;
    """, (definicion, termino))
    conn.commit()
    cur.close()
    conn.close()

def delete_definicion(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM definicions WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
