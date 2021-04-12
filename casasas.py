print("Calculadora de Empréstimo Bancário ")
valor_casa = int(input("Valor da casa:"))
print ("-=-" *20 )
salario = int(input("Qual seu Salário:"))
print ("-=-" *20 )
anos = int(input("Anos à pagar:"))
meses = anos * 12
parcelas = valor_casa / meses
minimo = (salario / 100) * 30

print("-=-" *20 )
print(f"O valor da casa dividido em, {meses:.2f} meses é de: {parcelas:.2f},por mês.")
print("-=-" *20 )

if parcelas < minimo:
    print('seu empréstimo foi aprovado.')
else:
    print('seu empréstimo não foi aprovado,pois o valor das parcelas é maior que 30% do seu salário que é de',minimo)