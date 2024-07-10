import streamlit as st
from PIL import Image
from functions import load_model, predict_image, partes_del_cuerpo
import openai
from modulo import get_x, get_y 


# Configurar la clave de API de OpenAI
openai.api_key = ''

# Título de la aplicación
st.title('Clasificador de radiografías')

# Función para cargar imagen desde el archivo
def cargar_imagen(archivo):
    img = Image.open(archivo)
    return img

# Función para mostrar la predicción y probabilidades
def mostrar_prediccion(img, learner):
    pred, probs = predict_image(img, learner)
    pred = int(pred)  # Convertir la predicción a entero
    parte_del_cuerpo = partes_del_cuerpo.get(pred, "Parte del cuerpo desconocida")
    return parte_del_cuerpo, probs

# Función para obtener la descripción de una parte del cuerpo en el contexto médico
def obtener_descripcion(parte_del_cuerpo):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                 {"role": "user", "content": f"Eres un médico traumatólogo experto. Imagina que estas observando una radiografía de {parte_del_cuerpo}. Inventa una descripcion de la imagen en tono de informe medico. Se creativo y profesional. Comienza el texto solo con 'informe radiológico' y luego el resto. No reveles informacion personal de los pacientes."}
            ],
            max_tokens=1500
        )
        return response.choices[0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error al obtener la descripción: {e}")
        return None

# Configurar la interfaz de la aplicación
st.sidebar.title('Ajustes')
st.sidebar.markdown('Sube una imagen de radiografía para analizar.')

# Cargar el modelo y mostrar un mensaje apropiado
model_path = 'best_model_densenet.pkl'
learner = load_model(model_path)
if learner is not None:
    st.sidebar.success("Modelo cargado exitosamente!")
else:
    st.sidebar.error("Fallo al cargar el modelo. Verifica la ruta y los permisos del archivo.")

# Carga de imagen y análisis
uploaded_file = st.sidebar.file_uploader("Sube una imagen de radiografía", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Cargar la imagen
    image = cargar_imagen(uploaded_file)
    
    # Mostrar la imagen en la mitad izquierda
    st.image(image, caption='Imagen subida', use_column_width=True)

    # Botón para analizar
    if st.sidebar.button('Analizar'):
        # Realizar predicción
        resultado, probabilidades = mostrar_prediccion(image, learner)
        if isinstance(resultado, str) and resultado == "Parte del cuerpo desconocida":
            st.sidebar.error("Fallo de predicción")
        else:
            st.sidebar.success(f"La imagen corresponde a: {resultado}")
            st.sidebar.write(f"Parámetros Observados: {probabilidades}")
            descripcion = obtener_descripcion(resultado)
            if descripcion:
                st.write(f"Información sobre {resultado}:")
                st.write(descripcion)
