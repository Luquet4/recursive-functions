'''
Exercício 4: 

Encontrar o Índice do Maior Elemento
Escreva uma função recursiva chamada indice_maior_elemento(lista) que retorna o
índice do maior elemento em uma lista.

Exemplo de Entrada:
indice_maior_elemento([1, 5, 3, 9, 2])

Saída Esperada:
3 # O maior elemento é 9, que está no índice 3
'''

def indice_maior_elemento(lista):
    if len(lista) == 1:
        return 0  
    
    indice_resto = indice_maior_elemento(lista[1:])
    
    return 0 if lista[0] >= lista[1 + indice_resto] else 1 + indice_resto

print(indice_maior_elemento([1, 5, 3, 9, 2]))
