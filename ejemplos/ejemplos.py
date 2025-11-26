import streamlit as st
from ejemplos.ejemplos import app as ejemplos_app

# ... resto del código ...

# En la parte donde manejas la navegación:
if selection == "Ejercicios y ejemplos":
    ejemplos_app()