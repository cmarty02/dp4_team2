import streamlit as st
from PIL import Image
from functions import load_model, predict_image, partes_del_cuerpo 
from modulo import get_x, get_y 

st.title('Clasificador de radiografías')

# Cargar el modelo y mostrar un mensaje apropiado
model_path = 'best_model_densenet.pkl'
learner = load_model(model_path)
if learner is not None:
    st.success("Modelo cargado exitosamente!")
else:
    st.error("Fallo al cargar el modelo. Verifica la ruta y los permisos del archivo.")

def cargar_imagen(archivo):
    img = Image.open(archivo)
    return img

def mostrar_prediccion(img):
    if learner is not None:
        pred, probs = predict_image(img, learner)
        pred = int(pred)  # Convertir la predicción a entero
        parte_del_cuerpo = partes_del_cuerpo.get(pred, "Parte del cuerpo desconocida")
        return parte_del_cuerpo, probs
    else:
        return "Fallo de predicción", {}


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
