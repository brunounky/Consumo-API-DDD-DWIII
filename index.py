import requests
import json

URL = "https://receitaws.com.br/v1"
req = requests.get("https://receitaws.com.br/v1/cnpj/{08327285000181}")
dados_recebidos = req.json()


