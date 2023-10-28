fimport streamlit as st
import pandas as pd

class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno, tipo, correo):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo = tipo
        self.correo = correo

class Directorio:
    def __init__(self):
        self.personas = []
        self.id_counter = {'profesor': 0, 'alumno': 0}

    def cargar_personas(self):
        # Aquí puedes cargar datos previamente almacenados en la lista de personas.
        # Por ejemplo, puedes leerlos desde un archivo CSV o una base de datos.
        # En este ejemplo, cargamos datos ficticios para demostración.
        self.personas.append(Persona("Juan", "Pérez", "Gómez", "profesor", "juan@example.com"))
        self.personas.append(Persona("Ana", "López", "Rodríguez", "alumno", "ana@example.com"))

    def guardar_personas(self):
        # Puedes agregar código aquí para guardar las personas en una base de datos o archivo si es necesario.
        pass

    def crear_persona(self, nombre, apellido_paterno, apellido_materno, tipo, correo):
        if tipo.lower() not in ['profesor', 'alumno']:
            st.error("Tipo de persona no válido. Use 'profesor' o 'alumno'.")
            return
        self.id_counter[tipo.lower()] += 1
        persona = Persona(nombre, apellido_paterno, apellido_materno, tipo, correo)
        self.personas.append(persona)
        self.guardar_personas()
        st.success(f"{tipo.capitalize()} creado con éxito. ID: {tipo[0].lower()}{self.id_counter[tipo.lower()]:02d}")

    def leer_persona(self, persona_id):
        for persona in self.personas:
            if persona.tipo.lower() + str(self.personas.index(persona) + 1).zfill(2) == persona_id:
                return persona
        return None

    def actualizar_persona(self, persona_id, nombre, apellido_paterno, apellido_materno, correo):
        persona = self.leer_persona(persona_id)
        if persona:
            persona.nombre = nombre
            persona.apellido_paterno = apellido_paterno
            persona.apellido_materno = apellido_materno
            persona.correo = correo
            self.guardar_personas()
            st.success(f"Datos de {persona.tipo} actualizados con éxito.")
        else:
            st.error("ID de persona no encontrado.")

    def eliminar_persona(self, persona_id):
        persona = self.leer_persona(persona_id)
        if persona:
            self.personas.remove(persona)
            self.guardar_personas()
            st.success(f"{persona.tipo.capitalize()} eliminado con éxito.")
        else:
            st.error("ID de persona no encontrado.")

def main():
    st.title("Directorio de Profesores y Alumnos")

    directorio = Directorio()
    directorio.cargar_personas()  # Cargar personas al iniciar la aplicación.

    st.sidebar.header("Menú")
    menu = st.sidebar.radio("Selecciona una opción:", ["Crear Persona", "Leer Persona", "Actualizar Persona", "Eliminar Persona"])

    if menu == "Crear Persona":
        st.header("Crear Persona")
        nombre = st.text_input("Nombre:")
        apellido_paterno = st.text_input("Apellido Paterno:")
        apellido_materno = st.text_input("Apellido Materno:")
        tipo = st.selectbox("Tipo de Persona:", ["Profesor", "Alumno"])
        correo = st.text_input("Correo Electrónico:")
        if st.button("Crear"):
            directorio.crear_persona(nombre, apellido_paterno, apellido_materno, tipo.lower(), correo)

    elif menu == "Leer Persona":
        st.header("Leer Persona")
        persona_id = st.text_input("ID de Persona:")
        if st.button("Leer"):
            persona = directorio.leer_persona(persona_id)
            if persona:
                st.success(f"Nombre: {persona.nombre}")
                st.success(f"Apellido Paterno: {persona.apellido_paterno}")
                st.success(f"Apellido Materno: {persona.apellido_materno}")
                st.success(f"Tipo: {persona.tipo.capitalize()}")
                st.success(f"Correo Electrónico: {persona.correo}")
            else:
                st.error("ID de persona no encontrado.")

    elif menu == "Actualizar Persona":
        st.header("Actualizar Persona")
        persona_id = st.text_input("ID de Persona:")
        nombre = st.text_input("Nombre:")
        apellido_paterno = st.text_input("Apellido Paterno:")
        apellido_materno = st.text_input("Apellido Materno:")
        correo = st.text_input("Correo Electrónico:")
        if st.button("Actualizar"):
            directorio.actualizar_persona(persona_id, nombre, apellido_paterno, apellido_materno, correo)

    elif menu == "Eliminar Persona":
        st.header("Eliminar Persona")
        persona_id = st.text_input("ID de Persona:")
        if st.button("Eliminar"):
            directorio.eliminar_persona(persona_id)

if __name__ == "__main__":
    main()
