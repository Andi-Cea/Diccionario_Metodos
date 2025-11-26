import streamlit as st
import pandas as pd
from db import get_definicions, insert_definicion, delete_definicion

# Vistas
from metodos_numericos import metodos_numericos
from metodos_numericos_dos import metodos_numericos_dos

st.set_page_config(page_title="Diccionario  ", layout="centered")

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "Navegación",
    ["Diccionario", "Agregar", "Eliminar", "Métodos Numéricos I", "Métodos Numéricos II"]
)

st.title("📘 Diccionario de Métodos Numéricos ( )")

# Cargar datos
data = get_definicions()
df = pd.DataFrame(data)

# =========================
# DICCIONARIO / BUSCAR
# =========================
if menu == "Diccionario":
    st.subheader("Buscar término")
    buscar = st.text_input("Escribe algo para buscar:")

    if buscar:
        filtrado = [
            x for x in data
            if buscar.lower() in x["termino"].lower()
            or buscar.lower() in x["definicion"].lower()
        ]
        st.dataframe(pd.DataFrame(filtrado))
    else:
        st.dataframe(df)

# =========================
# AGREGAR / EDITAR
# =========================
elif menu == "Agregar":
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
elif menu == "Eliminar":
    st.subheader("Eliminar término")

    if not df.empty:
        st.dataframe(df)

        id_borrar = st.number_input("ID a borrar", min_value=1, step=1)

        if st.button("Eliminar"):
            delete_definicion(id_borrar)
            st.warning("Eliminado.")
            st.rerun()
    else:
        st.info("No hay datos para eliminar.")

# =========================
# MÉTODOS NUMÉRICOS I
# =========================
elif menu == "Métodos Numéricos I":
    metodos_numericos.app()

# =========================
# MÉTODOS NUMÉRICOS II
# =========================
elif menu == "Métodos Numéricos II":
    metodos_numericos_dos.app()



