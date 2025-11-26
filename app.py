import streamlit as st
import pandas as pd
from db import get_definicions, insert_definicion, delete_definicion

# Vistas
from metodos_numericos import metodos_numericos
from metodos_numericos_dos import metodos_numericos_dos

# CONFIG
st.set_page_config(page_title="Diccionario", layout="wide")

# =========================
# ESTILOS (solo apariencia)
# =========================
st.markdown("""
    <style>
        /* Contenedor de tarjetas */
        .card {
            background-color: #1e1e1e;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #3a3a3a;
            margin-bottom: 15px;
        }
        .titulo {
            font-size: 22px;
            font-weight: bold;
            color: #4ca3ff;
        }
        .defin {
            font-size: 16px;
            color: #ffffff;
            margin-top: 8px;
        }
        .stTextInput>div>div>input {
            background-color: #111;
            color: white;
        }
        .stTextArea textarea {
            background-color: #111;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "Navegación",
    ["Diccionario", "Agregar", "Eliminar", "Métodos Numéricos I", "Métodos Numéricos II"]
)

st.title("📘 Diccionario de Métodos Numéricos")

# Cargar datos
data = get_definicions()
df = pd.DataFrame(data, columns=["id", "termino", "definicion"])

# =========================
# DICCIONARIO / BUSCAR
# =========================
if menu == "Diccionario":
    st.subheader("Buscar término")
    buscar = st.text_input("Escribe algo para buscar:")

    filtrado = data
    if buscar:
        filtrado = [
            x for x in data
            if buscar.lower() in x["termino"].lower()
            or buscar.lower() in x["definicion"].lower()
        ]

    # Render bonito tipo "cards"
    for item in filtrado:
        st.markdown(
            f"""
            <div class="card">
                <div class="titulo">{item['termino']}</div>
                <div class="defin">{item['definicion']}</div>
                <small style="color:#888;">ID: {item['id']}</small>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================
# AGREGAR / EDITAR
# =========================
elif menu == "Agregar":
    st.subheader("Agregar o actualizar término")

    col1, col2 = st.columns([2, 3])
    with col1:
        t = st.text_input("Término:")
    with col2:
        d = st.text_area("Definición:", height=150)

    if st.button("Guardar", use_container_width=True):
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
        st.dataframe(df, use_container_width=True)

        id_borrar = st.number_input("ID a borrar", min_value=1, step=1)

        if st.button("Eliminar", use_container_width=True):
            delete_definicion(id_borrar)
            st.warning("Elemento eliminado.")
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




