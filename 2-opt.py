import numpy as np
import tsplib95 as tsp
import timeit
from insercaoMaisProxima import run_insercao_mais_proxima


def troca_dois_opt(solucao_hlinha, aresta_atual_i, aresta_atual_j, nao_adjacente_i, nao_adjacente_j):

    aux = solucao_hlinha[aresta_atual_j]
    solucao_hlinha[aresta_atual_j] = solucao_hlinha[nao_adjacente_i]
    solucao_hlinha[nao_adjacente_i] = aux

    return solucao_hlinha


def custo_solucao(grafo, solucao_h):
    custo_total = 0

    for i in range(len(solucao_h) - 1):
        custo_total += grafo[solucao_h[i]][solucao_h[i+1]]

    return custo_total


def main_2opt():

    start = timeit.default_timer()

    grafo, solucao_h = run_insercao_mais_proxima()

    tamanho_solucao = 0
    custo_solucaoh = custo_solucao(grafo, solucao_h)

    if len(solucao_h) % 2 == 0:
        tamanho_solucao = int((len(solucao_h) / 2)) - 1
    else:
        tamanho_solucao = int((len(solucao_h) / 2)) - 1

    for i in range(tamanho_solucao):
        for j in range(i + 2, len(solucao_h) - 1):
            if i == 0 and j == len(solucao_h) - 2:
                break
            solucao_aux = solucao_h[:]
            solucao_hlinha = troca_dois_opt(solucao_aux, i, i+1, j, j+1)
            if custo_solucao(grafo, solucao_hlinha) < custo_solucaoh:
                solucao_h = solucao_hlinha       

    stop = timeit.default_timer()

    print("\nsolução inserção mais próxima: " + str(custo_solucaoh))
    print("2-opt melhorativa: " + str(custo_solucao(grafo, solucao_h)))

    print("Tempo de execução: " + str(stop - start))

main_2opt()