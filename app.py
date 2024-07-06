import streamlit as st
from PIL import Image
from test import load_model, predict_image, id
from modulo import get_x, get_y 

st.title('Clasificador de radiografías')

# Cargar el modelo y mostrar un mensaje apropiado
model_path = 'best_model_densenet_epsilon.pkl'
learner = load_model(model_path)
if learner is not None:
    st.success("Modelo cargado exitosamente!")
else:
    st.error("Fallo al cargar el modelo. Verifica la ruta y los permisos del archivo.")


def cargar_imagen(archivo):
    img = Image.open(archivo)
    return img

def mostrar_prediccion(img):
    """Función para mostrar la predicción utilizando el modelo cargado."""
    if learner is not None:
        pred, probs = predict_image(img, learner)
        pred_desc = id.get(pred, "Clase desconocida")  # Uso del diccionario importado
        return pred_desc, probs
    else:
        return "Prediction Fail", {}

archivo_subido = st.file_uploader("Sube una imagen de radiografía", type=["png", "jpg", "jpeg"])

if archivo_subido is not None:
    imagen = cargar_imagen(archivo_subido)
    st.image(imagen, caption='Imagen subida', use_column_width=True)
    if st.button('Clasificar'):
        resultado, probabilidades = mostrar_prediccion(imagen)
        if isinstance(resultado, str):  # Chequear si resultado es un mensaje de error
            st.error(resultado)
        else:
            st.success(f"La imagen corresponde a: {resultado}")
            st.write(f"Probabilidades: {probabilidades}")
