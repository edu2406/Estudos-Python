# %%

idades = [18, 22, 15, 45, 33, 19, 20]

print(idades)
# %%

edu = ["Eduardo", 18, 1.83, False, "Solteiro"]
print(edu)

# %%
type(edu)

# %%
print(edu[2])
print(edu[4])
print(edu[0])
# %%

idades = [18, 22, 15, 45, 33, 19, 20, 33, 12, 25]
print("Soma idades:", sum(idades))

print("Quantidade idades:", len(idades))

print("Media idades:", sum(idades) / len(idades))

print("Menor idade:", min(idades))

print("Maior idade:", max(idades))
# %%

edu = ["Eduardo",
      18,
      False, 
      "Solteiro",
      ["estudante", "estagiario", "dev jr.", "dev pl.", "dev sr."],
      ["0", "1000", "3000", "6500", "12000"],
      ["Roblox", "Valorant", "Hollow Knight"]]

print("Tamanho de edu:", len(edu))

print(edu[6][0])

jogos = edu[6]
primeiro_jogo = jogos[0]
print(primeiro_jogo)

# %%

tamanho = len(edu)
pos = tamanho - 1
jogos = edu[pos]

edu[pos][len(jogos) - 1]
# %%

edu[-1][-2]
# %%

edu[0:4]
edu[4][3:5]
# %%
edu[4][-2:]
# %%
# edu[ start : stop ]
edu[:4]
# %%
# edu[ start : stop : step ]
salarios = edu[5]
salarios[::-1]
salarios[::2]
# %%
