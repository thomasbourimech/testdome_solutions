def find_path(start, end, graph, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(node, end, graph, path)
            if newpath:
                return newpath
    return None


def create_map(map_matrix):
    mapping = {}
    for i in range(len(map_matrix)):
        for j, value in enumerate(map_matrix[i]):
            mapping[(i, j)] = map_matrix[i][j]
    return mapping


def create_graph(map_matrix):
    mapping = create_map(map_matrix)
    graph = {}
    for x in range(len(map_matrix)):
        for y in range(len(map_matrix[x])):
            connected = []
            for tpl in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if mapping.get(tpl):
                    connected.append(tpl)
            graph[(x, y)] = connected
    return graph


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    graph = create_graph(map_matrix)
    path = find_path((from_row, from_column), (to_row, to_column), graph)
    if path is not None:
        return True


if __name__ == '__main__':

    map_matrix = [[True, False, False],
                  [True, True, False],
                  [False, True, True]]

    print(route_exists(0, 0, 2, 2, map_matrix))
