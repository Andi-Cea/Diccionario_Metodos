import streamlit as st
from datos import get_definicions

def app():
    st.title("📘 Ejercicios y ejemplos")

    # Cargar términos
    rows = get_definicions()
    terminos = [r[1] for r in rows]

    if not terminos:
        st.warning("No hay términos en el diccionario.")
        return

    # Seleccionar término
    termino = st.selectbox("Selecciona un término", terminos)

    # Ejercicio básico
    ejercicios_base = {
        "Interpolación": "Construye un polinomio interpolante para los puntos (1,2), (2,3), (3,5).",
        "Trapecio": "Aproxima ∫(0→2) (x² + 1) dx usando la regla del trapecio con n=4.",
        "Simpson": "Usa Simpson para aproximar ∫(1→3) ln(x) dx con n=4.",
        "Newton": "Aplica Newton para encontrar la raíz de f(x)=x³−2x−5 con x₀=2.",
        "Bisección": "Encuentra una raíz de f(x)=e^x−3 usando bisección en [0,2]."
    }

    ejercicio = ejercicios_base.get(termino, f"Explica qué significa **{termino}** y da un ejemplo práctico.")

    st.markdown("---")
    st.subheader(f"Ejercicio sobre **{termino}**")
    st.write(ejercicio)

    st.markdown("---")
    st.subheader("Tu solución")
    st.text_area("Escribe tu razonamiento o solución:", height=150)

    if st.button("Guardar respuesta"):
        st.success("Respuesta guardada (no realmente 😄).")
