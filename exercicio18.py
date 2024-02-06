import math

ang= float(input('Digite o valor do ângulo: '))

ang_rad= math.radians(ang)

sen=math.sin (ang_rad)
cos=math.cos (ang_rad)
tan=math.tan (ang_rad)

print(f'O seno do ângulo {ang:.2f} graus é {sen:.2f}')
print(f'O cosseno do ângulo {ang:.2f} graus é {cos:.2f}')
print(f'A tangente do ângulo {ang:.2f} graus é {tan:.2f}')

#print(f'O valor do Seno do ângulo {ang:.2f} é {sen:.2f}\n O valor do Coseno do ângulo {ang} é {cos:.2f}\n O valor do Tangente do ângulo {ang} é {tan:.2f}')