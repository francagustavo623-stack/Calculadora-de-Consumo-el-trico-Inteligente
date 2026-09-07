import time #tbm pd ser usada pra ver o horario com a funcao "localtime()"
import getpass #coleta informacoes sensiveis do usuario, como o NOME dele
import os

a = time.localtime()
agora = a[3]
agoraa = int(agora)
momentitos = []
nome = getpass.getuser()


#sei q nao foi pedido, mas qria polir um pouco:3
if agoraa >= 21:
    momentitos.append(f"Boa noite, {nome.capitalize()}!")
elif agoraa >= 12 and agoraa < 21:
    momentitos.append(f"Boa tarde, {nome.capitalize()}!!")
else: 
    momentitos.append(f"Bom dia, {nome.capitalize()}!!!")
#as condicionais acima, basicamente, checa o momento exato em q o usuario esta e muda sua abordagem:3

print(*momentitos)# o "*" faz com q soh o necessario seja exibido.
print('Este programa vai te ajudar a calcular seu gasto diario com eletronicos')

Eletronico = input(f'{nome.capitalize()}, qual o seu eletronico? R: ')
os.system('cls')
potencia = int(input(f'Esse "{Eletronico.capitalize()}" possui quantos Watts? R: '))
os.system('cls')
horasDia = int(input(f'{nome.capitalize()}, voce utiliza esse "{Eletronico.capitalize()}" por quantas horas diariamente? R: '))

if horasDia > 24:
    os.system('cls')
    print('OPA, calmaee:3 Vamos deixar como 24 horas de gasto, ok?:3')
    consumoMensal = (potencia * 24 * 30) / 1000
else:
    consumoMensal = (potencia * horasDia * 30) / 1000

os.system('cls')
print(f'{nome.capitalize()}, esse seu aparelho (que se chama "{Eletronico.capitalize()}"), gasta aproximadamente: {consumoMensal} kWh no mes!')