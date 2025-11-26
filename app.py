import streamlit as st
import pandas as pd
from db import get_definicions, insert_definicion, delete_definicion

# Importar vistas
from metodos_numericos import metodos_numericos
from metodos_numericos_dos import metodos_numericos_dos

# Configuración general
st.set_page_config(page_title="Diccionario Local", layout="centered")

# ============ MENÚ LATERAL ============
menu = st.sidebar.radio(
    "Navegación",
    ["Diccionario", "Métodos Numéricos I", "Métodos Numéricos II"]
)

st.title("📘 Diccionario de Métodos Numéricos (Local)")

# ======================================
#      DICCIONARIO (LOCAL JSON)
# ======================================

if menu == "Diccionario":

    sub = st.radio(
        "Selecciona una sección:",
        ["Buscar", "Agregar / Editar", "Eliminar", "Ver todos"]
    )

    data = get_definicions()

    # ------- BUSCAR -------
    if sub == "Buscar":
        st.subheader("Buscar término")

        buscar = st.text_input("Escribe algo para buscar:")

        if buscar:
            filtrado = [
                x for x in data
                if buscar.lower() in x["termino"].lower() 
                or buscar.lower() in x["definicion"].lower()
            ]
        else:
            filtrado = data

        if filtrado:
            st.dataframe(pd.DataFrame(filtrado))
        else:
            st.info("No se encontraron resultados.")

    # ------- AGREGAR / EDITAR -------
    elif sub == "Agregar / Editar":
        st.subheader("Agregar o actualizar término")

        t = st.text_input("Término:")
        d = st.text_area("Definición:")

        if st.button("Guardar"):
            if t.strip() and d.strip():
                insert_definicion(t, d)
                st.success(f"'{t}' guardado correctamente.")
                st.rerun()
            else:
                st.error("Completa ambos campos.")

    # ------- ELIMINAR -------
    elif sub == "Eliminar":
        st.subheader("Eliminar término")

        df = pd.DataFrame(data)
        if not df.empty:
            st.dataframe(df)

            id_borrar = st.number_input("ID a borrar", min_value=1, step=1)
            if st.button("Eliminar"):
                delete_definicion(id_borrar)
                st.warning("Eliminado correctamente.")
                st.rerun()
        else:
            st.info("No hay datos para eliminar.")

    # ------- VER TODO -------
    elif sub == "Ver todos":
        st.subheader("Todos los términos")
        df = pd.DataFrame(data)

        if not df.empty:
            st.dataframe(df)
        else:
            st.info("Aún no hay términos registrados.")


# ======================================
#      MÉTODOS NUMÉRICOS I
# ======================================
elif menu == "Métodos Numéricos I":
    metodos_numericos.app()


# ======================================
#      MÉTODOS NUMÉRICOS II
# ======================================
elif menu == "Métodos Numéricos II":
    metodos_numericos_dos.app()


