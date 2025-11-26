import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("🎯 Ejercicios Interactivos - Métodos Numéricos II")
    
    # Menú de métodos
    metodo = st.sidebar.selectbox(
        "Selecciona un método:",
        [
            "1.2 Interpolación Polinomial",
            "2.2 Fórmula de Lagrange",
            "3.2 Interpolación de Newton - Diferencias Finitas",
            "4.2 Diferencias Divididas",
            "5.2 Interpolación de Hermite",
            "6.2 Ajuste de Curvas - Splines",
            "7.2 Regresión Lineal",
            "8.3 Newton-Cotes - Trapecio",
            "9.3 Regla de Simpson 1/3",
            "10.3 Regla de Simpson 3/8",
            "11.3 Integración de Romberg",
            "12.1 Punto Fijo para Sistemas NO lineales",
            "13.1 Método de Newton para Sistemas",
            "14.1 Método de Quasi-Newton"
        ]
    )
    
    # Inicializar estado de la sesión
    if 'score_2' not in st.session_state:
        st.session_state.score_2 = 0
    if 'exercises_completed_2' not in st.session_state:
        st.session_state.exercises_completed_2 = 0
    
    # Diccionario de métodos
    metodos = {
        "1.2 Interpolación Polinomial": interpolacion_polinomial,
        "2.2 Fórmula de Lagrange": lagrange,
        "3.2 Interpolación de Newton - Diferencias Finitas": newton_diferencias_finitas,
        "4.2 Diferencias Divididas": diferencias_divididas,
        "5.2 Interpolación de Hermite": hermite,
        "6.2 Ajuste de Curvas - Splines": splines,
        "7.2 Regresión Lineal": regresion_lineal,
        "8.3 Newton-Cotes - Trapecio": trapecio,
        "9.3 Regla de Simpson 1/3": simpson_13,
        "10.3 Regla de Simpson 3/8": simpson_38,
        "11.3 Integración de Romberg": romberg,
        "12.1 Punto Fijo para Sistemas NO lineales": punto_fijo_sistemas,
        "13.1 Método de Newton para Sistemas": newton_sistemas,
        "14.1 Método de Quasi-Newton": quasi_newton
    }
    
    # Mostrar puntuación
    st.sidebar.markdown("---")
    st.sidebar.metric("🏆 Puntuación", st.session_state.score_2)
    st.sidebar.metric("✅ Ejercicios Completados", st.session_state.exercises_completed_2)
    
    if st.sidebar.button("🔄 Reiniciar Puntuación"):
        st.session_state.score_2 = 0
        st.session_state.exercises_completed_2 = 0
        st.rerun()
    
    # Ejecutar método seleccionado
    if metodo in metodos:
        metodos[metodo]()

def check_answer_2(correct_answer, user_answer, tolerance=0.01):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        if abs(float(correct_answer) - float(user_answer)) <= tolerance:
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! +10 puntos")
            return True
        else:
            st.error("❌ Incorrecto. Intenta nuevamente.")
            return False
    except:
        st.error("❌ Formato inválido. Usa números.")
        return False

def interpolacion_polinomial():
    st.header("📊 Interpolación Polinomial")
    
    st.info("Encuentra polinomios que pasen por puntos dados")
    
    # Ejercicio 1 - Polinomio interpolante básico
    st.subheader("Ejercicio 1: Polinomio de Grado 1")
    st.write("Dados los puntos (1,2) y (3,4), encuentra el polinomio interpolante de grado 1")
    
    st.write("**Fórmula para dos puntos:**")
    st.latex(r"P_1(x) = y_0 + \frac{y_1 - y_0}{x_1 - x_0}(x - x_0)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Datos:**")
        st.write("x₀ = 1, y₀ = 2")
        st.write("x₁ = 3, y₁ = 4")
    
    with col2:
        user_pendiente = st.number_input("Pendiente (m):", value=0.0, step=0.1, key="pendiente")
        user_intercepto = st.number_input("Intercepto (b):", value=0.0, step=0.1, key="intercepto")
    
    if st.button("Verificar Polinomio", key="check_poly1"):
        pendiente_correcta = (4 - 2) / (3 - 1)
        intercepto_correcto = 2 - pendiente_correcta * 1
        
        if (check_answer_2(pendiente_correcta, user_pendiente, 0.01) and 
            check_answer_2(intercepto_correcto, user_intercepto, 0.01)):
            st.success("¡Polinomio correcto! P₁(x) = x + 1")

def lagrange():
    st.header("🎯 Fórmula de Lagrange")
    
    st.info("Usa polinomios de Lagrange para interpolación")
    
    st.subheader("Ejercicio: Polinomios de Lagrange Básicos")
    st.write("Para los puntos (1,2) y (3,4), calcula L₀(x) y L₁(x)")
    
    st.latex(r"L_0(x) = \frac{x - x_1}{x_0 - x_1} = \frac{x - 3}{1 - 3}")
    st.latex(r"L_1(x) = \frac{x - x_0}{x_1 - x_0} = \frac{x - 1}{3 - 1}")
    
    col1, col2 = st.columns(2)
    with col1:
        user_L0_coef = st.number_input("Coeficiente de x en L₀(x):", value=0.0, step=0.1)
        user_L0_const = st.number_input("Término constante en L₀(x):", value=0.0, step=0.1)
    
    with col2:
        user_L1_coef = st.number_input("Coeficiente de x en L₁(x):", value=0.0, step=0.1)
        user_L1_const = st.number_input("Término constante en L₁(x):", value=0.0, step=0.1)
    
    if st.button("Verificar Lagrange", key="check_lagrange"):
        L0_coef_correcto = -0.5  # 1/(1-3) = -0.5
        L0_const_correcto = 1.5   # -3/(1-3) = 1.5
        L1_coef_correcto = 0.5    # 1/(3-1) = 0.5
        L1_const_correcto = -0.5  # -1/(3-1) = -0.5
        
        correctos = 0
        if check_answer_2(L0_coef_correcto, user_L0_coef, 0.01): correctos += 1
        if check_answer_2(L0_const_correcto, user_L0_const, 0.01): correctos += 1
        if check_answer_2(L1_coef_correcto, user_L1_coef, 0.01): correctos += 1
        if check_answer_2(L1_const_correcto, user_L1_const, 0.01): correctos += 1
        
        if correctos == 4:
            st.success("¡Todos los polinomios de Lagrange correctos!")

def newton_diferencias_finitas():
    st.header("📈 Interpolación de Newton - Diferencias Finitas")
    
    st.info("Usa diferencias finitas para interpolación")
    
    st.subheader("Ejercicio: Tabla de Diferencias Finitas")
    st.write("Construye la tabla de diferencias finitas para:")
    st.write("x: 1, 2, 3")
    st.write("y: 2, 4, 8")
    
    st.write("**Calcula la primera diferencia finita:**")
    st.latex(r"\Delta y_0 = y_1 - y_0")
    
    user_delta1 = st.number_input("Δy₀:", value=0.0, step=0.1)
    
    if st.button("Verificar Diferencia Finita", key="check_dif_fin"):
        delta_correcto = 4 - 2
        if check_answer_2(delta_correcto, user_delta1, 0.01):
            st.write("**Segunda diferencia:** Δ²y₀ = Δy₁ - Δy₀ = (8-4) - (4-2) = 2")

def diferencias_divididas():
    st.header("🔍 Diferencias Divididas")
    
    st.info("Método de Newton con diferencias divididas")
    
    st.subheader("Ejercicio: Primera Diferencia Dividida")
    st.write("Para los puntos (1,2) y (3,4), calcula f[x₀,x₁]:")
    st.latex(r"f[x_0,x_1] = \frac{f(x_1) - f(x_0)}{x_1 - x_0}")
    
    user_dif_div = st.number_input("f[x₀,x₁]:", value=0.0, step=0.1)
    
    if st.button("Verificar Diferencia Dividida", key="check_dif_div"):
        correcto = (4 - 2) / (3 - 1)
        check_answer_2(correcto, user_dif_div, 0.01)

def hermite():
    st.header("✨ Interpolación de Hermite")
    
    st.info("Interpolación que usa valores de la función y su derivada")
    
    st.subheader("Ejercicio: Concepto de Hermite")
    st.write("¿Qué información adicional usa la interpolación de Hermite comparada con Lagrange?")
    
    opcion = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Solo valores de la función",
            "Valores de la función y su derivada",
            "Valores de segunda derivada",
            "Integral de la función"
        ],
        key="hermite_q"
    )
    
    if st.button("Verificar Hermite", key="check_hermite"):
        if opcion == "Valores de la función y su derivada":
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! Hermite usa función y derivada")
        else:
            st.error("❌ Incorrecto. Hermite requiere valores de la función y su derivada")

def splines():
    st.header("📐 Ajuste de Curvas - Splines")
    
    st.info("Interpolación por segmentos con condiciones de suavidad")
    
    st.subheader("Ejercicio: Splines Cúbicos")
    st.write("¿Cuántas condiciones se necesitan para un spline cúbico con n segmentos?")
    
    opcion_spline = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "n condiciones",
            "2n condiciones", 
            "4n condiciones",
            "4n - 2 condiciones"
        ],
        key="spline_q"
    )
    
    if st.button("Verificar Spline", key="check_spline"):
        if opcion_spline == "4n - 2 condiciones":
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! 4n - 2 condiciones para splines cúbicos")
        else:
            st.error("❌ Incorrecto. Splines cúbicos requieren 4n - 2 condiciones")

def regresion_lineal():
    st.header("📊 Regresión Lineal")
    
    st.info("Ajuste de recta por mínimos cuadrados")
    
    st.subheader("Ejercicio: Cálculo de Pendiente")
    st.write("Para los puntos (1,2), (2,3), (3,5), calcula la pendiente de la recta de regresión")
    
    st.write("**Fórmula de la pendiente:**")
    st.latex(r"m = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
    
    user_pendiente_reg = st.number_input("Pendiente de regresión:", value=0.0, step=0.1)
    
    if st.button("Verificar Regresión", key="check_reg"):
        x = [1, 2, 3]
        y = [2, 3, 5]
        n = 3
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi**2 for xi in x)
        
        pendiente_correcta = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        check_answer_2(pendiente_correcta, user_pendiente_reg, 0.01)

def trapecio():
    st.header("📐 Regla del Trapecio")
    
    st.info("Integración numérica usando trapecios")
    
    st.subheader("Ejercicio: Aplicación Simple")
    st.write("Aproxima ∫₀¹ x² dx usando un solo trapecio")
    
    st.latex(r"I \approx \frac{b-a}{2}[f(a) + f(b)]")
    st.write("a = 0, b = 1, f(x) = x²")
    st.write("f(0) = 0, f(1) = 1")
    
    user_trapecio = st.number_input("Aproximación con trapecio:", value=0.0, step=0.1)
    
    if st.button("Verificar Trapecio", key="check_trap"):
        correcto = (1-0)/2 * (0 + 1)
        check_answer_2(correcto, user_trapecio, 0.01)

def simpson_13():
    st.header("🎯 Regla de Simpson 1/3")
    
    st.info("Integración con parábolas")
    
    st.subheader("Ejercicio: Simpson 1/3 Simple")
    st.write("Aproxima ∫₀² x² dx usando Simpson 1/3 con 3 puntos")
    
    st.latex(r"I \approx \frac{h}{3}[f(x_0) + 4f(x_1) + f(x_2)]")
    st.write("x₀=0, x₁=1, x₂=2, h=1")
    st.write("f(0)=0, f(1)=1, f(2)=4")
    
    user_simpson = st.number_input("Aproximación con Simpson 1/3:", value=0.0, step=0.1)
    
    if st.button("Verificar Simpson 1/3", key="check_simp13"):
        correcto = 1/3 * (0 + 4*1 + 4)
        check_answer_2(correcto, user_simpson, 0.01)

def simpson_38():
    st.header("📏 Regla de Simpson 3/8")
    
    st.info("Integración con polinomios cúbicos")
    
    st.subheader("Ejercicio: Fórmula de Simpson 3/8")
    st.write("¿Cuántos puntos se necesitan para Simpson 3/8?")
    
    opcion_simp38 = st.radio(
        "Selecciona la respuesta correcta:",
        ["2 puntos", "3 puntos", "4 puntos", "5 puntos"],
        key="simp38_q"
    )
    
    if st.button("Verificar Simpson 3/8", key="check_simp38"):
        if opcion_simp38 == "4 puntos":
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! Simpson 3/8 requiere 4 puntos")
        else:
            st.error("❌ Incorrecto. Simpson 3/8 necesita 4 puntos")

def romberg():
    st.header("🚀 Integración de Romberg")
    
    st.info("Extrapolación de Richardson para integración")
    
    st.subheader("Ejercicio: Concepto de Romberg")
    st.write("¿Qué método combina Romberg para mejorar la precisión?")
    
    opcion_romberg = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "Trapecio con extrapolación de Richardson",
            "Simpson con interpolación",
            "Gauss con cuadratura",
            "Newton con diferencias"
        ],
        key="romberg_q"
    )
    
    if st.button("Verificar Romberg", key="check_romberg"):
        if opcion_romberg == "Trapecio con extrapolación de Richardson":
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! Romberg usa trapecio + Richardson")
        else:
            st.error("❌ Incorrecto. Romberg combina trapecio con extrapolación de Richardson")

def punto_fijo_sistemas():
    st.header("🔄 Punto Fijo para Sistemas NO Lineales")
    
    st.info("Resolución iterativa de sistemas no lineales")
    
    st.subheader("Ejercicio: Sistema Simple")
    st.write("Para el sistema:")
    st.latex(r"\begin{cases} x = \frac{y + 1}{2} \\ y = \frac{x}{2} \end{cases}")
    st.write("Con (x₀,y₀) = (0,0), calcula x₁:")
    
    user_x1_pf = st.number_input("x₁:", value=0.0, step=0.1)
    
    if st.button("Verificar Punto Fijo", key="check_pf"):
        x1_correcto = (0 + 1) / 2  # (y₀ + 1)/2
        check_answer_2(x1_correcto, user_x1_pf, 0.01)

def newton_sistemas():
    st.header("🎯 Método de Newton para Sistemas")
    
    st.info("Extensión multivariable del método de Newton")
    
    st.subheader("Ejercicio: Matriz Jacobiana")
    st.write("Para el sistema:")
    st.latex(r"\begin{cases} f(x,y) = x^2 + y^2 - 1 \\ g(x,y) = x - y \end{cases}")
    st.write("¿Cuál es el elemento J₁₁ de la matriz Jacobiana?")
    st.latex(r"J_{11} = \frac{\partial f}{\partial x}")
    
    user_jacobian = st.number_input("∂f/∂x:", value=0.0, step=0.1)
    
    if st.button("Verificar Jacobiana", key="check_jac"):
        jacobiano_correcto = 2  # ∂(x² + y² - 1)/∂x = 2x, evaluado en algún punto
        check_answer_2(jacobiano_correcto, user_jacobian, 0.01)

def quasi_newton():
    st.header("⚡ Método de Quasi-Newton")
    
    st.info("Métodos que aproximan la matriz Hessiana/Jacobiana")
    
    st.subheader("Ejercicio: Ventaja de Quasi-Newton")
    st.write("¿Cuál es la principal ventaja de Quasi-Newton sobre Newton tradicional?")
    
    opcion_qn = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "No requiere calcular derivadas",
            "Es siempre más rápido",
            "Siempre converge",
            "Usa menos memoria"
        ],
        key="qn_q"
    )
    
    if st.button("Verificar Quasi-Newton", key="check_qn"):
        if opcion_qn == "No requiere calcular derivadas":
            st.session_state.score_2 += 10
            st.session_state.exercises_completed_2 += 1
            st.success("🎉 ¡Correcto! Quasi-Newton evita cálculo exacto de derivadas")
        else:
            st.error("❌ Incorrecto. La ventaja principal es evitar el cálculo de derivadas")

# Para probar individualmente
if __name__ == "__main__":
    app()