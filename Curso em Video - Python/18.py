import math

angulo = int(input('Digite aqui o valor de um ângulo: '))
seno = "{:.2f}".format(math.sin(math.radians(angulo)))
cosseno = "{:.2f}".format(math.cos(math.radians(angulo)))
tangente = "{:.2f}".format(math.tan(math.radians(angulo)))
print(f'O seno de {str(angulo) + "º"} vale {str(seno) + "º"} \n'
      f'O cosseno de {str(angulo) + "º"} vale {str(cosseno) + "º"} \n'
      f'A tangente de {str(angulo) + "º"} vale {str(tangente) + "º"}')