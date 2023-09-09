'''Imagine que você está criando um aplicativo de entrega de comida e precisa informar ao usuário o tempo estimado de entrega de um restaurante. 
A mensagem deve conter o nome do restaurante e o tempo estimado de entrega em minutos.
'''

nomeRestaurante = input()
tempoEstimadoEntrega = int(input())

#TODO: Imprimir a saída no padrão definido no enunciado deste desafio.
#Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.

print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")