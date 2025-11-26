import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def app():
    st.title("🔬 Ejemplos Interactivos - Métodos Numéricos")
    
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
            "2.5 Bairstow",
            "3.1 Inversión de Matrices",
            "3.2 Gauss",
            "3.3 Gauss-Jordan",
            "3.4 Jacobi",
            "3.5 Gauss-Seidel",
            "4.2 Cholesky",
            "4.3 Doolittle",
            "5.1 Método de Potencias"
        ]
    )
    
    if metodo == "1.2 Errores Numéricos":
        errores_numericos()
    elif metodo == "1.3 Propagación del Error":
        propagacion_error()
    elif metodo == "1.4 Orden de Convergencia":
        orden_convergencia()
    elif metodo == "2.1 Bisección":
        biseccion()
    elif metodo == "2.2 Falsa Posición":
        falsa_posicion()
    elif metodo == "2.3 Newton-Raphson":
        newton_raphson()
    elif metodo == "2.4 Secante":
        secante()
    elif metodo == "2.5 Bairstow":
        bairstow()
    elif metodo == "3.1 Inversión de Matrices":
        inversion_matrices()
    elif metodo == "3.2 Gauss":
        gauss()
    elif metodo == "3.3 Gauss-Jordan":
        gauss_jordan()
    elif metodo == "3.4 Jacobi":
        jacobi()
    elif metodo == "3.5 Gauss-Seidel":
        gauss_seidel()
    elif metodo == "4.2 Cholesky":
        cholesky()
    elif metodo == "4.3 Doolittle":
        doolittle()
    elif metodo == "5.1 Método de Potencias":
        metodo_potencias()

def errores_numericos():
    st.header("🔍 Errores de Redondeo y Truncamiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Error de Redondeo")
        num = st.number_input("Número decimal:", value=0.1, step=0.1)
        st.write(f"Valor ingresado: {num}")
        st.write(f"Representación en Python: {num:.20f}")
        st.write(f"Error absoluto: {abs(num - 0.1):.20f}")
        
        # Ejemplo de suma problemática
        st.write("**Ejemplo problemático:**")
        a = 0.1
        b = 0.2
        c = 0.3
        st.write(f"0.1 + 0.2 = {a + b}")
        st.write(f"¿0.1 + 0.2 == 0.3? {a + b == c}")
    
    with col2:
        st.subheader("Error de Truncamiento")
        x = st.slider("Valor de x para e^x:", 0.1, 2.0, 1.0, 0.1)
        n_terminos = st.slider("Número de términos Taylor:", 1, 10, 3)
        
        # Serie de Taylor truncada
        def taylor_exp(x, n):
            resultado = 0
            for i in range(n):
                resultado += (x**i) / np.math.factorial(i)
            return resultado
        
        real = np.exp(x)
        aprox = taylor_exp(x, n_terminos)
        error = abs(real - aprox)
        
        st.write(f"Valor real e^{x}: {real:.6f}")
        st.write(f"Aproximación: {aprox:.6f}")
        st.write(f"Error de truncamiento: {error:.6f}")

def propagacion_error():
    st.header("📈 Propagación del Error")
    
    st.write("Ingresa valores con sus errores:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        a = st.number_input("Valor a:", value=10.0)
        error_a = st.number_input("Error en a:", value=0.1)
        
    with col2:
        b = st.number_input("Valor b:", value=5.0)
        error_b = st.number_input("Error en b:", value=0.1)
    
    operacion = st.selectbox("Operación:", ["Suma", "Resta", "Multiplicación", "División"])
    
    if operacion == "Suma":
        resultado = a + b
        error_propagado = error_a + error_b
    elif operacion == "Resta":
        resultado = a - b
        error_propagado = error_a + error_b
    elif operacion == "Multiplicación":
        resultado = a * b
        error_propagado = abs(b * error_a) + abs(a * error_b)
    else:  # División
        resultado = a / b
        error_propagado = (abs(1/b * error_a) + abs(-a/(b**2) * error_b))
    
    st.write(f"**Resultado:** {resultado:.4f} ± {error_propagado:.4f}")
    st.write(f"**Error relativo:** {(error_propagado/abs(resultado))*100:.2f}%")

def orden_convergencia():
    st.header("📊 Orden de Convergencia")
    
    metodo = st.selectbox("Selecciona método:", 
                         ["Bisección (lineal)", "Newton (cuadrático)", "Secante (superlineal)"])
    
    n_iter = st.slider("Número de iteraciones:", 3, 10, 5)
    
    # Datos de ejemplo para diferentes órdenes
    if metodo == "Bisección (lineal)":
        errores = [1/(2**i) for i in range(n_iter)]
    elif metodo == "Newton (cuadrático)":
        errores = [1/(2**(2**i)) for i in range(n_iter)]
    else:  # Secante
        errores = [1/(1.6**i) for i in range(n_iter)]
    
    # Calcular órdenes aproximados
    ratios = []
    for i in range(1, len(errores)-1):
        ratio = np.log(errores[i+1]/errores[i]) / np.log(errores[i]/errores[i-1])
        ratios.append(ratio)
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    
    # Gráfica de errores
    ax[0].semilogy(range(n_iter), errores, 'bo-', markersize=8)
    ax[0].set_xlabel('Iteración')
    ax[0].set_ylabel('Error (escala log)')
    ax[0].set_title('Convergencia del Error')
    ax[0].grid(True)
    
    # Gráfica de órdenes
    if ratios:
        ax[1].plot(range(1, len(ratios)+1), ratios, 'ro-', markersize=8)
        ax[1].axhline(y=1, color='g', linestyle='--', label='Lineal (orden 1)')
        ax[1].axhline(y=2, color='b', linestyle='--', label='Cuadrático (orden 2)')
        ax[1].set_xlabel('Iteración')
        ax[1].set_ylabel('Orden estimado')
        ax[1].set_title('Orden de Convergencia')
        ax[1].legend()
        ax[1].grid(True)
    
    st.pyplot(fig)
    
    st.write("**Orden estimado promedio:**", f"{np.mean(ratios):.3f}" if ratios else "N/A")

def biseccion():
    st.header("🎯 Método de Bisección")
    
    st.write("Encuentra raíces de f(x) = 0 en [a,b]")
    
    # Función predefinida
    funcion = st.selectbox("Función:", 
                          ["x² - 4", "x³ - 2x - 5", "cos(x) - x", "e^x - 2"])
    
    if funcion == "x² - 4":
        f = lambda x: x**2 - 4
        a, b = 1, 3
    elif funcion == "x³ - 2x - 5":
        f = lambda x: x**3 - 2*x - 5
        a, b = 2, 3
    elif funcion == "cos(x) - x":
        f = lambda x: np.cos(x) - x
        a, b = 0, 1
    else:  # e^x - 2
        f = lambda x: np.exp(x) - 2
        a, b = 0, 1
    
    col1, col2 = st.columns(2)
    with col1:
        a_input = st.number_input("a:", value=float(a))
    with col2:
        b_input = st.number_input("b:", value=float(b))
    
    tol = st.number_input("Tolerancia:", value=1e-6, format="%.6f")
    max_iter = st.slider("Máximo iteraciones:", 1, 20, 10)
    
    if st.button("Calcular raíz"):
        if f(a_input) * f(b_input) >= 0:
            st.error("f(a) y f(b) deben tener signos opuestos")
            return
        
        resultados = []
        a_curr, b_curr = a_input, b_input
        
        for i in range(max_iter):
            c = (a_curr + b_curr) / 2
            fc = f(c)
            resultados.append((i+1, a_curr, b_curr, c, fc))
            
            if abs(fc) < tol:
                break
                
            if f(a_curr) * fc < 0:
                b_curr = c
            else:
                a_curr = c
        
        # Mostrar resultados
        df = pd.DataFrame(resultados, 
                         columns=["Iter", "a", "b", "c", "f(c)"])
        st.dataframe(df.style.format("{:.6f}"), use_container_width=True)
        
        st.success(f"Raíz aproximada: {c:.8f}")
        
        # Gráfica
        x_vals = np.linspace(a_input, b_input, 100)
        y_vals = f(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, 'b-', label='f(x)')
        ax.axhline(y=0, color='k', linestyle='--')
        ax.plot(c, fc, 'ro', markersize=8, label='Raíz encontrada')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

def falsa_posicion():
    st.header("📐 Método de Falsa Posición")
    
    st.write("Similar a bisección pero usa interpolación lineal")
    
    # Usamos las mismas funciones que bisección
    funcion = st.selectbox("Función:", 
                          ["x² - 4", "x³ - 2x - 5", "cos(x) - x"])
    
    if funcion == "x² - 4":
        f = lambda x: x**2 - 4
        a, b = 1, 3
    elif funcion == "x³ - 2x - 5":
        f = lambda x: x**3 - 2*x - 5
        a, b = 2, 3
    else:  # cos(x) - x
        f = lambda x: np.cos(x) - x
        a, b = 0, 1
    
    col1, col2 = st.columns(2)
    with col1:
        a_input = st.number_input("a:", value=float(a), key="falsa_a")
    with col2:
        b_input = st.number_input("b:", value=float(b), key="falsa_b")
    
    if st.button("Calcular con Falsa Posición"):
        if f(a_input) * f(b_input) >= 0:
            st.error("f(a) y f(b) deben tener signos opuestos")
            return
        
        resultados = []
        a_curr, b_curr = a_input, b_input
        
        for i in range(10):
            fa, fb = f(a_curr), f(b_curr)
            c = (a_curr * fb - b_curr * fa) / (fb - fa)
            fc = f(c)
            
            resultados.append((i+1, a_curr, b_curr, c, fc))
            
            if abs(fc) < 1e-6:
                break
                
            if fa * fc < 0:
                b_curr = c
            else:
                a_curr = c
        
        df = pd.DataFrame(resultados, 
                         columns=["Iter", "a", "b", "c", "f(c)"])
        st.dataframe(df.style.format("{:.6f}"), use_container_width=True)
        st.success(f"Raíz aproximada: {c:.8f}")

def newton_raphson():
    st.header("🚀 Método de Newton-Raphson")
    
    st.write("Método de convergencia rápida que usa derivadas")
    
    funcion = st.selectbox("Función:", 
                          ["x² - 4", "x³ - 2x - 5", "cos(x) - x"],
                          key="newton_func")
    
    if funcion == "x² - 4":
        f = lambda x: x**2 - 4
        df = lambda x: 2*x
        x0 = 2.5
    elif funcion == "x³ - 2x - 5":
        f = lambda x: x**3 - 2*x - 5
        df = lambda x: 3*x**2 - 2
        x0 = 2.0
    else:  # cos(x) - x
        f = lambda x: np.cos(x) - x
        df = lambda x: -np.sin(x) - 1
        x0 = 0.5
    
    x0_input = st.number_input("Valor inicial x0:", value=float(x0))
    
    if st.button("Ejecutar Newton-Raphson"):
        resultados = []
        x_curr = x0_input
        
        for i in range(10):
            fx = f(x_curr)
            dfx = df(x_curr)
            x_next = x_curr - fx/dfx
            error = abs(x_next - x_curr)
            
            resultados.append((i+1, x_curr, fx, dfx, x_next, error))
            
            if error < 1e-8:
                break
            x_curr = x_next
        
        df_result = pd.DataFrame(resultados, 
                               columns=["Iter", "x_n", "f(x_n)", "f'(x_n)", "x_{n+1}", "Error"])
        st.dataframe(df_result.style.format("{:.8f}"), use_container_width=True)
        st.success(f"Raíz encontrada: {x_curr:.10f}")

def secante():
    st.header("📏 Método de la Secante")
    
    st.write("Similar a Newton pero sin necesidad de derivadas")
    
    funcion = st.selectbox("Función:", 
                          ["x² - 4", "x³ - 2x - 5", "cos(x) - x"],
                          key="secante_func")
    
    if funcion == "x² - 4":
        f = lambda x: x**2 - 4
        x0, x1 = 1, 3
    elif funcion == "x³ - 2x - 5":
        f = lambda x: x**3 - 2*x - 5
        x0, x1 = 2, 3
    else:  # cos(x) - x
        f = lambda x: np.cos(x) - x
        x0, x1 = 0, 1
    
    col1, col2 = st.columns(2)
    with col1:
        x0_input = st.number_input("x0:", value=float(x0), key="sec_x0")
    with col2:
        x1_input = st.number_input("x1:", value=float(x1), key="sec_x1")
    
    if st.button("Ejecutar Secante"):
        resultados = []
        x_prev, x_curr = x0_input, x1_input
        
        for i in range(10):
            f_prev, f_curr = f(x_prev), f(x_curr)
            x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
            error = abs(x_next - x_curr)
            
            resultados.append((i+1, x_prev, x_curr, x_next, f_curr, error))
            
            if error < 1e-8:
                break
            x_prev, x_curr = x_curr, x_next
        
        df_result = pd.DataFrame(resultados, 
                               columns=["Iter", "x_{n-1}", "x_n", "x_{n+1}", "f(x_n)", "Error"])
        st.dataframe(df_result.style.format("{:.8f}"), use_container_width=True)
        st.success(f"Raíz encontrada: {x_curr:.10f}")

def bairstow():
    st.header("🎭 Método de Bairstow")
    
    st.write("Encuentra raíces de polinomios (reales y complejas)")
    
    st.info("""
    Ejemplo: Encontrar raíces de x³ - 6x² + 11x - 6 = 0
    Las raíces reales son x = 1, 2, 3
    """)
    
    # Coeficientes del polinomio: x³ - 6x² + 11x - 6
    coef = [1, -6, 11, -6]
    
    if st.button("Aplicar Bairstow (simulación)"):
        st.write("**Proceso simplificado:**")
        st.write("1. Factorización cuadrática inicial")
        st.write("2. Refinamiento iterativo")
        st.write("3. Extracción de raíces")
        
        raices = np.roots(coef)
        
        st.success("Raíces encontradas:")
        for i, raiz in enumerate(raices, 1):
            st.write(f"Raíz {i}: {raiz:.6f}")

def inversion_matrices():
    st.header("🔄 Inversión de Matrices")
    
    st.write("Ingresa una matriz 2x2 para invertir:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        a11 = st.number_input("a11", value=2.0)
        a21 = st.number_input("a21", value=1.0)
    
    with col2:
        a12 = st.number_input("a12", value=1.0)
        a22 = st.number_input("a22", value=1.0)
    
    A = np.array([[a11, a12], [a21, a22]])
    
    if st.button("Calcular inversa"):
        try:
            det = a11 * a22 - a12 * a21
            if abs(det) < 1e-10:
                st.error("Matriz singular - no tiene inversa")
            else:
                A_inv = np.linalg.inv(A)
                
                st.write("**Matriz original A:**")
                st.write(A)
                
                st.write("**Determinante:**", det)
                
                st.write("**Matriz inversa A⁻¹:**")
                st.write(A_inv)
                
                # Verificación
                I = A @ A_inv
                st.write("**Verificación A × A⁻¹:**")
                st.write(I)
                
        except np.linalg.LinAlgError:
            st.error("La matriz no es invertible")

def gauss():
    st.header("🎯 Eliminación Gaussiana")
    
    st.write("Resuelve sistemas de ecuaciones lineales")
    
    sistema = st.selectbox("Sistema ejemplo:", 
                          ["2x + y = 5, x - y = 1", 
                           "3x + 2y = 7, x + y = 3"])
    
    if sistema == "2x + y = 5, x - y = 1":
        A = np.array([[2, 1], [1, -1]])
        b = np.array([5, 1])
    else:
        A = np.array([[3, 2], [1, 1]])
        b = np.array([7, 3])
    
    st.write("**Matriz aumentada:**")
    Ab = np.column_stack((A, b))
    st.write(Ab)
    
    if st.button("Aplicar Eliminación Gaussiana"):
        # Eliminación hacia adelante
        n = len(b)
        Ab_work = Ab.astype(float).copy()
        
        st.write("**Proceso de eliminación:**")
        
        for i in range(n):
            # Pivote
            pivot = Ab_work[i, i]
            Ab_work[i, :] = Ab_work[i, :] / pivot
            
            st.write(f"Paso {i+1}:")
            st.write(Ab_work)
            
            # Eliminación
            for j in range(i+1, n):
                factor = Ab_work[j, i]
                Ab_work[j, :] = Ab_work[j, :] - factor * Ab_work[i, :]
        
        # Sustitución hacia atrás
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = Ab_work[i, -1] - np.sum(Ab_work[i, i+1:n] * x[i+1:n])
        
        st.success("**Solución:**")
        for i in range(n):
            st.write(f"x{i+1} = {x[i]:.2f}")

def gauss_jordan():
    st.header("🔷 Método de Gauss-Jordan")
    
    st.write("Encuentra la matriz inversa usando eliminación completa")
    
    A = np.array([[2, 1], [1, 3]])
    
    st.write("Matriz A:")
    st.write(A)
    
    if st.button("Aplicar Gauss-Jordan"):
        try:
            # Matriz aumentada [A|I]
            n = A.shape[0]
            I = np.eye(n)
            AI = np.hstack((A, I))
            
            st.write("Matriz aumentada [A|I]:")
            st.write(AI)
            
            # Simulación del proceso
            A_inv = np.linalg.inv(A)
            
            st.write("**Matriz inversa resultante A⁻¹:**")
            st.write(A_inv)
            
            # Verificación
            st.write("**Verificación A × A⁻¹:**")
            st.write(A @ A_inv)
            
        except np.linalg.LinAlgError:
            st.error("La matriz no es invertible")

def jacobi():
    st.header("🔄 Método de Jacobi")
    
    st.write("Método iterativo para sistemas lineales")
    
    st.info("Sistema: 4x + y = 7, x + 3y = 5")
    
    A = np.array([[4, 1], [1, 3]])
    b = np.array([7, 5])
    x0 = np.array([0, 0])
    
    n_iter = st.slider("Iteraciones Jacobi:", 1, 10, 5)
    
    if st.button("Ejecutar Jacobi"):
        resultados = []
        x = x0.copy()
        n = len(b)
        
        for k in range(n_iter):
            x_new = np.zeros(n)
            for i in range(n):
                suma = 0
                for j in range(n):
                    if j != i:
                        suma += A[i, j] * x[j]
                x_new[i] = (b[i] - suma) / A[i, i]
            
            error = np.linalg.norm(x_new - x)
            resultados.append((k+1, x_new[0], x_new[1], error))
            x = x_new.copy()
        
        df = pd.DataFrame(resultados, 
                         columns=["Iter", "x1", "x2", "Error"])
        st.dataframe(df.style.format("{:.6f}"), use_container_width=True)
        
        st.success(f"Solución aproximada: x1 = {x[0]:.6f}, x2 = {x[1]:.6f}")

def gauss_seidel():
    st.header("⚡ Método de Gauss-Seidel")
    
    st.write("Similar a Jacobi pero usa valores actualizados inmediatamente")
    
    st.info("Sistema: 4x + y = 7, x + 3y = 5")
    
    A = np.array([[4, 1], [1, 3]])
    b = np.array([7, 5])
    x0 = np.array([0, 0])
    
    n_iter = st.slider("Iteraciones Gauss-Seidel:", 1, 10, 5, key="gs_iter")
    
    if st.button("Ejecutar Gauss-Seidel"):
        resultados = []
        x = x0.copy()
        n = len(b)
        
        for k in range(n_iter):
            x_old = x.copy()
            for i in range(n):
                suma = 0
                for j in range(n):
                    if j != i:
                        suma += A[i, j] * x[j]
                x[i] = (b[i] - suma) / A[i, i]
            
            error = np.linalg.norm(x - x_old)
            resultados.append((k+1, x[0], x[1], error))
        
        df = pd.DataFrame(resultados, 
                         columns=["Iter", "x1", "x2", "Error"])
        st.dataframe(df.style.format("{:.6f}"), use_container_width=True)
        
        st.success(f"Solución aproximada: x1 = {x[0]:.6f}, x2 = {x[1]:.6f}")

def cholesky():
    st.header("🔺 Método de Cholesky")
    
    st.write("Factorización para matrices simétricas definidas positivas")
    
    A = np.array([[4, 2], [2, 5]])
    
    st.write("Matriz simétrica A:")
    st.write(A)
    
    if st.button("Aplicar Cholesky"):
        try:
            L = np.linalg.cholesky(A)
            st.write("**Factor L:**")
            st.write(L)
            
            st.write("**Verificación L × Lᵀ:**")
            st.write(L @ L.T)
            
        except np.linalg.LinAlgError:
            st.error("La matriz no es definida positiva")

def doolittle():
    st.header("🔧 Método de Doolittle")
    
    st.write("Factorización LU con 1's en la diagonal de L")
    
    A = np.array([[2, 1], [1, 3]])
    
    st.write("Matriz A:")
    st.write(A)
    
    if st.button("Aplicar Doolittle"):
        # Factorización LU manual para 2x2
        L = np.eye(2)
        U = np.zeros((2, 2))
        
        U[0, 0] = A[0, 0]
        U[0, 1] = A[0, 1]
        L[1, 0] = A[1, 0] / U[0, 0]
        U[1, 1] = A[1, 1] - L[1, 0] * U[0, 1]
        
        st.write("**Matriz L:**")
        st.write(L)
        
        st.write("**Matriz U:**")
        st.write(U)
        
        st.write("**Verificación L × U:**")
        st.write(L @ U)

def metodo_potencias():
    st.header("💪 Método de las Potencias")
    
    st.write("Encuentra el autovalor dominante de una matriz")
    
    A = np.array([[2, 1], [1, 3]])
    
    st.write("Matriz A:")
    st.write(A)
    
    x0 = np.array([1, 1])
    n_iter = st.slider("Iteraciones:", 1, 10, 5, key="potencias_iter")
    
    if st.button("Ejecutar Método de Potencias"):
        x = x0.copy()
        autovalor_approx = 0
        resultados = []
        
        for k in range(n_iter):
            # Multiplicar por A
            y = A @ x
            # Nueva aproximación del autovalor
            autovalor_new = np.linalg.norm(y, np.inf)
            # Normalizar
            x = y / autovalor_new
            
            resultados.append((k+1, autovalor_new, x[0], x[1]))
            autovalor_approx = autovalor_new
        
        df = pd.DataFrame(resultados, 
                         columns=["Iter", "Autovalor", "v1", "v2"])
        st.dataframe(df.style.format("{:.6f}"), use_container_width=True)
        
        # Autovalores reales para comparación
        autovalores_reales = np.linalg.eigvals(A)
        autovalor_dominante = max(autovalores_reales)
        
        st.success(f"Autovalor dominante aproximado: {autovalor_approx:.6f}")
        st.info(f"Autovalor dominante real: {autovalor_dominante:.6f}")