# %%

import requests
import json

# %%
ceps = [
  "01001000",
  "01310930",
  "20040002",
  "30140071",
  "40010000",
  "61901180",
  "69900000",
  "76820000",
  "88010000",
  "99010000",
  "19060100",
  "70040900",
]

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
for i in ceps:
  resposta = requests.get(url.format(cep=i))
  if resposta.status_code == 200:
    dados.append(resposta.json())
dados

# %%

print(dados)
with open("ceps.json", "w") as open_file:
  json.dump(dados, open_file, ensure_ascii=False, indent=4)
# %%
