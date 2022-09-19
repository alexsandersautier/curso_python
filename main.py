largura: float = float(input('Qual o valor da largura do cômodo:'))
profundidade: float = float(input('Qual o valor da profundidade do comodo:'))
altura: float = 2.9

area_paredes: float = (2*(largura+profundidade)*altura)
print("A area das paredes é: " , str(area_paredes))

area_teto: float = largura * profundidade
print('A area do teto é:', area_teto)

print('A litragem de de tinta necessária é: ',
      (area_paredes + area_teto)/10
)
