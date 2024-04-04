import requests
import json

def main():

    print("Consulta de DDD para saber quais são as cidades que compoem o mesmo")
    print("DDD usual não precisa por o 0 inicial")

    ddd = input("Informe o DDD: ")

    URL = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    req = requests.get(URL)
    dados_recebidos = req.json()

    print(json.loads(req.text))

if __name__ == "__main__":
    main()