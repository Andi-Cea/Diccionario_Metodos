import streamlit as st
from datos import get_definicions  # solo datos, nada de app.py

def app():
    st.title("📘 Ejemplos y Ejercicios")
    st.write("Aquí puedes practicar con ejercicios generados a partir de los términos del diccionario.")

    rows = get_definicions()
    terminos = [r[1] for r in rows]

    if not terminos:
        st.warning("No hay términos registrados en el diccionario.")
        return

    termino = st.selectbox("Selecciona un término para ver un ejercicio:", terminos)

    ejercicios_base = {
        "Interpolación": "Dado el conjunto de puntos (1,2), (2,3), (3,5), construye un polinomio interpolante.",
        "Trapecio": "Aproxima ∫(0→2) (x² + 1) dx usando la regla del trapecio con n = 4.",
        "Simpson": "Usa la regla de Simpson para aproximar ∫(1→3) ln(x) dx con n = 4.",
        "Newton": "Aplica el método de Newton para encontrar la raíz de f(x)=x³−2x−5 con x₀=2.",
        "Bisección": "Encuentra una raíz de f(x)=e^x−3 usando bisección en [0,2]."
    }

    ejercicio_default = f"Explica con tus palabras qué significa **{termino}** y da un ejemplo práctico sencillo."
    ejercicio = ejercicios_base.get(termino, ejercicio_default)

    st.markdown("---")
    st.subheader(f"Ejercicio sobre **{termino}**")
    st.write(ejercicio)

    st.markdown("---")
    st.subheader("Tu solución")
    st.text_area("Escribe aquí tu razonamiento o solución:", height=150)

    if st.button("Guardar respuesta"):
        st.success("Respuesta guardada (no realmente 😄).")
