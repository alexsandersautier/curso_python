from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input('Qual o valor da largura do cômodo:'))
profundidade: float = float(input('Qual o valor da profundidade do comodo:'))
altura: float = 2.9

print("A area das paredes é: " ,
      calc.calcular_area_paredes(largura,profundidade,altura)
)

print('A area do teto é:',
      calc.calcular_area_teto(largura,profundidade)
)

print('A litragem de de tinta necessária é: ',
      calc.calcular_litragem_necessario()
)
