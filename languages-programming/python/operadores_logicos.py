### Operadores Logicos

## AND

'''
### codigo original
idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura) >= 1.70
msg = 'Pode participar do evento? ' + str(resultado)

print(msg)
'''

IDADE = 18
ALTURA = 1.70

def verificar_condicao(idade, IDADE, altura, ALTURA):
    resultado = (str(idade) >= str(IDADE)) and (str(altura) >= str(ALTURA))
    return resultado

idade = input('Qual a sua idade ?')
altura = input('Qual a sua altura ?')

resultado = verificar_condicao(idade, IDADE, altura, ALTURA)

if resultado == True:
  print('Participante permitido a participar do evento, porque constou ' + str(resultado) + ' no resultado')
elif resultado == False:
  print('Participante não permitido a participar do evento, porque constou ' + str(resultado) + ' no resultado')



## OR

## NOT
