print("APS5")
print("Aprovação de crédito")


nome_cliente = input("\nDigite o nome do cliente: ")
renda_mensal = float(input("Digite a renda mensal: "))
valor_emprestimo = float(input("Digite o valor do emprestimo: "))
num_parcelas = int(input("Digite a quantidade de parcelas: "))
hist_credito = input("Situação de credito (B-Bom, R-Regular, P-Ruim): ")


# Cálculos
valor_parcela = valor_emprestimo / num_parcelas
perc_renda = valor_parcela * 100 / renda_mensal


# Processo
if hist_credito == "P":
    credito = "negado"

elif hist_credito == "R":
    if perc_renda <= 20:
        credito = "aprovado"
    elif perc_renda <= 35:
        credito = "restrito"
    else:
        credito = "negado"

elif hist_credito == "B":
    if perc_renda <= 30:
        credito = "aprovado"
    elif perc_renda <= 50:
        credito = "restrito"
    else:
        credito = "negado"

else:
    credito = "negado"

    

# Regra extra das parcelas
if credito == "aprovado" and num_parcelas > 60:
    credito = "aprovado restrito"
elif credito == "restrito" and num_parcelas > 60:
    credito = "negado"

print("Nome do cliente:", nome_cliente)
print("Valor emprestimo:", valor_emprestimo)
print("Valor parcela:", valor_parcela)
print("Percentual da renda:", perc_renda)
print("Situação final de credito:", credito)

input("\nPressione ENTER para sair...")
