def gardenNoAdj(N: int, paths):
    graph = [[] for _ in range(N)]
    for path in paths:
        graph[path[0] - 1].append(path[1] - 1)
        graph[path[1] - 1].append(path[0] - 1)
    res = [0 for _ in range(N)]
    for i in range(N):
        # python支持直接集合相减，减完直接随便取一个就可以
        res[i] = ({1, 2, 3, 4} - {res[j] for j in graph[i]}).pop()
    return res


if __name__ == '__main__':
    N = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    res = gardenNoAdj(N, paths)
    print(res)
