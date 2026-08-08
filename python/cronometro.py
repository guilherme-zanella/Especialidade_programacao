from time import sleep

def linha(tamanho=30):
    print('—' * tamanho)

def titulo(titulo):
    linha(40)
    print(titulo.center(40))
    linha(40)

def input_numero(text):
    while True:
        try:
            numero = int(input(text))
            return numero
        except:
            print(f'Erro. Digite um número inteiro válido')
    
titulo('Cronômetro')

inicio = input_numero('Digite o início: ')
final = input_numero('Digite o final: ')
passo = input_numero('Digite o passo: ')

if passo == 0:
    passo = 1

final+=1
    
if inicio > final:
    if passo > 0:
        passo = passo * -1
    final-=2

linha(40)
for numero in range(inicio, final, passo):
    print(numero)
    sleep(1)
print('Fim!')
linha(40)
