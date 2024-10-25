
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from bs4 import BeautifulSoup

@csrf_exempt  # Deshabilita la verificación de CSRF para esta vista (útil en pruebas con Postman)
def prueba(request):
    print(request.GET)
    if request.method == 'GET':
        data = {'message': 'Hello, this is a GET request!'}
        texto = text_extract(request.GET)
        print(texto)
        return JsonResponse(texto)
    """elif request.method == 'POST':
        data = {'message': 'Hello, this is a POST request!', 'received_data': request.POST}
        return JsonResponse(data)"""


def text_extract(path):
    url = path.get("url")
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto = soup.get_text()

        
        return {"texto": texto}
    else:
        print(f'Error al acceder a la página: {response.status_code}')