def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    if start not in graph:
        return None
    
    for node in graph[start]:
        if node not in path:
            newpath = findPath(graph, node, end, path)
            if newpath:
                return newpath
    return None


def main():
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['E'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

    print(findPath(graph, 'B', 'D'))

main()

