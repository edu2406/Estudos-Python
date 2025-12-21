
import random


def get_input():
    while True:
        
        try:
            numero_usuario = int(input("Entre com um número: "))
        except ValueError as err:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
          return numero_usuario
        
        print("Valor inválido! O valor deve estar entre 1 e 15.")
        
def check_number(sorteio, usuario): 
    if sorteio == usuario:
        print("Parabéns! Você ganhou!")
        return True
    elif usuario > sorteio:
        print("Número muito alto. Tente um número menor!")
        return False
    else:
        print("Número muito baixo. Tente um número maior!")
        return False

numero_sorteio = random.randint(1, 15)

for i in range(3):
   
    numero_usuario = get_input()
    
    if check_number(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram. O número sorteado era:", numero_sorteio)

 

# tentativas = 3
# while tentativas >= 0:
#      if  tentativas == 0:
#          print("Suas tentativas acabaram. O número sorteado era:", numero_sorteio)
#          break
#      numero_usuario = int(input("Entre com um número: "))
#      if numero_sorteio == numero_usuario:
#          print("Parabéns! Você ganhou!")
#          break
#      elif numero_usuario > numero_sorteio:
#          print("Número muito alto. Tente um número menor!")
#      else:
#          print("Número muito baixo. Tente um número maior!")
#      tentativas -= 1