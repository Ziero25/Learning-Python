import datetime
anoNascimento = int(input("Digite o ano em que você nasceu: "))
anoAtual = datetime.date.today().year - anoNascimento
print(f"Você tem {anoAtual} de idade.")
