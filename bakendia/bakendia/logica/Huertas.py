from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("xx_LeetSpeakNER_mstsb_mpnet")

texts =["Si tratta _s+o%l\"o di una questione men'ta?le."]

@csrf_exempt  # Deshabilita la verificación de CSRF para esta vista (útil en pruebas con Postman)
def setText(request):
    devolucion={}
    devolucion["elementos"] = []
    if request.method == 'GET':
        data = {'message': 'Hello, this is a GET request!'}
        texto = request.GET.get("texto")    
        texts[0] = texto
        print(texts[0])
    
        # Procesar los textos con el modelo NER
        for doc in nlp.pipe(texts):
            print(f"Texto procesado: {doc.text}")
            print("Entidades detectadas:")
            for ent in doc.ents:
                print(f"Entidad: {ent.text}, Etiqueta: {ent.label_}")
                print(ent)
                devolucion["elementos"].append({"palabra":ent.text, "ofuscacion": ent.label_})
            print("-" * 40)
    print(devolucion)
    return JsonResponse(devolucion)