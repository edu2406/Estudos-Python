# %%
def par_impar(numero:int):
  if numero % 2 == 0:
    print("É par!")
  else:
    print("É ímpar!")


numero = input("Entre com um número: ")
numero = int(numero)

par_impar(numero)


# %%

def par_impar(numero:int):
  if numero % 2 == 0:
    return "par"
  else:
    return "ímpar"


numero = input("Entre com um número: ")
numero = int(numero)

resultado = par_impar(numero)

print("O valor", numero, "é", resultado)
# %%
