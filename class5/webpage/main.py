import streamlit as st

st.sidebar. title("Calculadora ICI")

def pedir_valores():
    name= st.text_input("Nombre")
    n1= st.number_input("Numero 1")
    n2= st.number_input("Numero 2")
    
    if st.button("Suma"):
        st.success(f"Hola: {name}")
        st.write(f"{n1} + {n2} = {n1+n2}")
        
    if st.button("Resta"):
        st.success(f"Hola: {name}")
        st.write(f"{n1} + {n2} = {n1-n2}")
        
    if st.button("Multiplicacion"):
        st.success(f"Hola {name}")
        st.write(f"{n1} * {n2} = {n1 * n2}")
        
    if st.button("Division"):
        st.success(f"Hola: {name}")
        st.write(f"{n1} / {n2} = {n1 / n2}")
        

opcion = st.sidebar.selectbox("Opciones", ["Suma", "Resta", "multiplicacion", "Division", "Acerca de"])

match opcion:
    case "Suma":
        st.write("Esta es la opcion de suma...")
        pedir_valores()
    case "Resta":
        st.write("Esta es la opcion de resta...")
        pedir_valores()
    case "Multiplicacion":
        st.write("Esta es la opcion de multiplicacion...")
    case "Division":
        st.write("Esta es la opcion de division...")
        pedir_valores()
    case "Acerca de":
        st.write("Nuestro programa es un ejemplo")
        pedir_valores()
        
