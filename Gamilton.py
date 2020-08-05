A =  [[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # Матрица Смежности для заданого графа
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]]

n = 11 # Количество Вершин

Visited = [False] * n
Path = [] # Гамильтонов цикл

def hamilton(current):
    Path.append(current)
    if len(Path) == n:
        print(Path)
        if A[Path[0]][Path[-1]] == 1 or A[Path[-1]][Path[0]] == 1: # Проверка на Гамильтонов цикл
            return True
        else:
            Path.pop()
            return False
    Visited[current] = True

    for i in range(n):
        if A[current][i] == 1 and not Visited[i]:
            if hamilton(i): # Рекурсивный вызов для непосещенных вершин
                return True
    Visited[current] = False
    Path.pop()

    return False

print(hamilton(0))
            
