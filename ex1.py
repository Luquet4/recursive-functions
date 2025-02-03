'''
    - Exercicio 1
        Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
        string e devolve a string invertida. Não use laços (for ou while).
'''

def revert_string(x):
    if len(x) == 0:
        return ""
    else:
        return x[-1] + revert_string(x[:-1])

result = revert_string("Python")
print(result)
