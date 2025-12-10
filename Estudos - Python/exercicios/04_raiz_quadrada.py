numero = input("Entre com um número inteiro para calcular a sua raiz quadrada: ")
numero = int(numero)

raiz = numero ** 0.5
raiz = round(raiz, 4)

print("Raiz quadrada de", numero, "é", raiz)