from dotenv import load_dotenv

import requests
import json
import os

load_dotenv()

def buscar_personagens(limite = 10):
    API_COMICVINE = os.getenv("COMICVINE_API_KEY")

    if (API_COMICVINE is None):
        print("Chave API Comicvine não encontrada")
        return
    else:
        print("Buscando personagens...")
        URL_PERSONAGENS = f"https://comicvine.gamespot.com/api/characters/?api_key={API_COMICVINE}&format=json&limit={limite}"

        resposta = requests.get(URL_PERSONAGENS, headers={"User-Agent": "marvel-rag"})
        resposta = resposta.json()

        return
    

if __name__ == "__main__":
    buscar_personagens()
    

