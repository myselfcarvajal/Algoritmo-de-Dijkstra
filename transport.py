def dijkstra(Grafo, salida, prioridad):
    dist, prev = {}, {}
    result = {}

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = [vertice for vertice in Grafo]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for vecino in Grafo[u]:
            medio_transporte_optimo = None
            tiempo_optimo = float("inf") if prioridad == 'tiempo' else 0
            costo_optimo = float("inf") if prioridad == 'costo' else 0

            for medio_transporte in Grafo[u][vecino]:
                tiempo = Grafo[u][vecino][medio_transporte]['time']
                costo = Grafo[u][vecino][medio_transporte]['cost']

                if prioridad == 'tiempo' and tiempo < tiempo_optimo:
                    tiempo_optimo = tiempo
                    medio_transporte_optimo = medio_transporte
                elif prioridad == 'costo' and costo < costo_optimo:
                    costo_optimo = costo
                    medio_transporte_optimo = medio_transporte

            if medio_transporte_optimo:
                if prioridad == 'tiempo':
                    if vecino in Q and dist[vecino] > dist[u] + tiempo_optimo:
                        dist[vecino] = dist[u] + tiempo_optimo
                        prev[vecino] = u
                        result[vecino] = medio_transporte_optimo
                else:
                    if vecino in Q and dist[vecino] > dist[u] + costo_optimo:
                        dist[vecino] = dist[u] + costo_optimo
                        prev[vecino] = u
                        result[vecino] = medio_transporte_optimo

    return result, dist, prev


def obtener_prioridad():
    prioridad = input("Ingresa la prioridad (tiempo o costo): ").lower()
    while prioridad not in ['tiempo', 'costo']:
        print("Prioridad inválida. Debe ser tiempo o costo.")
        prioridad = input("Ingresa la prioridad (tiempo o costo): ").lower()
    return prioridad


grafo = {
    'a': {'b': {'T': {'time': 4, 'cost': 8}, 'A': {'time': 2, 'cost': 15}, 'M': {'time': 6, 'cost': 10}}, 'c': {'T': {'time': 3, 'cost': 5}, 'A': {'time': 1, 'cost': 12}, 'M': {'time': 5, 'cost': 8}}},
    'b': {'d': {'T': {'time': 5, 'cost': 7}, 'A': {'time': 3, 'cost': 10}, 'M': {'time': 8, 'cost': 5}}},
    'c': {'b': {'T': {'time': 2, 'cost': 6}, 'A': {'time': 4, 'cost': 9}, 'M': {'time': 7, 'cost': 12}}, 'd': {'T': {'time': 3, 'cost': 4}, 'A': {'time': 2, 'cost': 8}, 'M': {'time': 5, 'cost': 6}}, 'e': {'T': {'time': 6, 'cost': 10}, 'A': {'time': 4, 'cost': 12}, 'M': {'time': 9, 'cost': 15}}},
    'd': {'f': {'T': {'time': 5, 'cost': 7}, 'A': {'time': 3, 'cost': 10}, 'M': {'time': 8, 'cost': 5}}, 'e': {'T': {'time': 1, 'cost': 3}, 'A': {'time': 2, 'cost': 6}, 'M': {'time': 4, 'cost': 4}}},
    'e': {'g': {'T': {'time': 5, 'cost': 9}, 'A': {'time': 2, 'cost': 11}, 'M': {'time': 7, 'cost': 10}}},
    'g': {'z': {'T': {'time': 4, 'cost': 6}, 'A': {'time': 2, 'cost': 8}, 'M': {'time': 6, 'cost': 10}}},
    'f': {'g': {'T': {'time': 2, 'cost': 4}, 'A': {'time': 1, 'cost': 6}, 'M': {'time': 3, 'cost': 5}}, 'z': {'T': {'time': 7, 'cost': 11}, 'A': {'time': 5, 'cost': 15}, 'M': {'time': 10, 'cost': 18}}},
    'z': {}
}

prioridad = obtener_prioridad()
s, distancia, previos = dijkstra(grafo, 'a', prioridad)
print(f"Prioridad: {prioridad}")
print(f"Mejor ruta y medio de transporte: {s}")
print(f"Tiempo mínimo: {distancia}")
print(f"Camino previo: {previos}")


