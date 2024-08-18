print('===== LOJA DO KAIQUE =====')

preco = float(input('Diga qual foi o preço das compras: '))
print('Formas de pagamento '
      '[1] à vista dinheiro/cheque '
      '[2] à vista cartão '
      '[3] 2x no cartão '
      '[4] 3x ou mais no cartão')
opcao = int(input('Qual das seguintes opções você escolhe? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra teve um desconto à vista, então sua conta ficou R$ {total:.2f}')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R$ {preco:.2f} teve um desconto à vista de 5%, então sua conta ficou R$ {total:.2f}')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'A parcela em 2 vezes ficará R$ {parcela:.2f} em cada mês')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final, com parcelas de R$ {parcela:.2f}')
else:
    print('Opção inválida de pagamento!')

print(f'O total a pagar é R$ {total:.2f}')
