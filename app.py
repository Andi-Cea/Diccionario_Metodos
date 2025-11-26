import streamlit as st
import pandas as pd
from db import create_table, insert_definicion, get_definicions, delete_definicion, update_definicion

# Importar vistas (si no las usas, simplemente crea archivos vacíos con una función app())
from metodos_numericos import metodos_numericos
from metodos_numericos_dos import metodos_numericos_dos

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Diccionario - PostgreSQL", layout="centered")

# Crear tabla al iniciar
try:
    create_table()
except Exception as e:
    st.error(f"No se pudo crear la tabla: {e}")

# --- MENÚ LATERAL ---
menu = st.sidebar.radio(
    "Selecciona una vista:",
    ["Principal", "Métodos Numéricos I", "Métodos Numéricos II"]
)

# ================== VISTA PRINCIPAL ==================
if menu == "Principal":
    st.title("📘 Diccionario interactivo: Métodos Numéricos")

    # ------------------ BÚSQUEDA ------------------
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("Buscar palabra", value="", placeholder="Escribe una palabra...")
    with col2:
        exact = st.checkbox("Búsqueda exacta", value=False)

    try:
        rows = get_definicions()  # lista de tuplas (id, termino, definicion)
    except Exception as e:
        st.error(f"No se pudieron cargar las definiciones: {e}")
        rows = []

    # Diccionario: termino → (id, definicion)
    data = {r[1]: (r[0], r[2]) for r in rows}

    # ------------------ FUNCIÓN DE BÚSQUEDA ------------------
    def search(q, exact_match):
        q = q.strip().lower()
        if not q:
            return sorted([(k, v[1]) for k, v in data.items()], key=lambda x: x[0].lower())
        if exact_match:
            return [(k, v[1]) for k, v in data.items() if k.lower() == q]
        return [(k, v[1]) for k, v in data.items() if q in k.lower() or q in v[1].lower()]

    results = search(query, exact)

    st.markdown("---")
    st.subheader(f"Resultados ({len(results)})")

    # ------------------ RESULTADOS ------------------
    for palabra, defin in results:
        with st.expander(palabra):
            st.write(defin)

            colA, colB = st.columns(2)

            # ---- EDITAR ----
            with colA:
                if st.button("✏️ Editar", key=f"edit_{palabra}"):
                    st.session_state["edit_word"] = palabra
                    st.session_state["edit_def"] = defin
                    st.rerun()

            # ---- ELIMINAR ----
            with colB:
                if st.button("🗑️ Eliminar", key=f"del_{palabra}"):
                    try:
                        delete_definicion(palabra)
                        st.success(f"'{palabra}' eliminado correctamente.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"No se pudo eliminar: {e}")

    st.markdown("---")

    # ------------------ FORMULARIO AÑADIR / EDITAR ------------------
    st.subheader("Añadir o editar palabra")
    default_word = st.session_state.get("edit_word", "")
    default_def = st.session_state.get("edit_def", "")

    with st.form("form_add"):
        word = st.text_input("Palabra", value=default_word)
        definition = st.text_area("Definición", value=default_def, height=150)
        submitted = st.form_submit_button("Guardar")

    if submitted:
        word = word.strip()
        definition = definition.strip()

        if not word:
            st.error("La palabra no puede estar vacía.")
        else:
            try:
                if word in data:  # actualizar
                    update_definicion(word, definition)
                    st.success(f"'{word}' actualizado correctamente.")
                else:  # insertar
                    insert_definicion(word, definition)
                    st.success(f"'{word}' agregado correctamente.")

                # Si renombraste, eliminar el término anterior
                original = st.session_state.get("edit_word")
                if original and original != word:
                    try:
                        delete_definicion(original)
                    except:
                        pass

                # limpiar estado de edición
                if "edit_word" in st.session_state:
                    del st.session_state["edit_word"]
                if "edit_def" in st.session_state:
                    del st.session_state["edit_def"]

                st.rerun()

            except Exception as e:
                st.error(f"No se pudo guardar la palabra: {e}")

    # ------------------ TABLA COMPLETA ------------------
    if st.checkbox("Mostrar tabla completa"):
        if rows:
            df = pd.DataFrame(rows, columns=["ID", "Palabra", "Definición"])
            st.dataframe(df, use_container_width=True)


# ================== OTRAS VISTAS ==================
elif menu == "Métodos Numéricos I":
    metodos_numericos.app()

elif menu == "Métodos Numéricos II":
    metodos_numericos_dos.app()
