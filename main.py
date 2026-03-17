from typing import List, Dict, Optional, Union
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world() -> Dict[str, str]:
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: Optional[str] = Query(None)) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    url: str = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response: requests.Response = requests.get(url)

    if response.status_code == 200:
        dados_json: List[Dict[str, str]] = response.json()

        # Se não filtrar por restaurante, retorna todos
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante: List[Dict[str, str]] = []

        for item in dados_json:
            company: str = item.get('Company', '').lower()
            if company == restaurante.lower():
                dados_restaurante.append({
                    "item": str(item.get('Item', '')),
                    "price": str(item.get('Price', '')),
                    "description": str(item.get('Description', ''))
                })

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    else:
        # Retorno de erro precisa ser consistente com Dict[str, str]
        return {'Erro': f'{response.status_code} - {response.text}'}