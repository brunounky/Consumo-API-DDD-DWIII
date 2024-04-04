import requests
import json

def main():
    URL = "https://brasilapi.com.br/api/ddd/v1/15"
    req = requests.get(URL)
    dados_recebidos = req.json()

    print(json.loads(req.content))

if __name__ == "__main__":
    main()