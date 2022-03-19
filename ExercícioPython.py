#Detector de Palíndromo
Frase = str(input('Difite uma frase: ')).strip().upper()
proj = Frase.split()
junto = ''.join(proj)
inverso = ''
for p in range (len(junto) - 1,-1,-1):
    inverso += junto[p]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é um Palíndromo!')




