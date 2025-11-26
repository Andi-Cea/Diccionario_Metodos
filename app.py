import streamlit as st
import pandas as pd
from db import get_definicions, insert_definicion, delete_definicion

st.set_page_config(page_title="Diccionario Local", layout="centered")

st.title("📘 Diccionario de Métodos Numéricos (Local)")

# =========================
# BUSCADOR
# =========================
st.subheader("Buscar término")

buscar = st.text_input("Escribe algo para buscar:")

data = get_definicions()

if buscar:
    filtrado = [x for x in data if buscar.lower() in x["termino"].lower()]
else:
    filtrado = data

st.dataframe(pd.DataFrame(filtrado))

# =========================
# AGREGAR / ACTUALIZAR
# =========================
st.subheader("Agregar o actualizar término")

t = st.text_input("Término:")
d = st.text_area("Definición:")

if st.button("Guardar"):
    if t.strip() and d.strip():
        insert_definicion(t, d)
        st.success("Guardado correctamente.")
        st.rerun()
    else:
        st.error("Completa ambos campos.")

# =========================
# ELIMINAR
# =========================
st.subheader("Eliminar término")

id_borrar = st.number_input("ID a borrar", min_value=1, step=1)

if st.button("Eliminar"):
    delete_definicion(id_borrar)
    st.warning("Eliminado.")
    st.rerun()


