import requests
import json

def main():

    ddd = input("Informe o DDD: ")

    URL = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    req = requests.get(URL)
    dados_recebidos = req.json()

    print(json.loads(req.text))

if __name__ == "__main__":
    main()