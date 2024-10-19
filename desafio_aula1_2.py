rendaMensal = float(input('Digite sua renda mensal: '))

despesasMes1 = float(input('Digite o total de despesas de 3 meses atrás: '))
despesasMes2 = float(input('Digite o total de despesas de 2 meses atrás: '))
despesasMes3 = float(input('Digite o total de despesas do mês passado: '))

mediaDespesas3Meses = ((despesasMes1 + despesasMes2 + despesasMes3) / 3)
saldoAnual = (rendaMensal - mediaDespesas3Meses) * 12

print(f'Saldo anual final: {saldoAnual:.2f} e valor médio de despesas: {mediaDespesas3Meses:.2f}')