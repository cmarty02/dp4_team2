import torch
from torchvision import transforms
from PIL import Image
import torch.nn as nn
from torchvision.models import densenet121
from fastai.vision.all import *
from pathlib import Path

def cargar_modelo(ruta_modelo):
    """ Carga un modelo entrenado usando FastAI. """
    # Crear un objeto dummy DataBlock para inicializar un Learner
    dls = ImageDataLoaders.from_folder(Path('.'), valid_pct=0.2, seed=42,
                                       item_tfms=Resize(224),
                                       batch_tfms=Normalize.from_stats(*imagenet_stats))
    learn = cnn_learner(dls, densenet121, metrics=accuracy)
    learn = learn.load(ruta_modelo, with_opt=False, device='cpu')
    learn.model.eval()
    return learn.model

def preprocesar_imagen(archivo_imagen):
    """ Preprocesa la imagen para hacerla compatible con las entradas del modelo. """
    transformacion = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    imagen = Image.open(archivo_imagen)
    imagen = imagen.convert('RGB')  # Asegurar que la imagen está en modo RGB
    imagen_tensor = transformacion(imagen)
    imagen_tensor = imagen_tensor.unsqueeze(0)  # Añadir una dimensión de batch
    return imagen_tensor

def predecir(learn, archivo_imagen):
    """ Realiza la predicción usando el modelo y la imagen proporcionada. """
    imagen = PILImage.create(archivo_imagen)
    pred,pred_idx,probs = learn.predict(imagen)
    return pred, probs[pred_idx].item()

