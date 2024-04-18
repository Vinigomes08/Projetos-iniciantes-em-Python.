"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio' # Iteráveis
#       1110987654321

nome = 'Maria Helena' # Iteráveis

contador = 0
nova_string = ''
while contador < len(nome):
    tamanho_nome = nome[contador]
    nova_string += f'*{tamanho_nome}'
    contador += 1
print('\nQuantas letras tem seu nome?:', contador)
print(nova_string)
