"""
Iterável -> str, range, etc (__inter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entrgue seu iterador
"""
# for letra in texto
texto = 'Luiz' # iterável
iteratador = iter(texto) # ietrador

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# for letra in texto:
#     print(letra)
