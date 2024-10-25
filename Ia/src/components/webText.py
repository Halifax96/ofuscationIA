import requests
from bs4 import BeautifulSoup

url = 'https://cabify.com/es'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    texto = soup.get_text()

    print(texto)
else:
    print(f'Error al acceder a la página: {response.status_code}')
