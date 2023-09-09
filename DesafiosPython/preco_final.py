'''
    Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.

'''

valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

total_hamburguer = valorHamburguer * quantidadeHamburguer
total_bebidas = valorBebida * quantidadeBebida
total = total_bebidas + total_hamburguer

troco = valorPago - total

print("O preço final do pedido é R$ %.2f. Seu troco é R$ %.2f." % (total,troco))