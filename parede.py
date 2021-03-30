altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
area = altura * largura
tinta = area / 2
print(f" Você precisará de {tinta:.2f}l de tinta para pintar a parede que mede {area:.2f}m² ")
