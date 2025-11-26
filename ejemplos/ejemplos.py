import streamlit as st
import random
import numpy as np
from datos import get_definicions

def app():
    st.title("🎯 Laboratorio Interactivo - Métodos Numéricos")
    
    # Configurar pestañas para diferentes tipos de ejercicios
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Ejercicios Guiados", "🎮 Quiz Rápido", "🧮 Calculadora Numérica", "📊 Visualizaciones"])
    
    with tab1:
        ejercicios_guiados()
    
    with tab2:
        quiz_rapido()
    
    with tab3:
        calculadora_numerica()
    
    with tab4:
        visualizaciones()

def ejercicios_guiados():
    st.header("📝 Ejercicios Guiados por Término")
    
    # Cargar términos
    rows = get_definicions()
    terminos = [r[1] for r in rows]

    if not terminos:
        st.warning("No hay términos en el diccionario.")
        return

    # Seleccionar término
    termino = st.selectbox("Selecciona un término para practicar:", terminos)
    
    # Banco de ejercicios organizado por tema
    ejercicios_db = {
        "Bisección": {
            "enunciado": "Encuentra una raíz de f(x) = x³ - 2x - 5 usando el método de bisección en el intervalo [2, 3]",
            "pasos": [
                "Calcula f(a) y f(b) para verificar que hay cambio de signo",
                "Encuentra el punto medio c = (a + b)/2",
                "Evalúa f(c) y decide en qué subintervalo continuar",
                "Repite hasta alcanzar la tolerancia deseada"
            ],
            "solucion": "La raíz aproximada es x ≈ 2.0946"
        },
        "Newton": {
            "enunciado": "Aplica el método de Newton para encontrar la raíz de f(x) = eˣ - 3x² con x₀ = 1",
            "pasos": [
                "Calcula f(x) y f'(x)",
                "Aplica la fórmula: x₁ = x₀ - f(x₀)/f'(x₀)",
                "Repite el proceso iterativo",
                "Verifica la convergencia"
            ],
            "solucion": "La raíz aproximada es x ≈ 0.9100"
        },
        "Trapecio": {
            "enunciado": "Aproxima ∫(0→2) (x² + 1) dx usando la regla del trapecio con n=4",
            "pasos": [
                "Divide el intervalo en 4 subintervalos",
                "Calcula h = (b-a)/n",
                "Aplica la fórmula del trapecio",
                "Suma las áreas de todos los trapecios"
            ],
            "solucion": "La aproximación es 4.25"
        },
        "Gauss": {
            "enunciado": "Resuelve el sistema usando eliminación Gaussiana:\n2x + y - z = 8\n-3x - y + 2z = -11\n-2x + y + 2z = -3",
            "pasos": [
                "Escribe la matriz aumentada",
                "Aplica operaciones elementales para triangularizar",
                "Realiza sustitución hacia atrás",
                "Verifica la solución"
            ],
            "solucion": "x = 2, y = 3, z = -1"
        }
    }
    
    # Ejercicio por defecto si no está en la base
    ejercicio = ejercicios_db.get(termino, {
        "enunciado": f"Explica qué significa **{termino}** y resuelve un problema típico.",
        "pasos": ["Investiga el concepto", "Plantea un ejemplo", "Resuélvelo paso a paso"],
        "solucion": "Solución del ejemplo planteado"
    })
    
    st.subheader(f"Ejercicio: {termino}")
    st.write(ejercicio["enunciado"])
    
    # Mostrar pasos guiados
    st.write("**Pasos a seguir:**")
    for i, paso in enumerate(ejercicio["pasos"], 1):
        st.write(f"{i}. {paso}")
    
    # Área para que el usuario escriba su solución
    st.subheader("Tu solución paso a paso:")
    solucion_usuario = st.text_area("Describe tu procedimiento:", height=200, key="solucion_guiada")
    
    # Botones de interacción
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 Ver pista"):
            st.info(f"Pista: {ejercicio['pasos'][0]}")
    
    with col2:
        if st.button("✅ Verificar solución"):
            if solucion_usuario:
                st.success("¡Procedimiento registrado! Revisa tu trabajo comparando con la solución.")
                with st.expander("Ver solución completa"):
                    st.write(ejercicio["solucion"])
            else:
                st.warning("Escribe tu solución primero")
    
    with col3:
        if st.button("🔄 Nuevo ejercicio"):
            st.rerun()

def quiz_rapido():
    st.header("🎮 Quiz Rápido - Métodos Numéricos")
    
    preguntas = [
        {
            "pregunta": "¿Qué método garantiza convergencia si f(a)*f(b) < 0?",
            "opciones": ["Newton-Raphson", "Bisección", "Secante", "Todos"],
            "respuesta": 1
        },
        {
            "pregunta": "En punto flotante, ¿qué error domina en operaciones iterativas?",
            "opciones": ["Error absoluto", "Error relativo", "Error de truncamiento", "Error de redondeo"],
            "respuesta": 3
        },
        {
            "pregunta": "¿Qué método usa derivadas para acelerar convergencia?",
            "opciones": ["Bisección", "Falsa posición", "Newton-Raphson", "Secante"],
            "respuesta": 2
        },
        {
            "pregunta": "En Gauss-Seidel, ¿cómo se actualizan las variables?",
            "opciones": ["Simultáneamente", "Secuencialmente", "Aleatoriamente", "En paralelo"],
            "respuesta": 1
        }
    ]
    
    if 'puntaje' not in st.session_state:
        st.session_state.puntaje = 0
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas = []
    
    if st.session_state.pregunta_actual < len(preguntas):
        p = preguntas[st.session_state.pregunta_actual]
        
        st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1}")
        st.write(p["pregunta"])
        
        respuesta = st.radio("Selecciona tu respuesta:", p["opciones"], key=f"pregunta_{st.session_state.pregunta_actual}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⏭️ Siguiente pregunta"):
                # Verificar respuesta
                if respuesta == p["opciones"][p["respuesta"]]:
                    st.session_state.puntaje += 1
                    st.session_state.respuestas.append(True)
                else:
                    st.session_state.respuestas.append(False)
                
                st.session_state.pregunta_actual += 1
                st.rerun()
    
    else:
        st.subheader("🎉 Quiz Completado!")
        st.write(f"Puntaje final: **{st.session_state.puntaje}/{len(preguntas)}**")
        
        # Mostrar revisión
        st.write("**Revisión de respuestas:**")
        for i, (p, correcta) in enumerate(zip(preguntas, st.session_state.respuestas)):
            emoji = "✅" if correcta else "❌"
            st.write(f"{emoji} Pregunta {i+1}: {p['pregunta']}")
            st.write(f"   Respuesta correcta: **{p['opciones'][p['respuesta']]}**")
        
        if st.button("🔄 Reiniciar quiz"):
            st.session_state.puntaje = 0
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas = []
            st.rerun()

def calculadora_numerica():
    st.header("🧮 Calculadora Numérica Interactiva")
    
    metodo = st.selectbox("Selecciona un método numérico:", 
                         ["Bisección", "Newton-Raphson", "Trapecio", "Simpson 1/3"])
    
    if metodo == "Bisección":
        st.latex(r"f(x) = x^3 - 2x - 5")
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("a", value=2.0)
        with col2:
            b = st.number_input("b", value=3.0)
        with col3:
            tol = st.number_input("Tolerancia", value=0.001, format="%.4f")
        
        if st.button("Calcular bisección"):
            # Simulación del método
            st.write("**Iteraciones:**")
            for i in range(5):
                c = (a + b) / 2
                st.write(f"Iteración {i+1}: c = {c:.6f}")
    
    elif metodo == "Newton-Raphson":
        st.latex(r"f(x) = e^x - 3x^2")
        st.latex(r"f'(x) = e^x - 6x")
        x0 = st.number_input("x₀", value=1.0)
        
        if st.button("Calcular Newton"):
            st.write("**Iteraciones:**")
            x = x0
            for i in range(5):
                fx = np.exp(x) - 3*x**2
                fpx = np.exp(x) - 6*x
                x_new = x - fx/fpx
                st.write(f"Iteración {i+1}: x = {x_new:.6f}, f(x) = {fx:.6f}")
                x = x_new

def visualizaciones():
    st.header("📊 Visualizaciones de Métodos Numéricos")
    
    viz_type = st.selectbox("Tipo de visualización:", 
                           ["Convergencia de métodos", "Error vs Iteraciones", "Métodos de integración"])
    
    if viz_type == "Convergencia de métodos":
        st.write("**Comparación de velocidad de convergencia:**")
        st.image("https://via.placeholder.com/600x300?text=Gráfico+Convergencia+Métodos", 
                caption="Bisección (lineal) vs Newton (cuadrática) vs Secante (superlineal)")
    
    elif viz_type == "Error vs Iteraciones":
        st.write("**Evolución del error en diferentes métodos:**")
        # Datos de ejemplo
        iteraciones = list(range(1, 11))
        error_biseccion = [0.5 * (0.5)**i for i in iteraciones]
        error_newton = [0.1 * (0.1)**i for i in iteraciones]
        
        st.line_chart({
            "Bisección": error_biseccion,
            "Newton": error_newton
        })
    
    st.write("---")
    st.write("**Práctica interactiva:**")
    
    # Ejemplo simple de método numérico interactivo
    st.subheader("Método de Bisección Interactivo")
    
    def f(x):
        return x**3 - 2*x - 5
    
    a, b = 2, 3
    puntos = []
    
    for i in range(5):
        c = (a + b) / 2
        puntos.append((i+1, a, b, c, f(c)))
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    # Mostrar tabla de iteraciones
    st.write("**Iteraciones del método:**")
    for iter, a_val, b_val, c_val, fc in puntos:
        st.write(f"Iteración {iter}: a={a_val:.4f}, b={b_val:.4f}, c={c_val:.4f}, f(c)={fc:.4f}")

if __name__ == "__main__":
    app()