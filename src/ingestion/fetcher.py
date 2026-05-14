from dotenv import load_dotenv

import requests
import json
import os

load_dotenv()


def buscar_personagens(limite=100, offset=0):
    API_COMICVINE = os.getenv("COMICVINE_API_KEY")

    if API_COMICVINE is None:
        print("Chave API Comicvine não encontrada")
        return

    lista_personagens = []

    print("Buscando personagens...")

    while True:
        URL_PERSONAGENS = (
            f"https://comicvine.gamespot.com/api/characters/"
            f"?api_key={API_COMICVINE}&format=json&limit={limite}&offset={offset}"
        )

        resposta = requests.get(URL_PERSONAGENS, headers={"User-Agent": "marvel-rag"}).json()

        for character in resposta["results"]:
            personagem = {
                "Nome": "",
                "Nome_Real": "",
                "Resumo": "",
                "Descricao": "",
                "Apelidos": "",
                "Primeira_Aparicao": "",
                "Qtd_Aparicoes": "",
                "Origem": "",
                "Icone_URL": "",
                "Img_URL": "",
            }

            try:
                if character["publisher"]["id"] == 31:
                    personagem["Nome"] = character["name"]
                    personagem["Nome_Real"] = character["real_name"]
                    personagem["Resumo"] = character["deck"]
                    personagem["Descricao"] = character["description"]
                    personagem["Apelidos"] = character["aliases"]
                    personagem["Primeira_Aparicao"] = character["first_appeared_in_issue"]
                    personagem["Qtd_Aparicoes"] = character["count_of_issue_appearances"]
                    personagem["Origem"] = character["origin"]
                    personagem["Icone_URL"] = character["image"]["icon_url"]
                    personagem["Img_URL"] = character["image"]["small_url"]

                    lista_personagens.append(personagem)
                    print(f"Personagem {personagem['Nome']} adicionado à lista")

            except (KeyError, TypeError):
                continue

        if (len(lista_personagens) == 1000):
            return lista_personagens

            
        if resposta["number_of_page_results"] == 0:
            break

        offset += 100

    return lista_personagens


if __name__ == "__main__":
    buscar_personagens()
