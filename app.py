import requests
import json
from typing import List, Dict, Any

url: str = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response: requests.Response = requests.get(url)
print(response)

dados_restaurante: Dict[str, List[Dict[str, Any]]] = {}  # inicializa vazio

if response.status_code == 200:
    dados_json: List[Dict[str, Any]] = response.json()
    
    for item in dados_json:
        nome_do_restaurante: str = item.get('Company', 'Desconhecido')
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            "item": item.get('Item', ''),
            "price": item.get('price', 0),
            "description": item.get('description', '')
        })
    
    # Só escreve os arquivos se a requisição deu certo
    for nome_do_restaurante, dados in dados_restaurante.items():
        nome_do_arquivo: str = f'{nome_do_restaurante}.json'
        with open(nome_do_arquivo, 'w') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4)
else:
    print(f'O erro foi {response.status_code}')