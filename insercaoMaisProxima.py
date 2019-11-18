import numpy as np
import tsplib95 as tsp
import sys


def vertice_mais_proximo(ciclo, grafo):
    menor_peso = 9999999
    vertice_proximo = -1

    for i in range(len(ciclo)):
        for j in range(3, len(ciclo[i])):
            for key, value in ciclo[i][j].items():
                if value < menor_peso and value != 0:
                        vertice_proximo = key
                        menor_peso = value
                        aux_delete_coluna = j
    
    ciclo = np.delete(ciclo, aux_delete_coluna, axis=1)

    return vertice_proximo, ciclo


def calcula_insercoes(grafo, vertices_ciclo, vertice_mais_proximo):
    menor_custo_total = 9999999
    posicao_menor_custo = -1

    for i in range(len(vertices_ciclo) - 1):
        custo_total = grafo[vertices_ciclo[i]][vertice_mais_proximo] + grafo[vertice_mais_proximo][vertices_ciclo[i+1]] - grafo[vertices_ciclo[i]][vertices_ciclo[i+1]]

        if custo_total < menor_custo_total:
            menor_custo_total = custo_total
            posicao_menor_custo = i 

    vertices_ciclo.insert(posicao_menor_custo + 1, vertice_mais_proximo)

    return vertices_ciclo


def insercao_mais_proxima(grafo, ciclo, vertices_restantes, vertices_ciclo):
    while vertices_restantes > 0:
        vertice_proximo, ciclo = vertice_mais_proximo(ciclo, grafo)
        
        vertices_ciclo = calcula_insercoes(grafo, vertices_ciclo, vertice_proximo)

        vertices_restantes -= 1

    return vertices_ciclo


def run_insercao_mais_proxima():

    # grafo = np.array([[0, 1, 2, 7, 5], [1, 0, 3, 4, 3], [2, 3, 0, 5, 2], [7, 4, 5, 0, 3], [5, 3, 2, 3, 0]])

    problema = tsp.load_problem(sys.argv[1])

    matrix = np.array(problema._create_explicit_matrix().numbers)

    grafo = matrix.reshape(-1, problema.dimension)

    ciclo_inicial = grafo[0:3, :]
    novo_ciclo_inicial = []
    vertices_ciclo = [0, 1, 2, 0]

    for i in range(len(ciclo_inicial)):
        for j in range(len(ciclo_inicial[i])):
            novo_ciclo_inicial.append({j : ciclo_inicial[i][j]})

    novo_ciclo_inicial = np.array(novo_ciclo_inicial)
    novo_ciclo_inicial = novo_ciclo_inicial.reshape(-1, problema.dimension)
    vertices_restantes = len(grafo) - 3

    ciclo_final = insercao_mais_proxima(grafo, novo_ciclo_inicial, vertices_restantes, vertices_ciclo)
    custo_total = 0

    for i in range(len(ciclo_final) - 1):
        custo_total += grafo[ciclo_final[i]][ciclo_final[i+1]] 


    return grafo, ciclo_final

