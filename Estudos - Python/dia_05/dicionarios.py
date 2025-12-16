# %%

lista = [2, 132, "edu", True, ["ds", "de", "da"], True]
lista[2]
# %%

dados_edu = {
            "nome":"Edu",
            "filhos":False,
            "idade":18,
            "formacao":["Ciencia de Dados", "Técnico em Informática"],
            "cargos":[
              {"nome": "ds jr.", "empresa":"empresa x"},
              {"nome": "ds pl.", "empresa":"empresa y"},
              {"nome": "ds sr.", "empresa":"empresa z"},
              {"nome": "ds espec.", "empresa":"empresa w"},
            ]
          }

# %%
print(dados_edu)
print(dados_edu["formacao"][-1])
print(dados_edu["cargos"][-1]["empresa"])
# %%

dados_edu["estado civil"] = "solteiro"

# %%

print("Chaves:", dados_edu.keys())
print("Valores:", dados_edu.values())
print("Itens:", dados_edu.items())
# %%

for i in [10,20,30,13,312,"edu"]:
  print(i)

# %%

for i in dados_edu:
  print(i, "->", dados_edu[i])

# %%

for chave, valor in dados_edu.items():
  print(chave, "->", valor)

for i, j in dados_edu.items():
  print(i, "->", j)
# %%


