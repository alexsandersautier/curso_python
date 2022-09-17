largura: float = float(input('Qual o valor da largura do cômodo:'))
profundidade: float = float(input('Qual o valor da profundidade do comodo:'))
altura: float = 2.9

print(largura)
print(profundidade)

print("A area das paredes é: " ,
      (2*(largura+profundidade)*altura))