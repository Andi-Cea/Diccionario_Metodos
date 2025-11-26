import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title("🎯 Ejercicios Interactivos - Métodos Numéricos")
    
    # Menú de métodos
    metodo = st.sidebar.selectbox(
        "Selecciona un método:",
        [
            "1.2 Errores Numéricos",
            "1.3 Propagación del Error", 
            "1.4 Orden de Convergencia",
            "2.1 Bisección",
            "2.2 Falsa Posición",
            "2.3 Newton-Raphson",
            "2.4 Secante",
            "3.1 Inversión de Matrices",
            "3.2 Gauss",
            "3.3 Gauss-Jordan",
            "3.4 Jacobi",
            "3.5 Gauss-Seidel",
            "4.2 Cholesky",
            "5.1 Método de Potencias"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'exercises_completed' not in st.session_state:
        st.session_state.exercises_completed = 0
    
    # Diccionario de métodos
    metodos = {
        "1.2 Errores Numéricos": errores_numericos,
        "1.3 Propagación del Error": propagacion_error,
        "1.4 Orden de Convergencia": orden_convergencia,
        "2.1 Bisección": biseccion,
        "2.2 Falsa Posición": falsa_posicion,
        "2.3 Newton-Raphson": newton_raphson,
        "2.4 Secante": secante,
        "3.1 Inversión de Matrices": inversion_matrices,
        "3.2 Gauss": gauss,
        "3.3 Gauss-Jordan": gauss_jordan,
        "3.4 Jacobi": jacobi,
        "3.5 Gauss-Seidel": gauss_seidel,
        "4.2 Cholesky": cholesky,
        "5.1 Método de Potencias": metodo_potencias
    }
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score = 0
        st.session_state.exercises_completed = 0
        st.rerun()
    
    # Ejecutar método seleccionado
    if metodo in metodos:
        metodos[metodo]()

def check_answer(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def errores_numericos():
    st.header("🔍 Ejercicios - Errores Numéricos")
    
    st.info("Resuelve estos ejercicios sobre errores de redondeo y truncamiento")
    
    # Ejercicio 1 - Error de redondeo
    st.subheader("Ejercicio 1: Error de Redondeo")
    st.write("Calcula el error absoluto al aproximar π (3.1415926535) con 3.14")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        user_answer1 = st.number_input("Error absoluto:", value=0.0, step=0.0001, format="%.6f")
    
    with col2:
        if st.button("Verificar ✅", key="check1"):
            correct_answer = abs(3.1415926535 - 3.14)
            check_answer(correct_answer, user_answer1)
    
    # Ejercicio 2 - Serie de Taylor
    st.subheader("Ejercicio 2: Error de Truncamiento")
    st.write("Aproxima e¹ usando 3 términos de la serie de Taylor:")
    st.latex(r"e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}")
    
    user_approx = st.number_input("Tu aproximación para e¹:", value=0.0, step=0.1)
    
    if st.button("Verificar Aproximación", key="check2"):
        # Calcular aproximación correcta
        correct_approx = 1 + 1 + 1/2 + 1/6
        check_answer(correct_approx, user_approx, 0.001)
    
    # Ejercicio 3 - Opción múltiple
    st.subheader("Ejercicio 3: Pregunta Conceptual")
    st.write("¿Cuál de estos números tiene mayor error de redondeo en representación binaria?")
    
    option = st.radio(
        "Selecciona la respuesta correcta:",
        ["0.5", "0.1", "0.25", "0.125"],
        key="error_q"
    )
    
    if st.button("Verificar Selección", key="check3"):
        if option == "0.1":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! 0.1 tiene representación infinita periódica en binario")
        else:
            st.error("❌ Incorrecto. 0.1 no se puede representar exactamente en binario")

def propagacion_error():
    st.header("📈 Ejercicios - Propagación del Error")
    
    st.info("Practica el cálculo de propagación de errores")
    
    # Ejercicio 1 - Suma con errores
    st.subheader("Ejercicio 1: Suma con Errores")
    st.write("Si a = 10 ± 0.1 y b = 5 ± 0.2, ¿cuál es el error en a + b?")
    
    user_error_sum = st.number_input("Error en a + b:", value=0.0, step=0.1)
    
    if st.button("Verificar Suma", key="check_sum"):
        correct_error = 0.1 + 0.2  # Error absoluto en suma
        check_answer(correct_error, user_error_sum)
    
    # Ejercicio 2 - Multiplicación con errores
    st.subheader("Ejercicio 2: Multiplicación con Errores")
    st.write("Para los mismos valores, ¿cuál es el error aproximado en a × b?")
    
    user_error_mult = st.number_input("Error en a × b:", value=0.0, step=0.1)
    
    if st.button("Verificar Multiplicación", key="check_mult"):
        # Error en multiplicación: |b|·Δa + |a|·Δb
        correct_error = abs(5)*0.1 + abs(10)*0.2
        check_answer(correct_error, user_error_mult, 0.1)

def orden_convergencia():
    st.header("📊 Ejercicios - Orden de Convergencia")
    
    st.info("Identifica el orden de convergencia de diferentes métodos")
    
    # Ejercicio 1 - Identificar orden
    st.subheader("Ejercicio 1: Identificar el Orden")
    st.write("Observa esta secuencia de errores y determina el orden de convergencia:")
    st.write("Errores: 0.1, 0.05, 0.0125, 0.00156")
    
    order_guess = st.selectbox(
        "¿Qué orden de convergencia crees que tiene?",
        ["Lineal (orden 1)", "Cuadrático (orden 2)", "Superlineal", "No converge"],
        key="order_q"
    )
    
    if st.button("Verificar Orden", key="check_order"):
        if order_guess == "Cuadrático (orden 2)":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Los errores disminuyen cuadráticamente")
        else:
            st.error("❌ Incorrecto. La relación entre errores sugiere convergencia cuadrática")

def biseccion():
    st.header("🎯 Ejercicios - Método de Bisección")
    
    st.info("Practica el método de bisección para encontrar raíces")
    
    # Ejercicio 1 - Aplicar bisección
    st.subheader("Ejercicio 1: Aplicar Bisección")
    st.write("Encuentra una raíz de f(x) = x² - 4 en el intervalo [1, 3]")
    st.write("Aplica UNA iteración del método de bisección")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Datos iniciales:**")
        st.write("a = 1, b = 3")
        st.write("f(1) = -3, f(3) = 5")
    
    with col2:
        user_c = st.number_input("Calcula el punto medio c:", value=0.0, step=0.1)
    
    if st.button("Verificar Iteración", key="check_bisec"):
        correct_c = (1 + 3) / 2
        if check_answer(correct_c, user_c):
            st.write("**Siguiente paso:** ¿En qué subintervalo continuar?")
            st.write("f(2) = 0 → ¡Raíz encontrada!")

def falsa_posicion():
    st.header("📐 Ejercicios - Falsa Posición")
    
    st.info("Practica el método de falsa posición")
    
    st.subheader("Ejercicio: Falsa Posición")
    st.write("Para f(x) = x² - 4 en [1, 3], calcula la primera aproximación:")
    st.latex(r"c = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}")
    
    st.write("Datos: a=1, b=3, f(a)=-3, f(b)=5")
    
    user_c_falsa = st.number_input("Calcula c:", value=0.0, step=0.1)
    
    if st.button("Verificar Falsa Posición", key="check_falsa"):
        correct_c = (1*5 - 3*(-3)) / (5 - (-3))
        check_answer(correct_c, user_c_falsa, 0.01)

def newton_raphson():
    st.header("🚀 Ejercicios - Newton-Raphson")
    
    st.info("Practica el método de Newton-Raphson")
    
    st.subheader("Ejercicio: Una Iteración de Newton")
    st.write("Para f(x) = x² - 4, con x₀ = 3, calcula x₁:")
    st.latex(r"x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}")
    
    st.write("f(x) = x² - 4, f'(x) = 2x")
    st.write("x₀ = 3, f(3) = 5, f'(3) = 6")
    
    user_x1 = st.number_input("Calcula x₁:", value=0.0, step=0.1)
    
    if st.button("Verificar Newton", key="check_newton"):
        correct_x1 = 3 - 5/6
        check_answer(correct_x1, user_x1, 0.01)

def secante():
    st.header("📏 Ejercicios - Método de la Secante")
    
    st.info("Practica el método de la secante")
    
    st.subheader("Ejercicio: Método de la Secante")
    st.write("Para f(x) = x² - 4, con x₀=1, x₁=3, calcula x₂:")
    st.latex(r"x_2 = x_1 - f(x_1) \cdot \frac{x_1 - x_0}{f(x_1) - f(x_0)}")
    
    st.write("x₀=1, x₁=3, f(1)=-3, f(3)=5")
    
    user_x2 = st.number_input("Calcula x₂:", value=0.0, step=0.1)
    
    if st.button("Verificar Secante", key="check_sec"):
        correct_x2 = 3 - 5 * (3-1)/(5 - (-3))
        check_answer(correct_x2, user_x2, 0.01)

def inversion_matrices():
    st.header("🔄 Ejercicios - Inversión de Matrices")
    
    st.info("Practica la inversión de matrices 2x2")
    
    st.subheader("Ejercicio: Inversa de Matriz 2x2")
    st.write("Calcula la inversa de:")
    st.latex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Fórmula para matriz 2x2:**")
        st.latex(r"A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}")
    
    with col2:
        user_det = st.number_input("Determinante (ad-bc):", value=0.0, step=0.1)
        user_inv_11 = st.number_input("Elemento (1,1) de A⁻¹:", value=0.0, step=0.1)
    
    if st.button("Verificar Inversa", key="check_inv"):
        correct_det = 2*3 - 1*1
        correct_inv_11 = 3/5
        
        if check_answer(correct_det, user_det, 0.01) and check_answer(correct_inv_11, user_inv_11, 0.01):
            st.success("¡Ambas respuestas correctas! +20 puntos")
            st.session_state.score += 10  # Bonus por ambas correctas

def gauss():
    st.header("🎯 Ejercicios - Eliminación Gaussiana")
    
    st.info("Resuelve sistemas con eliminación gaussiana")
    
    st.subheader("Ejercicio: Sistema 2x2")
    st.write("Resuelve:")
    st.latex(r"\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}")
    
    st.write("**Primer paso:** Haz 1 el coeficiente de x en la primera ecuación")
    
    user_x1_coef = st.number_input("Nuevo coeficiente de y en ec. 1:", value=0.0, step=0.1)
    
    if st.button("Verificar Primer Paso", key="check_gauss1"):
        # Dividir primera ecuación por 2: 2x + y = 5 → x + 0.5y = 2.5
        check_answer(0.5, user_x1_coef, 0.01)

def gauss_jordan():
    st.header("🔷 Ejercicios - Gauss-Jordan")
    
    st.info("Practica la eliminación completa")
    
    st.subheader("Ejercicio: Matriz Identidad")
    st.write("¿Cuál es el objetivo final del método de Gauss-Jordan?")
    
    answer = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Convertir la matriz en triangular superior",
            "Convertir la matriz en la identidad", 
            "Encontrar el determinante",
            "Calcular autovalores"
        ],
        key="gauss_jordan_q"
    )
    
    if st.button("Verificar Objetivo", key="check_gj"):
        if answer == "Convertir la matriz en la identidad":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Gauss-Jordan busca la matriz identidad")
        else:
            st.error("❌ Incorrecto. Gauss-Jordan transforma la matriz en la identidad")

def jacobi():
    st.header("🔄 Ejercicios - Método de Jacobi")
    
    st.info("Practica métodos iterativos")
    
    st.subheader("Ejercicio: Primera Iteración de Jacobi")
    st.write("Para el sistema:")
    st.latex(r"\begin{cases} 4x + y = 7 \\ x + 3y = 5 \end{cases}")
    st.write("Con valor inicial (x₀,y₀) = (0,0), calcula x₁:")
    
    user_x1_jacobi = st.number_input("x₁ = (7 - y₀)/4 =", value=0.0, step=0.1)
    
    if st.button("Verificar Jacobi", key="check_jacobi"):
        correct_x1 = (7 - 0)/4
        check_answer(correct_x1, user_x1_jacobi, 0.01)

def gauss_seidel():
    st.header("⚡ Ejercicios - Gauss-Seidel")
    
    st.info("Practica el método de Gauss-Seidel")
    
    st.subheader("Ejercicio: Diferencia con Jacobi")
    st.write("¿Cuál es la principal diferencia entre Jacobi y Gauss-Seidel?")
    
    answer_gs = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Jacobi usa todos los valores nuevos en cada iteración",
            "Gauss-Seidel usa valores actualizados inmediatamente",
            "Solo Jacobi converge siempre",
            "Gauss-Seidel es más lento que Jacobi"
        ],
        key="gs_q"
    )
    
    if st.button("Verificar Diferencia", key="check_gs"):
        if answer_gs == "Gauss-Seidel usa valores actualizados inmediatamente":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Gauss-Seidel actualiza valores sobre la marcha")
        else:
            st.error("❌ Incorrecto. Gauss-Seidel usa valores recién calculados")

def cholesky():
    st.header("🔺 Ejercicios - Factorización de Cholesky")
    
    st.info("Practica factorización de matrices")
    
    st.subheader("Ejercicio: Requisito de Cholesky")
    st.write("¿Qué propiedad debe tener una matriz para aplicar Cholesky?")
    
    answer_chol = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Ser diagonal",
            "Ser simétrica y definida positiva", 
            "Tener determinante cero",
            "Ser triangular"
        ],
        key="cholesky_q"
    )
    
    if st.button("Verificar Cholesky", key="check_chol"):
        if answer_chol == "Ser simétrica y definida positiva":
            st.session_state.score += 10
            st.session_state.exercises_completed += 1
            st.success("🎉 ¡Correcto! Cholesky requiere matrices simétricas definidas positivas")
        else:
            st.error("❌ Incorrecto. La matriz debe ser simétrica y definida positiva")

def metodo_potencias():
    st.header("💪 Ejercicios - Método de las Potencias")
    
    st.info("Practica encontrar autovalores dominantes")
    
    st.subheader("Ejercicio: Aproximación Inicial")
    st.write("Para la matriz A = [[2,1],[1,3]] y vector inicial v₀ = [1,1]")
    st.write("Calcula la primera aproximación del autovalor:")
    
    user_eigen_approx = st.number_input("Aproximación del autovalor dominante:", value=0.0, step=0.1)
    
    if st.button("Verificar Autovalor", key="check_eigen"):
        A = np.array([[2, 1], [1, 3]])
        v0 = np.array([1, 1])
        Av = A @ v0
        correct_approx = np.linalg.norm(Av, np.inf)  # Norma infinito
        check_answer(correct_approx, user_eigen_approx, 0.1)