from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input('Qual o valor da largura do cômodo:'))
profundidade: float = float(input('Qual o valor da profundidade do comodo:'))
altura: float = 2.9

calc.area_paredes: float = (2*(largura+profundidade)*altura)
print("A area das paredes é: " , calc.area_paredes)

calc.area_teto: float = largura * profundidade
print('A area do teto é:', calc.area_teto)

print('A litragem de de tinta necessária é: ',
      (calc.area_paredes + calc.area_teto)/10
)
