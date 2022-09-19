from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
      input('Qual o valor da largura do cômodo:'),
      input('Qual o valor da profundidade do comodo:')
)

print("A area das paredes é: " ,
      calc.calcular_area_paredes(
            comodo
      )
)

print('A area do teto é:',
      calc.calcular_area_teto(
            comodo
      )
)

print('A litragem de de tinta necessária é: ',
      calc.calcular_litragem_necessario()
)
