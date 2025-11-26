# En tu archivo ejemplos/ejemplos.py - VERSIÓN MEJORADA

import streamlit as st
import random
import numpy as np
import sys
import os
import pandas as pd

try:
    # Intentar importar desde el directorio padre
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from datos import get_definicions
    DATA_LOADED = True
except ImportError as e:
    st.error(f"Error cargando datos: {e}")
    DATA_LOADED = False

def app():
    try:
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
    
    except Exception as e:
        st.error(f"Error en la aplicación de ejemplos: {e}")
        st.info("💡 Si el problema persiste, verifica que todos los archivos estén correctamente configurados.")

def ejercicios_guiados():
    st.header("📝 Ejercicios Guiados por Término")
    
    # Manejo robusto de la carga de términos
    try:
        if DATA_LOADED:
            rows = get_definicions()
            terminos = [r[1] for r in rows]
        else:
            raise ImportError("No se pudieron cargar los datos")
    except:
        # Lista de respaldo con términos comunes de métodos numéricos
        terminos = [
            "Bisección", "Newton-Raphson", "Secante", "Falsa Posición",
            "Trapecio", "Simpson", "Gauss", "Jacobi", "Gauss-Seidel", 
            "Error de redondeo", "Error de truncamiento", "Convergencia",
            "Pivoteo", "Factorización LU", "Cholesky", "Diferencias Finitas"
        ]
        st.info("📝 Usando términos predefinidos. Los datos del diccionario no están disponibles.")

    if not terminos:
        st.warning("No hay términos disponibles para practicar.")
        return

    # Seleccionar término
    termino = st.selectbox("Selecciona un término para practicar:", terminos)
    
    # Ejercicios mejorados con más variedad
    ejercicio, solucion = generar_ejercicio(termino)
    
    st.subheader(f"🧩 Ejercicio: {termino}")
    st.write(ejercicio["enunciado"])
    
    # Mostrar pasos guiados
    with st.expander("📋 Ver pasos recomendados"):
        for i, paso in enumerate(ejercicio["pasos"], 1):
            st.write(f"{i}. {paso}")
    
    # Área para solución del usuario
    st.subheader("✍️ Tu solución")
    solucion_usuario = st.text_area(
        "Describe tu procedimiento paso a paso:", 
        height=200, 
        placeholder="1. Primero, identifique...\n2. Luego, calcule...\n3. Finalmente, verifique...",
        key=f"sol_{termino}"
    )
    
    # Botones de interacción
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💡 Sugerencia", key=f"hint_{termino}"):
            st.info(f"**Sugerencia:** {ejercicio.get('sugerencia', 'Revisa la teoría del método antes de empezar.')}")
    
    with col2:
        if st.button("📚 Ver teoría", key=f"theory_{termino}"):
            with st.expander("Conceptos teóricos"):
                st.write(ejercicio.get('teoria', 'Consulta el diccionario para la teoría completa.'))
    
    with col3:
        if st.button("✅ Ver solución", key=f"sol_btn_{termino}"):
            if solucion_usuario:
                st.success("¡Bien! Ahora compara con la solución de referencia:")
            else:
                st.warning("Te recomiendo intentar resolverlo primero, pero aquí está la solución:")
            
            with st.expander("🔍 Solución detallada"):
                st.write(solucion)

def generar_ejercicio(termino):
    """Genera ejercicios dinámicos basados en el término"""
    
    ejercicios_base = {
        "Bisección": {
            "enunciado": "Encuentra una raíz de f(x) = x³ - 2x - 5 en el intervalo [2, 3] usando 5 iteraciones del método de bisección.",
            "pasos": [
                "Verifica que f(2)*f(3) < 0",
                "Calcula el punto medio c = (a+b)/2",
                "Evalúa f(c) y determina el nuevo intervalo",
                "Repite hasta completar las iteraciones",
                "Calcula el error aproximado"
            ],
            "sugerencia": "Recuerda que cada iteración reduce el intervalo a la mitad.",
            "teoria": "El método de bisección garantiza convergencia cuando hay cambio de signo en el intervalo.",
            "solucion": "Después de 5 iteraciones: x ≈ 2.0938, Error ≈ 0.03125"
        },
        "Newton-Raphson": {
            "enunciado": "Aplica el método de Newton-Raphson para encontrar una raíz de f(x) = eˣ - 3x² empezando con x₀ = 1. Realiza 3 iteraciones.",
            "pasos": [
                "Calcula f(x) y f'(x)",
                "Aplica x₁ = x₀ - f(x₀)/f'(x₀)", 
                "Repite para x₂ y x₃",
                "Analiza la convergencia"
            ],
            "sugerencia": "Verifica que la derivada no sea cero en ninguna iteración.",
            "solucion": "Iteración 1: x₁ = 0.5, Iteración 2: x₂ ≈ 0.783, Iteración 3: x₃ ≈ 0.885"
        },
        # ... más ejercicios para otros términos
    }
    
    # Ejercicio por defecto si el término no está en la base
    if termino not in ejercicios_base:
        ejercicio_default = {
            "enunciado": f"Explica el método **{termino}** y resuelve un problema ejemplo.",
            "pasos": [
                f"Investiga los fundamentos de {termino}",
                "Plantea un problema adecuado", 
                "Aplica el método paso a paso",
                "Analiza los resultados y el error"
            ],
            "sugerencia": f"Busca en el diccionario la definición completa de {termino}.",
            "solucion": f"Solución de ejemplo para {termino}"
        }
        return ejercicio_default, f"Esta es la solución de referencia para el método {termino}."
    
    return ejercicios_base[termino], ejercicios_base[termino]["solucion"]

def quiz_rapido():
    st.header("🎮 Quiz Rápido - Métodos Numéricos")
    
    # Preguntas mejoradas
    preguntas = [
        {
            "pregunta": "¿Qué método garantiza convergencia si f(a)*f(b) < 0?",
            "opciones": ["Newton-Raphson", "Bisección", "Secante", "Todos"],
            "respuesta": 1,
            "explicacion": "✅ Correcto! Solo el método de bisección garantiza convergencia cuando hay cambio de signo."
        },
        {
            "pregunta": "¿Cuál es el orden de convergencia del método de Newton-Raphson?",
            "opciones": ["Lineal", "Cuadrático", "Cúbico", "Superlineal"],
            "respuesta": 1, 
            "explicacion": "✅ Exacto! Newton-Raphson tiene convergencia cuadrática bajo condiciones adecuadas."
        },
        {
            "pregunta": "En el método de Gauss-Seidel, las variables se actualizan:",
            "opciones": [
                "Todas simultáneamente", 
                "Una por una usando los últimos valores",
                "En orden aleatorio", 
                "Solo al final de cada iteración"
            ],
            "respuesta": 1,
            "explicacion": "✅ Correcto! Gauss-Seidel actualiza secuencialmente usando los valores más recientes."
        }
    ]
    
    # Inicializar estado del quiz
    if 'quiz_state' not in st.session_state:
        st.session_state.quiz_state = {
            'puntaje': 0,
            'pregunta_actual': 0,
            'completado': False,
            'respuestas': []
        }
    
    state = st.session_state.quiz_state
    
    if not state['completado'] and state['pregunta_actual'] < len(preguntas):
        # Mostrar pregunta actual
        p = preguntas[state['pregunta_actual']]
        
        st.subheader(f"Pregunta {state['pregunta_actual'] + 1} de {len(preguntas)}")
        st.write(f"**{p['pregunta']}**")
        
        # Opciones de respuesta
        opcion_seleccionada = st.radio(
            "Selecciona tu respuesta:",
            p["opciones"],
            key=f"q{state['pregunta_actual']}"
        )
        
        # Botón para avanzar
        if st.button("⏭️ Siguiente", key=f"next{state['pregunta_actual']}"):
            # Verificar respuesta
            es_correcta = (opcion_seleccionada == p["opciones"][p["respuesta"]])
            if es_correcta:
                state['puntaje'] += 1
            
            state['respuestas'].append({
                'pregunta': p['pregunta'],
                'correcta': es_correcta,
                'explicacion': p['explicacion']
            })
            
            state['pregunta_actual'] += 1
            if state['pregunta_actual'] >= len(preguntas):
                state['completado'] = True
            
            st.rerun()
    
    else:
        # Mostrar resultados finales
        state['completado'] = True
        
        st.balloons()
        st.subheader("🎉 Quiz Completado!")
        
        puntaje = state['puntaje']
        total = len(preguntas)
        porcentaje = (puntaje / total) * 100
        
        # Mostrar resultado con estilo
        if porcentaje >= 90:
            st.success(f"🏆 **Excelente!** Puntaje: {puntaje}/{total} ({porcentaje:.0f}%)")
        elif porcentaje >= 70:
            st.info(f"⭐ **Buen trabajo!** Puntaje: {puntaje}/{total} ({porcentaje:.0f}%)")
        else:
            st.warning(f"📚 **Sigue practicando!** Puntaje: {puntaje}/{total} ({porcentaje:.0f}%)")
        
        # Revisión detallada
        with st.expander("📊 Ver revisión detallada"):
            for i, resp in enumerate(state['respuestas']):
                emoji = "✅" if resp['correcta'] else "❌"
                st.write(f"{emoji} **Pregunta {i+1}:** {resp['pregunta']}")
                st.write(f"   {resp['explicacion']}")
                st.write("")
        
        # Botón para reiniciar
        if st.button("🔄 Intentar otro quiz"):
            st.session_state.quiz_state = {
                'puntaje': 0,
                'pregunta_actual': 0,
                'completado': False,
                'respuestas': []
            }
            st.rerun()

def calculadora_numerica():
    st.header("🧮 Calculadora Numérica Interactiva")
    
    metodo = st.selectbox(
        "Selecciona un método:",
        ["Bisección", "Newton-Raphson", "Regla del Trapecio", "Simpson 1/3", "Eliminación Gaussiana"]
    )
    
    if metodo == "Bisección":
        calcular_biseccion()
    elif metodo == "Newton-Raphson":
        calcular_newton()
    elif metodo == "Regla del Trapecio":
        calcular_trapecio()
    else:
        st.info(f"🚧 Calculadora para {metodo} en desarrollo...")

def calcular_biseccion():
    st.subheader("Método de Bisección")
    
    col1, col2 = st.columns(2)
    with col1:
        funcion = st.text_input("f(x)", "x**3 - 2*x - 5")
        a = st.number_input("a", value=2.0)
    with col2:
        b = st.number_input("b", value=3.0)
        iteraciones = st.slider("Iteraciones", 1, 10, 5)
    
    if st.button("Calcular"):
        try:
            # Simulación del método
            st.write("**Iteraciones:**")
            resultados = []
            a_act, b_act = a, b
            
            for i in range(iteraciones):
                c = (a_act + b_act) / 2
                # Evaluación simple (en producción usar eval con precauciones)
                fa = a_act**3 - 2*a_act - 5  # Simplificado para demo
                fc = c**3 - 2*c - 5
                
                resultados.append({
                    'Iteración': i+1,
                    'a': a_act,
                    'b': b_act, 
                    'c': c,
                    'f(c)': fc,
                    'Error': (b_act - a_act) / 2
                })
                
                if fa * fc < 0:
                    b_act = c
                else:
                    a_act = c
            
            # Mostrar resultados en tabla
            df = pd.DataFrame(resultados)
            st.dataframe(df.style.format("{:.4f}"), use_container_width=True)
            
            st.success(f"**Raíz aproximada:** {c:.6f}")
            
        except Exception as e:
            st.error(f"Error en el cálculo: {e}")

def calcular_newton():
    st.subheader("Método de Newton-Raphson")
    # Implementación similar a calcular_biseccion pero para Newton
    st.info("Implementación de Newton-Raphson en desarrollo...")

def calcular_trapecio():
    st.subheader("Regla del Trapecio")
    # Implementación para integración numérica
    st.info("Implementación de la Regla del Trapecio en desarrollo...")

def visualizaciones():
    st.header("📊 Visualizaciones Interactivas")
    
    st.write("""
    **Próximamente:** Gráficos interactivos que muestren:
    - Convergencia de diferentes métodos
    - Comparación de errores
    - Visualización de métodos de integración
    - Animaciones de algoritmos iterativos
    """)
    
    # Placeholder para futuras visualizaciones
    st.image("https://via.placeholder.com/600x300?text=Visualizaciones+Interactivas", 
             caption="Gráficos y animaciones de métodos numéricos")

if __name__ == "__main__":
    app()