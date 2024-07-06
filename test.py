from fastai.vision.all import load_learner, PILImage
import pathlib
from modulo import get_x, get_y  # Asegúrate de importar correctamente estas funciones


id = {
    0: 'Abdomen',
    1: 'Tobillo',
    2: 'Columna cervical',
    3: 'Tórax',
    4: 'Clavículas',
    5: 'Codo',
    6: 'Pies',
    7: 'Dedos',
    8: 'Antebrazo',
    9: 'Mano',
    10: 'Cadera',
    11: 'Rodilla',
    12: 'Pierna',
    13: 'Columna lumbar',
    14: 'Otros',
    15: 'Pelvis',
    16: 'Hombro',
    17: 'Senos paranasales',
    18: 'Cráneo',
    19: 'Muslo',
    20: 'Columna torácica',
    21: 'Muñeca'
}


def load_model(model_path):
    # Configuración de pathlib para evitar problemas con PosixPath en Windows
    original_pathlib_path = pathlib.Path
    pathlib.PosixPath = pathlib.WindowsPath

    try:
        # Importar las funciones dentro de la función no es necesario si ya están en el espacio de nombres
        learner = load_learner(model_path)
        print("Modelo cargado exitosamente!")
        return learner

    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

    finally:
        # Restaurar pathlib.Path
        pathlib.Path = original_pathlib_path


def predict_image(img, learner):
    # Verificar si 'img' es una ruta de archivo y cargarla
    if isinstance(img, str):
        img = PILImage.create(img)
    
    # Asegurarse de que la imagen esté en el formato adecuado
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Aplicar el mismo preprocesamiento que se hizo durante el entrenamiento, como redimensionar
    # Asegúrate de que las dimensiones son las que el modelo espera, e.g., 224x224 para modelos como ResNet
    img = img.resize((224, 224))
    
    # Realizar la predicción
    pred, _, probs = learner.predict(img)

    # Devolver la clase predicha y las probabilidades
    return pred, probs

