import streamlit as st

def app():
    st.title("📊 Métodos Numéricos: Interpolación e Integración")

    # Sección 1.2
    st.markdown("## 1.2 Interpolación Polinomial")
    
    st.markdown("""
    **Definición:** Una función de interpolación es aquella que pasa a través de puntos dados como datos, 
    la cual puede hacerse mediante un polinomio. La interpolación polinómica (ajustar un polinomio a los puntos dados) 
    consiste en determinar el polinomio único de n-ésimo grado que se ajuste a $n + 1$ datos. Este polinomio, 
    entonces proporciona una fórmula para calcular los valores intermedios.

    Son varios los métodos que podemos usar para construir el polinomio de interpolación: 
    resolver un sistema de ecuaciones lineales para hallar sus coeficientes, usar los polinomios de Lagrange, entre otros.
    """)
    
    st.markdown("**Fórmula:** Si $x = x_0$ sustituyendo en la serie de Taylor:")
    st.latex(r"""
    f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \frac{f'''(x_0)}{3!}(x - x_0)^3 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n
    """)

    # Sección 2.2
    st.markdown("## 2.2 Fórmula de Lagrange")
    
    st.markdown("**Definición:**")
    st.markdown("""
    - En análisis numérico, el polinomio de Lagrange, llamado así en honor a Joseph-Louis de Lagrange, 
    es el polinomio que interpola un conjunto de puntos dado en la forma de Lagrange. 
    Fue descubierto por Edward Waring en 1779 y redescubierto más tarde por Leonhard Euler en 1783.
    
    - Dado que existe un único polinomio interpolador para un determinado conjunto de puntos, 
    resulta algo confuso llamar a este polinomio el polinomio interpolador de Lagrange. 
    Un nombre más conciso es interpolación polinómica en la forma de Lagrange.
    """)
    
    st.markdown("**Fórmula:**")
    st.latex(r"P(x) = \sum_{i=0}^{n} L_i(x) \cdot f(x_i)")
    st.latex(r"L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{(x - x_j)}{(x_i - x_j)}")

    # Sección 3.2
    st.markdown("## 3.2 Interpolación de Newton, Diferencias Finitas")
    
    st.markdown("### 1.1.2. Diferencias Finitas")
    st.markdown("""
    Consideremos una función $y = f(x)$ definida en forma tabular, para la que se desconoce la expresión analítica de $f(x)$. 
    Dados los valores $x_0, x_1 = x_0 + h, x_2 = x_0 + 2h, \\ldots, x_n = x_0 + nh$, 
    todos ellos igualmente espaciados entre sí ($x_k = x_0 + kh$), de la variable independiente $x$, 
    se conocen los correspondientes valores $y_0, y_1, y_2, \\ldots, y_n$, de la variable dependiente $y$.
    """)
    
    st.markdown("**Tabla de Valores:**")
    st.markdown("""
    | $x_i$ | $y_i$ |
    |-------|-------|
    | $x_0$ | $y_0$ |
    | $x_1 = x_0 + h$ | $y_1$ |
    | $x_2 = x_0 + 2h$ | $y_2$ |
    | $x_3 = x_0 + 3h$ | $y_3$ |
    | $\\vdots$ | $\\vdots$ |
    | $x_n = x_0 + nh$ | $y_n$ |
    """)
    
    st.markdown("**Corolario**")
    st.markdown("""
    Si en el proceso de la obtención de las diferencias sucesivas de la función, una de estas diferencias se vuelve constante 
    (o aproximadamente constante), puede afirmarse que el conjunto de valores tabulados queda satisfecho exactamente 
    (o muy aproximadamente) por un polinomio de grado igual al orden de la diferencia constante.
    """)
    
    st.markdown("**Tabla de Diferencias Finitas:**")
    st.latex(r"""
    \begin{array}{cccccc}
    x_i & y_i & \Delta y_i & \Delta^2 y_i & \Delta^3 y_i & \Delta^4 y_i \\
    \hline
    x_0 & y_0 & a_0 = y_1 - y_0 & b_0 = a_1 - a_0 & c_0 = b_1 - b_0 & d_0 = c_1 - c_0 \\
    x_1 & y_1 & a_1 = y_2 - y_1 & b_1 = a_2 - a_1 & c_1 = b_2 - b_1 & d_1 = c_2 - c_1 \\
    x_2 & y_2 & a_2 = y_3 - y_2 & b_2 = a_3 - a_2 & c_2 = b_3 - b_2 & \\
    x_3 & y_3 & a_3 = y_4 - y_3 & & & \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \\
    x_{n-1} & y_{n-1} & & b_{n-2} = a_{n-1} - a_{n-2} & & \\
    x_n & y_n & a_{n-1} = y_n - y_{n-1} & & c_{n-3} = b_{n-2} - b_{n-3}& d_{n-4} = c_{n-3} - c_{n-4}\\
    \end{array}
    """)

    # Sección 4.2
    st.markdown("## 4.2 Diferencias Divididas")
    
    st.markdown("**Definición:**")
    st.markdown("""
    En análisis numérico, la interpolación polinómica es una técnica de interpolación de un conjunto de datos 
    o de una función por un polinomio. Es decir, dado cierto número de puntos obtenidos por muestreo o a partir 
    de un experimento se pretende encontrar un polinomio que pase por todos los puntos.

    Dada una función $f$ de la cual se conocen sus valores en un número finito de abscisas $x_0, x_1, \\ldots, x_m$, 
    se llama interpolación polinómica al proceso de hallar un polinomio $p_m(x)$ de grado menor o igual a $m$.
    """)
    
    st.markdown("**Fórmula de Diferencias Divididas hacia adelante:**")
    st.latex(r"""
    \begin{aligned}
    f(X_k) = & f(X_0) + (X_k - X_0)f[X_0, X_1] + (X_k - X_1)(X_k - X_0)f[X_0, X_1, X_2] \\
    & + (X_k - X_2)(X_k - X_1)(X_k - X_0)f[X_0, X_1, X_2, X_3] + \ldots \\
    & + (X_k - X_{k-1}) \ldots (X_k - X_0)f[X_0, \ldots, X_n]
    \end{aligned}
    """)
    
    st.markdown("**Fórmula de Diferencias Divididas hacia atrás:**")
    st.latex(r"""
    \begin{aligned}
    f(X_k) = & f(X_n) + (X_k - X_n)f[X_{n-1}, X_n] + (X_k - X_n)(X_k - X_{n-1})f[X_{n-2}, X_{n-1}, X_n] \\
    & + \ldots + (X_k - X_n)\ldots(X_k - X_{k+1})f[X_k, \ldots, X_n]
    \end{aligned}
    """)
    
    st.markdown("**Tabla de Diferencias Divididas:**")
    st.latex(r"""
    \begin{array}{|c|c|c|c|c|}
    \hline
    x_i & f_i = f[x_i] & f[x_i, x_{i+1}] & f[x_i, x_{i+1}, x_{i+2}] & f[x_i, x_{i+1}, x_{i+2}, x_{i+3}] \\
    \hline
    x_0 & f_0 & f[x_0, x_1] = \frac{f_1 - f_0}{x_1 - x_0} & f[x_0, x_1, x_2] = \frac{f[x_1, x_2] - f[x_0, x_1]}{x_2 - x_0} & f[x_0, x_1, x_2, x_3] = \frac{f[x_1, x_2, x_3] - f[x_0, x_1, x_2]}{x_3 - x_0} \\
    \hline
    x_1 & f_1 & f[x_1, x_2] = \frac{f_2 - f_1}{x_2 - x_1} & f[x_1, x_2, x_3] = \frac{f[x_2, x_3] - f[x_1, x_2]}{x_3 - x_1} & f[x_1, x_2, x_3, x_4] \\
    \hline
    x_2 & f_2 & f[x_2, x_3] = \frac{f_3 - f_2}{x_3 - x_2} & f[x_2, x_3, x_4] = \frac{f[x_3, x_4] - f[x_2, x_3]}{x_4 - x_2} &  \\
    \hline
    x_3 & f_3 & f[x_3, x_4] = \frac{f_4 - f_3}{x_4 - x_3} &  &  \\
    \hline
    x_4 & f_4 & & \\
    \hline
    \end{array}
    """)

    # Sección 5.2
    st.markdown("## 5.2 Interpolación de Hermite")
    
    st.markdown("**Introducción:**")
    st.markdown("""
    La interpolación de Hermite es un método de interpolación. Consiste en buscar un polinomio $H_n(x)$ por pedazos 
    que sea cúbico en cada subintervalo $[x_{i-1}, x_i]$, $1 \\leq i \\leq n$ y que cumpla $f'(x)$ en los puntos 
    $\\{x_0, \\ldots, x_n\\}$, donde $f(x)$ es la función que se quiere interpolar.

    La función $H_n(x)$ queda determinada en forma única por estas condiciones y su cálculo requiere de la solución 
    de $n$ sistemas lineales de ecuaciones de tamaño 4x4 cada uno.
    """)
    
    st.markdown("**Polinomio de Hermite:**")
    st.latex(r"""
    \begin{aligned}
    H_{2n+1}(x_k) = & f(z_0) + (x_k - z_0)f[z_0, z_1] + (x_k - z_1)(x_k - z_0)f[z_0, z_1, z_2] \\
    & + (x_k - z_2)(x_k - z_1)(x_k - z_0)f[z_0, z_1, z_2, z_3] + \cdots \\
    & + (x_k - z_{k-1})\cdots(x_k - z_0)f[z_0, \ldots, z_k]
    \end{aligned}
    """)
    
    st.markdown("**Tabla de Diferencias Divididas para Hermite:**")
    st.latex(r"""
    \begin{array}{|c|c|c|c|}
    \hline
    x_i & f(x_i) & f[x_i, x_{i+1}] & f[x_i, x_{i+1}, x_{i+2}] \\
    \hline
    z_0 = x_0 & f[z_0] = f(x_0) & f[z_0, z_1] = f'(x_0) & f[z_0, z_1, z_2] = \frac{f[z_1, z_2] - f[z_0, z_1]}{z_2 - z_0} \\
    \hline
    z_1 = x_0 & f[z_1] = f(x_0) & f[z_1, z_2] = \frac{f[z_2] - f[z_1]}{z_2 - z_1} & f[z_1, z_2, z_3] = \frac{f[z_2, z_3] - f[z_1, z_2]}{z_3 - z_1} \\
    \hline
    z_2 = x_1 & f[z_2] = f(x_1) & f[z_2, z_3] = f'(x_1) & f[z_2, z_3, z_4] = \frac{f[z_3, z_4] - f[z_2, z_3]}{z_4 - z_2} \\
    \hline
    z_3 = x_1 & f[z_3] = f(x_1) & f[z_3, z_4] = \frac{f[z_4] - f[z_3]}{z_4 - z_3} & f[z_3, z_4, z_5] = \frac{f[z_4, z_5] - f[z_3, z_4]}{z_5 - z_3} \\
    \hline
    z_4 = x_2 & f[z_4] = f(x_2) & f[z_4, z_5] = f'(x_2) & \\
    \hline
    z_5 = x_2 & f[z_5] = f(x_2) & & \\
    \hline
    \end{array}
    """)

    # Sección 6.2
    st.markdown("## 6.2 Ajuste de curvas. Splines")
    
    st.markdown("**Definición:** Los splines son funciones polinómicas por tramos que se utilizan para interpolar datos. Un spline de grado $k$ es una función $S(x)$ definida en $[a,b]$ que coincide con un polinomio de grado $\\leq k$ en cada subintervalo $[x_i, x_{i+1}]$ y tiene derivadas continuas hasta el orden $k-1$ en los nodos.")
    
    st.markdown("**Fórmula (Spline Cúbico):**")
    st.markdown("Para cada intervalo $[x_i, x_{i+1}]$, el spline cúbico tiene la forma:")
    st.latex(r"S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3")
    st.markdown("donde los coeficientes se determinan mediante las condiciones:")
    st.markdown("""
    - $S_i(x_i) = f(x_i)$ y $S_i(x_{i+1}) = f(x_{i+1})$
    - $S'_i(x_{i+1}) = S'_{i+1}(x_{i+1})$
    - $S''_i(x_{i+1}) = S''_{i+1}(x_{i+1})$
    """)

    # Sección 7.2
    st.markdown("## 7.2 Regresión lineal y Aproximación funcional")
    
    st.markdown("**Definición:** La regresión lineal es un método estadístico que modela la relación entre una variable dependiente y una o más variables independientes mediante una ecuación lineal. Minimiza la suma de los cuadrados de las diferencias entre los valores observados y los predichos.")
    
    st.markdown("**Fórmula (Regresión Lineal Simple):**")
    st.latex(r"y = \beta_0 + \beta_1 x + \varepsilon")
    st.markdown("donde los coeficientes se calculan como:")
    st.latex(r"\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad \beta_0 = \bar{y} - \beta_1 \bar{x}")

    # Sección 8.3
    st.markdown("## 8.3 Newton–Cotes Regla del trapecio")
    
    st.markdown("**Definición:** La regla del trapecio es un método de integración numérica que aproxima la integral de una función mediante el área de trapecios. Es una fórmula de Newton-Cotes de primer orden.")
    
    st.markdown("**Fórmula:**")
    st.latex(r"\int_a^b f(x) dx \approx \frac{b-a}{2} [f(a) + f(b)]")
    st.markdown("Para $n$ subintervalos:")
    st.latex(r"\int_a^b f(x) dx \approx \frac{h}{2} [f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)]")
    st.markdown("donde $h = \\frac{b-a}{n}$.")

    # Sección 9.3
    st.markdown("## 9.3 Regla de Simpson 1/3")
    
    st.markdown("**Definición:** La regla de Simpson 1/3 es un método de integración numérica que aproxima la integral usando parábolas. Es una fórmula de Newton-Cotes de segundo orden.")
    
    st.markdown("**Fórmula:**")
    st.latex(r"\int_a^b f(x) dx \approx \frac{h}{3} [f(x_0) + 4f(x_1) + f(x_2)]")
    st.markdown("Para $n$ subintervalos (con $n$ par):")
    st.latex(r"\int_a^b f(x) dx \approx \frac{h}{3} [f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)]")

    # Sección 10.3
    st.markdown("## 10.3 Regla de Simpson 3/8")
    
    st.markdown("**Definición:** La regla de Simpson 3/8 es un método de integración numérica que aproxima la integral usando polinomios cúbicos. Es una fórmula de Newton-Cotes de tercer orden.")
    
    st.markdown("**Fórmula:**")
    st.latex(r"\int_a^b f(x) dx \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]")
    st.markdown("Para $n$ subintervalos (con $n$ múltiplo de 3):")
    st.latex(r"\int_a^b f(x) dx \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + 3f(x_4) + \cdots + f(x_n)]")

    # Sección 11.3
    st.markdown("## 11.3 Integración de Romberg")
    
    st.markdown("**Definición:** La integración de Romberg es un método que combina la regla del trapecio con la extrapolación de Richardson para obtener aproximaciones más precisas de integrales definidas.")
    
    st.markdown("**Fórmula:**")
    st.latex(r"R_{k,1} = \frac{1}{2} \left[ R_{k-1,1} + h_{k-1} \sum_{i=1}^{2^{k-2}} f(a + (2i-1)h_k) \right]")
    st.latex(r"R_{k,m} = R_{k,m-1} + \frac{R_{k,m-1} - R_{k-1,m-1}}{4^{m-1} - 1}")
    st.markdown("donde $h_k = \\frac{b-a}{2^{k-1}}$ y $R_{1,1} = \\frac{b-a}{2}[f(a) + f(b)]$.")

    # Sección 12.1
    st.markdown("## 12.1 Punto fijo para sistemas NO lineales")
    
    st.markdown("**Definición:** El método del punto fijo para sistemas no lineales busca encontrar la solución de un sistema de ecuaciones $F(x) = 0$ transformándolo en un problema de punto fijo $x = G(x)$, donde $G$ es una función de iteración.")
    
    st.markdown("**Fórmula:**")
    st.markdown("Dado el sistema $F(x) = 0$, se reescribe como:")
    st.latex(r"x = G(x)")
    st.markdown("y se itera mediante:")
    st.latex(r"x^{(k+1)} = G(x^{(k)})")
    st.markdown("La convergencia está garantizada si $\\|G'(x)\\| < 1$ en una región que contiene la solución.")

    # Sección 13.1
    st.markdown("## 13.1 Método de Newton")
    
    st.markdown("**Definición:** El método de Newton es un algoritmo iterativo para encontrar raíces de funciones no lineales. Utiliza la linealización de la función mediante su derivada para aproximarse a la raíz.")
    
    st.markdown("**Fórmula:**")
    st.markdown("Para una función $f(x)$:")
    st.latex(r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}")
    st.markdown("Para sistemas de ecuaciones $F(x) = 0$:")
    st.latex(r"x^{(k+1)} = x^{(k)} - J_F(x^{(k)})^{-1} F(x^{(k)})")
    st.markdown("donde $J_F$ es la matriz jacobiana de $F$.")

    # Sección 14.1
    st.markdown("## 14.1 Método de quasi Newton")
    
    st.markdown("**Definición:** Los métodos quasi-Newton son variantes del método de Newton que evitan el cálculo directo de la matriz jacobiana o hessiana, aproximándola mediante actualizaciones sucesivas.")
    
    st.markdown("**Fórmula (BFGS - Broyden-Fletcher-Goldfarb-Shanno):**")
    st.latex(r"x_{k+1} = x_k - \alpha_k B_k^{-1} \nabla f(x_k)")
    st.latex(r"B_{k+1} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}")
    st.markdown("donde $s_k = x_{k+1} - x_k$, $y_k = \\nabla f(x_{k+1}) - \\nabla f(x_k)$, y $B_k$ aproxima la hessiana.")

if __name__ == "__main__":
    app()
