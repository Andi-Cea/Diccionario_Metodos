import streamlit as st

def app():
    st.title("🔢 Métodos Numéricos I ")

    # Sección 1.2
    st.markdown("## 1.2 Errores de Redondeo, Truncamiento, Absoluto y Relativo")

    st.markdown("### Aritmética de Punto Flotante")
    st.markdown("""
    **Definición:** Sistema para representar números reales en una computadora. Un número se expresa como:
    """)
    st.latex(r"\pm d_1.d_2d_3\ldots d_t \times \beta^e")
    st.markdown("""
    donde:
    - $\\beta$: Base (ej. 2, 10, 16)
    - $t$: Número de dígitos en la mantisa (precisión)
    - $e$: Exponente (entero)
    """)
    st.markdown("**Fuente de Error:** La memoria es finita, por lo que muchos números no pueden representarse con exactitud.")

    st.markdown("### Error de Truncamiento")
    st.markdown("""
    **Definición:** Error que se introduce cuando un proceso matemático infinito se "corta" o trunca para ser finito.
    **Ejemplo Clásico:** Usar un número finito de términos de una **Serie de Taylor**.
    """)

    st.markdown("### Polinomio de Taylor")
    st.markdown("**Definición:** Aproxima el valor de una función $f(x)$ alrededor de un punto $a$.")
    st.markdown("**Fórmula:**")
    st.latex(r"P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n")
    st.markdown("**Error de Truncamiento (Resto de Lagrange):**")
    st.latex(r"R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{(n+1)}")
    st.markdown("donde $\\xi$ es un número entre $x$ y $a$.")

    st.markdown("### Error Absoluto (EA)")
    st.markdown("**Definición:** Diferencia entre el valor verdadero ($VV$) y el valor aproximado ($VA$).")
    st.markdown("**Fórmula:**")
    st.latex(r"EA = |VV - VA|")

    st.markdown("### Error Relativo (ER)")
    st.markdown("**Definición:** Error absoluto en relación al valor verdadero.")
    st.markdown("**Fórmula:**")
    st.latex(r"ER = \frac{|VV - VA|}{|VV|}")
    st.markdown("**Error Relativo Porcentual:**")
    st.latex(r"ER\% = ER \times 100\%")

    # Sección 1.3
    st.markdown("## 1.3 Propagación del Error en Operaciones Aritméticas")
    st.markdown("Si $x_a$ e $y_a$ son aproximaciones a $x$ e $y$ con errores $\\Delta x$ e $\\Delta y$:")

    st.markdown("**Suma/Resta:**")
    st.latex(r"\Delta (x_a \pm y_a) \approx \Delta x + \Delta y")

    st.markdown("**Multiplicación:**")
    st.latex(r"\Delta (x_a \cdot y_a) \approx |x_a| \Delta y + |y_a| \Delta x")

    st.markdown("**División:**")
    st.latex(r"\Delta \left( \frac{x_a}{y_a} \right) \approx \frac{|y_a| \Delta x + |x_a| \Delta y}{|y_a|^2}")

    # Sección 1.4
    st.markdown("## 1.4 Orden de Convergencia")
    st.markdown("""
    **Definición:** Mide la velocidad a la que una sucesión iterativa $\\{p_n\\}$ se acerca a su límite $L$.
    **Definición Formal:** Si existe una constante $\\lambda > 0$ y un entero $N$ tal que para toda $n \\geq N$:
    """)
    st.latex(r"|p_{n+1} - L| \leq \lambda |p_n - L|^\alpha")
    st.markdown("""
    entonces la sucesión converge con **orden $\\alpha$**.
    - $\\alpha = 1$: Convergencia lineal
    - $\\alpha = 2$: Convergencia cuadrática
    - $\\alpha > 1$: Convergencia superlineal
    """)

    # Sección 2.1
    st.markdown("## 2.1 Método de Bisección")
    st.markdown("""
    **Definición:** Método cerrado para encontrar raíces. Requiere un intervalo $[a, b]$ donde $f(a) \\cdot f(b) < 0$ (Teorema de Bolzano).
    **Algoritmo:**
    1. Calcular el punto medio: 
    """)
    st.latex(r"p = \frac{a + b}{2}")
    st.markdown("""
    2. Si $f(a) \\cdot f(p) < 0$, la raíz está en $[a, p]$ $\\rightarrow$ $b = p$
    3. Si no, la raíz está en $[p, b]$ $\\rightarrow$ $a = p$
    """)
    st.markdown("**Convergencia:** Lineal. El error se reduce a la mitad en cada iteración.")

    # Sección 2.2
    st.markdown("## 2.2 Método de Falsa Posición (Regula Falsi)")
    st.markdown("""
    **Definición:** Método cerrado que mejora la bisección. Usa la intersección con el eje x de la secante entre $(a, f(a))$ y $(b, f(b))$.
    """)
    st.markdown("**Fórmula:**")
    st.latex(r"p = b - f(b) \cdot \frac{a - b}{f(a) - f(b)}")
    st.markdown("o equivalentemente:")
    st.latex(r"p = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}")
    st.markdown("**Convergencia:** Generalmente superlineal.")

    # Sección 2.3
    st.markdown("## 2.3 Método de Newton (Newton-Raphson)")
    st.markdown("**Definición:** Método abierto que utiliza la tangente a la función en un punto inicial.")
    st.markdown("**Fórmula Iterativa:**")
    st.latex(r"p_{n+1} = p_n - \frac{f(p_n)}{f'(p_n)}")
    st.markdown("**Convergencia:** Cuadrática, si $f'(p_n) \\neq 0$ y la estimación inicial es buena.")

    # Sección 2.4
    st.markdown("## 2.4 Método de la Secante")
    st.markdown("**Definición:** Similar a Newton, pero evita el cálculo de la derivada.")
    st.markdown("**Fórmula Iterativa:**")
    st.latex(r"p_{n+1} = p_n - f(p_n) \cdot \frac{p_n - p_{n-1}}{f(p_n) - f(p_{n-1})}")
    st.markdown("**Convergencia:** Superlineal (con orden $\\alpha \\approx 1.618$).")

    # Sección 2.5
    st.markdown("## 2.5 Método de Bairstow")
    st.markdown("""
    **Definición:** Método para encontrar raíces (reales y complejas) de un polinomio. Encuentra factores cuadráticos.
    **Algoritmo:** Dado un polinomio $P(x)$, busca un factor cuadrático $x^2 + ux + v$.
    **Proceso Iterativo:**
    1. Se realiza una división sintética de $P(x)$ entre $x^2 + ux + v$, obteniendo un cociente $Q(x)$ y un residuo $R(x) = b_1(x + u) + b_0$.
    2. El objetivo es encontrar $u$ y $v$ tales que $b_1 = 0$ y $b_0 = 0$.
    3. Se resuelve el sistema:
    """)
    st.latex(r"""
    \begin{cases}
    c_1 \Delta u + c_2 \Delta v = -b_1 \\
    c_2 \Delta u + c_3 \Delta v = -b_0
    \end{cases}
    """)
    st.markdown("""
    (donde $c_1, c_2, c_3$ se obtienen de una segunda división sintética).
    4. Se actualizan los valores: $u = u + \\Delta u$, $v = v + \\Delta v$.
    """)
    st.markdown("**Convergencia:** Cuadrática.")

    # Sección 3.1
    st.markdown("## 3.1 Sistemas Lineales y Matrices")
    
    st.markdown("### Condiciones Necesarias y Suficientes")
    st.markdown("Para un sistema de ecuaciones lineales $A\\mathbf{x} = \\mathbf{b}$, donde $A \\in \\mathbb{R}^{n \\times n}$:")
    st.markdown("""
    **Existencia y Unicidad:** El sistema tiene solución única si y solo si:
    """)
    st.latex(r"\det(A) \neq 0")
    st.markdown("o equivalentemente, si $A$ es una matriz **no singular**.")
    st.markdown("**Condición de Rango:**")
    st.latex(r"\text{rank}(A) = \text{rank}([A|\mathbf{b}]) = n")
    st.markdown("**Independencia Lineal:** Las columnas de $A$ deben ser linealmente independientes.")

    st.markdown("### 3.1.1 Inversión de Matrices")
    st.markdown("""
    **Definición:** Dada una matriz cuadrada $A$, su inversa $A^{-1}$ satisface:
    """)
    st.latex(r"A \cdot A^{-1} = A^{-1} \cdot A = I")
    st.markdown("donde $I$ es la matriz identidad.")
    st.markdown("**Condición de Existencia:** $A^{-1}$ existe si y solo si $\\det(A) \\neq 0$.")
    st.markdown("**Propiedad:** Si $A^{-1}$ existe, la solución del sistema $A\\mathbf{x} = \\mathbf{b}$ es:")
    st.latex(r"\mathbf{x} = A^{-1}\mathbf{b}")

    st.markdown("### 3.1.2 Método de Intercambio")
    st.markdown("""
    **Objetivo:** Reorganizar ecuaciones o variables para mejorar la estabilidad numérica.
    **Procedimiento:** Intercambiar filas (o columnas) de la matriz para colocar el elemento de mayor magnitud en la posición pivotal.
    **Ventaja:** Reduce los errores de redondeo en la eliminación gaussiana.
    """)

    # Sección 3.2
    st.markdown("## 3.2 Métodos Exactos")

    st.markdown("### 3.2.1 Método de Gauss y Pivoteo Parcial")
    st.markdown("""
    **Objetivo:** Transformar el sistema en uno triangular superior mediante operaciones elementales de fila.
    **Algoritmo:**
    1. Para $k = 1$ hasta $n-1$:
        - **Pivoteo Parcial:** Encontrar $p$ tal que $|a_{pk}| = \\max_{i \\geq k} |a_{ik}|$
        - Intercambiar filas $k$ y $p$ si es necesario
        - Para $i = k+1$ hasta $n$:
        """)
    st.latex(r"m_{ik} = \frac{a_{ik}}{a_{kk}}")
    st.markdown("        - Para $j = k$ hasta $n+1$:")
    st.latex(r"a_{ij} = a_{ij} - m_{ik} \cdot a_{kj}")
    st.markdown("    2. Resolver por sustitución regresiva.")
    st.markdown("**Pivoteo Parcial:** Selecciona el elemento de mayor magnitud en la columna como pivote.")

    st.markdown("### 3.2.2 Método de Gauss-Jordan y Pivoteo Total")
    st.markdown("""
    **Objetivo:** Transformar la matriz aumentada $[A|\\mathbf{b}]$ en $[I|\\mathbf{x}]$ directamente.
    **Algoritmo:**
    1. Para $k = 1$ hasta $n$:
        - **Pivoteo Total:** Encontrar $p,q$ tal que $|a_{pq}| = \\max_{i,j \\geq k} |a_{ij}|$
        - Intercambiar filas $k$ y $p$, columnas $k$ y $q$
        - Normalizar: $a_{kj} = \\frac{a_{kj}}{a_{kk}}$ para $j = k+1,\\ldots,n+1$
        - Para $i = 1$ hasta $n$, $i \\neq k$:
        """)
    st.latex(r"a_{ij} = a_{ij} - a_{ik} \cdot a_{kj} \quad \text{para } j = k+1,\ldots,n+1")
    st.markdown("**Pivoteo Total:** Selecciona el elemento de mayor magnitud en la submatriz restante.")

    st.markdown("### 3.3.3 Gauss-Jordan Particionado")
    st.markdown("""
    **Definición:** Versión del método Gauss-Jordan que opera sobre particiones de la matriz para mejorar eficiencia en matrices grandes.
    **Forma Matricial:** Se expresa la eliminación en términos de operaciones con bloques:
    """)
    st.latex(r"""
    \begin{bmatrix}
    A_{11} & A_{12} \\
    A_{21} & A_{22}
    \end{bmatrix}
    \rightarrow
    \begin{bmatrix}
    I & A_{11}^{-1}A_{12} \\
    0 & A_{22} - A_{21}A_{11}^{-1}A_{12}
    \end{bmatrix}
    """)
    st.markdown("**Ventaja:** Permite procesamiento paralelo y es más eficiente para matrices de gran tamaño.")

    # Sección 3.4
    st.markdown("## 3.4 Métodos Iterativos")

    st.markdown("### 3.4.1 Mejoramiento Iterativo de la Solución")
    st.markdown("""
    **Objetivo:** Refinar una solución aproximada $\\mathbf{x}^{(0)}$ obtenida por métodos directos.
    **Algoritmo:**
    1. Calcular el residual: $\\mathbf{r}^{(k)} = \\mathbf{b} - A\\mathbf{x}^{(k)}$
    2. Resolver $A\\mathbf{d}^{(k)} = \\mathbf{r}^{(k)}$ para $\\mathbf{d}^{(k)}$
    3. Actualizar: $\\mathbf{x}^{(k+1)} = \\mathbf{x}^{(k)} + \\mathbf{d}^{(k)}$
    """)
    st.markdown("**Convergencia:** Si $\\|A^{-1}\\mathbf{r}^{(k)}\\| < \\|\\mathbf{x}^{(k)}\\|$, el proceso converge.")

    st.markdown("### 3.4.2 Método de Jacobi")
    st.markdown("""
    **Descomposición:** $A = D - L - U$, donde:
    - $D$: matriz diagonal
    - $L$: matriz triangular inferior estricta
    - $U$: matriz triangular superior estricta
    """)
    st.markdown("**Fórmula Iterativa:**")
    st.latex(r"x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1, j\neq i}^{n} a_{ij}x_j^{(k)} \right), \quad i = 1,\ldots,n")
    st.markdown("**Forma Matricial:**")
    st.latex(r"\mathbf{x}^{(k+1)} = D^{-1}((L + U)\mathbf{x}^{(k)} + \mathbf{b})")
    st.markdown("**Condición de Convergencia:** $A$ debe ser estrictamente diagonal dominante.")

    st.markdown("### 3.4.3 Método de Gauss-Seidel")
    st.markdown("**Diferencia con Jacobi:** Usa los valores más recientes disponibles en cada iteración.")
    st.markdown("**Fórmula Iterativa:**")
    st.latex(r"x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)} \right)")
    st.markdown("**Forma Matricial:**")
    st.latex(r"\mathbf{x}^{(k+1)} = (D - L)^{-1}(U\mathbf{x}^{(k)} + \mathbf{b})")
    st.markdown("**Convergencia:** Generalmente más rápido que Jacobi. Converge si $A$ es definida positiva o estrictamente diagonal dominante.")

    st.markdown("### 3.4.4 Método de Relajación (SOR)")
    st.markdown("**Objetivo:** Acelerar la convergencia de Gauss-Seidel mediante un parámetro de relajación $\\omega$.")
    st.markdown("**Fórmula Iterativa:**")
    st.latex(r"x_i^{(k+1)} = (1-\omega)x_i^{(k)} + \frac{\omega}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)} \right)")
    st.markdown("**Parámetro $\\omega$:**")
    st.markdown("""
    - $0 < \\omega < 1$: Sub-relajación (mayor estabilidad)
    - $\\omega = 1$: Equivalente a Gauss-Seidel
    - $1 < \\omega < 2$: Sobre-relajación (acelera convergencia)
    """)
    st.markdown("**Forma Matricial:**")
    st.latex(r"\mathbf{x}^{(k+1)} = (D - \omega L)^{-1}((1-\omega)D + \omega U)\mathbf{x}^{(k)} + \omega(D - \omega L)^{-1}\mathbf{b}")
    st.markdown("**Convergencia:** Requiere $0 < \\omega < 2$ para matrices definidas positivas.")

    # Sección 4.1
    st.markdown("## 4.1 Modelos de Contexto y Comportamiento")
    st.markdown("""
    **Modelos de Contexto:**
    - Describen el entorno y condiciones bajo las cuales se aplican los métodos numéricos
    - Incluyen: tipo de matriz (definida positiva, banda, dispersa), precisión requerida, recursos computacionales disponibles
    - Ejemplo: Elegir entre métodos directos o iterativos según el tamaño y estructura del sistema

    **Modelos de Comportamiento:**
    - Describen cómo se comportan los algoritmos bajo diferentes condiciones
    - Análisis de: estabilidad numérica, complejidad computacional, convergencia, sensibilidad a perturbaciones
    - Ejemplo: Estudio del número de condición de una matriz para predecir la propagación de errores
    """)

    # Sección 4.2
    st.markdown("## 4.2 Método de Cholesky")
    st.markdown("""
    **Definición:** Método de factorización para matrices simétricas y definidas positivas.
    **Condiciones de Aplicación:**
    - $A$ debe ser simétrica: $A = A^T$
    - $A$ debe ser definida positiva: $\\mathbf{x}^T A \\mathbf{x} > 0$ para todo $\\mathbf{x} \\neq 0$
    - Todos los autovalores de $A$ deben ser positivos
    """)
    st.markdown("**Factorización:**")
    st.latex(r"A = LL^T")
    st.markdown("donde $L$ es una matriz triangular inferior.")
    st.markdown("**Algoritmo:** Para $i = 1$ hasta $n$:")
    st.latex(r"""
    \begin{aligned}
    l_{ii} &= \sqrt{a_{ii} - \sum_{k=1}^{i-1} l_{ik}^2} \\
    l_{ji} &= \frac{1}{l_{ii}} \left( a_{ji} - \sum_{k=1}^{i-1} l_{jk} l_{ik} \right), \quad j = i+1,\ldots,n
    \end{aligned}
    """)
    st.markdown("""
    **Ventajas:**
    - Más eficiente que LU (aproximadamente la mitad de operaciones)
    - Mejor estabilidad numérica
    - Solo necesita almacenar la matriz triangular inferior
    """)

    # Sección 4.3
    st.markdown("## 4.3 Método de Doolittle")
    st.markdown("""
    **Definición:** Variante de la factorización LU donde los elementos diagonales de $L$ son 1.
    **Factorización:**
    """)
    st.latex(r"A = LU")
    st.markdown("""
    donde:
    - $L$: triangular inferior con $l_{ii} = 1$
    - $U$: triangular superior
    """)
    st.markdown("**Algoritmo:** Para $k = 1$ hasta $n$:")
    st.latex(r"""
    \begin{aligned}
    u_{kj} &= a_{kj} - \sum_{m=1}^{k-1} l_{km} u_{mj}, \quad j = k,\ldots,n \\
    l_{ik} &= \frac{1}{u_{kk}} \left( a_{ik} - \sum_{m=1}^{k-1} l_{im} u_{mk} \right), \quad i = k+1,\ldots,n
    \end{aligned}
    """)
    st.markdown("""
    **Aplicación:** Resolver $A\\mathbf{x} = \\mathbf{b}$ mediante:
    1. Resolver $L\\mathbf{y} = \\mathbf{b}$ (sustitución hacia adelante)
    2. Resolver $U\\mathbf{x} = \\mathbf{y}$ (sustitución hacia atrás)
    """)

    # Sección 4.4
    st.markdown("## 4.4 Solución de Sistemas Bandados (Método de Crout)")
    st.markdown("""
    **Definición:** Factorización LU optimizada para matrices bandadas.
    **Matriz Bandada:** Matriz donde los elementos no nulos se concentran alrededor de la diagonal principal.
    **Factorización de Crout:**
    """)
    st.latex(r"A = LU")
    st.markdown("""
    donde:
    - $L$: triangular inferior
    - $U$: triangular superior con $u_{ii} = 1$
    """)
    st.markdown("**Algoritmo:** Para $j = 1$ hasta $n$:")
    st.latex(r"""
    \begin{aligned}
    l_{ij} &= a_{ij} - \sum_{k=1}^{j-1} l_{ik} u_{kj}, \quad i = j,\ldots,\min(j+p,n) \\
    u_{ji} &= \frac{1}{l_{jj}} \left( a_{ji} - \sum_{k=1}^{j-1} l_{jk} u_{ki} \right), \quad i = j+1,\ldots,\min(j+q,n)
    \end{aligned}
    """)
    st.markdown("donde $p$ y $q$ son los anchos de banda inferior y superior.")
    st.markdown("""
    **Ventajas:**
    - Reduce complejidad computacional de $O(n^3)$ a $O(npq)$
    - Menor requerimiento de memoria
    - Mantiene la estructura de banda
    """)

    # Sección 5.1
    st.markdown("## 5.1 Método de Potencias")
    st.markdown("**Objetivo:** Encontrar el autovalor de mayor magnitud y su autovector correspondiente.")
    st.markdown("**Algoritmo:**")
    st.markdown("1. Escoger vector inicial $\\mathbf{v}_0$ (normalmente $\\|\\mathbf{v}_0\\| = 1$)")
    st.markdown("2. Para $k = 1, 2, \\ldots$ hasta convergencia:")
    st.latex(r"""
    \begin{aligned}
    \mathbf{w}_k &= A\mathbf{v}_{k-1} \\
    \mathbf{v}_k &= \frac{\mathbf{w}_k}{\|\mathbf{w}_k\|} \\
    \lambda_k &= \mathbf{v}_k^T A \mathbf{v}_k
    \end{aligned}
    """)
    st.markdown("**Convergencia:**")
    st.latex(r"|\lambda^{(k)} - \lambda_1| = O\left( \left| \frac{\lambda_2}{\lambda_1} \right|^k \right)")
    st.markdown("""
    donde $\\lambda_1$ es el autovalor dominante y $\\lambda_2$ el siguiente en magnitud.
    **Aplicaciones:**
    - Cálculo del radio espectral
    - Análisis de estabilidad de sistemas
    - Algoritmo PageRank de Google
    """)

    # Sección 5.2
    st.markdown("## 5.2 Transformación de Householder")
    st.markdown("**Definición:** Transformación ortogonal que refleja vectores sobre un hiperplano.")
    st.markdown("**Matriz de Householder:**")
    st.latex(r"H = I - 2\frac{\mathbf{v}\mathbf{v}^T}{\mathbf{v}^T\mathbf{v}}")
    st.markdown("donde $\\mathbf{v}$ es el vector de reflexión.")
    st.markdown("""
    **Propiedades:**
    - Ortogonal: $H^T H = I$
    - Simétrica: $H = H^T$
    - Involutiva: $H^2 = I$
    """)
    st.markdown("**Construcción:** Dado un vector $\\mathbf{x}$, para encontrar $H$ tal que $H\\mathbf{x} = \\alpha\\mathbf{e}_1$:")
    st.latex(r"""
    \begin{aligned}
    \mathbf{v} &= \mathbf{x} \pm \|\mathbf{x}\|\mathbf{e}_1 \\
    \alpha &= \mp \|\mathbf{x}\|
    \end{aligned}
    """)
    st.markdown("**Aplicación en QR:** Reducir matriz a forma triangular superior:")
    st.latex(r"H_n H_{n-1} \cdots H_1 A = R")

    # Sección 5.3
    st.markdown("## 5.3 Iteración QR")
    st.markdown("**Objetivo:** Calcular todos los autovalores de una matriz.")
    st.markdown("**Algoritmo Básico:**")
    st.markdown("1. $A_1 = A$")
    st.markdown("2. Para $k = 1, 2, \\ldots$ hasta convergencia:")
    st.latex(r"""
    \begin{aligned}
    A_k &= Q_k R_k \quad \text{(Factorización QR)} \\
    A_{k+1} &= R_k Q_k
    \end{aligned}
    """)
    st.markdown("""
    **Propiedades:**
    - $A_{k+1}$ es unitariamente similar a $A_k$: $A_{k+1} = Q_k^T A_k Q_k$
    - Los autovalores se preservan en cada iteración
    - Bajo condiciones adecuadas, $A_k$ converge a forma triangular superior (Schur)
    """)
    st.markdown("**Versiones Mejoradas:**")
    st.markdown("""
    - **QR con desplazamiento:** $A_k - \\mu_k I = Q_k R_k$, $A_{k+1} = R_k Q_k + \\mu_k I$
    - **QR con doble desplazamiento:** Para matrices reales con autovalores complejos
    - **QR para matrices de Hessenberg:** Reduce costo computacional
    """)
    st.markdown("**Convergencia:**")
    st.latex(r"(a_{k+1})_{i,i-1} \rightarrow 0 \quad \text{y} \quad (a_k)_{ii} \rightarrow \lambda_i")
    st.markdown("""
    **Aplicaciones:**
    - Resolver problemas de autovalores completos
    - Análisis de sistemas dinámicos
    - Análisis de estabilidad en ingeniería
    """)

if __name__ == "__main__":
    app()

