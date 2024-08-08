from math import sin, cos, tan, radians

angulog = float(input('Digite um ângulo em graus:'))
angulor = radians(angulog)
seno = sin(angulor)
cosseno = cos(angulor)
tangente = tan(angulor)

print('O seno, costumo e tangente de {}° é:' . format(angulog))
print('Seno: {:.2f} \nCostumo: {:.2f} \nTangente: {:.2f}' .format(seno, cosseno, tangente))
