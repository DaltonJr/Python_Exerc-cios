import math

angulo = int(input('digite o grau:'))

rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('o seno de {}º é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo,sen,cos,tan))