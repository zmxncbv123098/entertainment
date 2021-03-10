import time


def print_beautify(arr):
    for i in arr:
        elem = eval(i)
        for j in elem:
            print(*j)
        print("=" * 20)


def puzz_breadth_first(start, end):
    """
    Breadth First algorithm
    """
    front = [[start]]
    expanded = []
    expanded_nodes = 0
    while front:
        i = 0
        for j in range(1, len(front)):  # minimum
            if len(front[i]) > len(front[j]):
                print(front[i], " > ", front[j])
                i = j
        path = front[i]
        front = front[:i] + front[i + 1:]
        endnode = path[-1]
        if endnode in expanded:
            continue
        for k in moves(endnode):
            if k in expanded:
                continue
            front.append(path + [k])
        expanded.append(endnode)
        expanded_nodes += 1
        if endnode == end:
            break
    print("Expanded nodes:", expanded_nodes)
    print("Solution:")
    print_beautify(path)


def moves(mat):
    output = []
    initial_mtx = eval(mat)
    # zero_coord = initial_mtx.index(0)

    m = eval(mat)
    i = 0
    while 0 not in m[i]:
        i += 1
    j = m[i].index(0)  # blank space (zero)

    if i > 0:
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]  # move up
        if (manh(initial_mtx) - manh(m)) == 1.0:
            output.append(str(m))
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]

    if i < 2:
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]  # move down
        if (manh(initial_mtx) - manh(m)) == 1.0:
            output.append(str(m))
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]

    if j > 0:
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]  # move left
        if (manh(initial_mtx) - manh(m)) == 1.0:
            output.append(str(m))
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]

    if j < 2:
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]  # move right
        if (manh(initial_mtx) - manh(m)) == 1.0:
            output.append(str(m))
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]
    return output


def manh_dst_matrix(a, b, n):
    """

    :param a: Индекс нулевого эл-та
    :param b: Будующий нулевой индекс
    :param n: Размер квадратной матрицы
    :return: Манхэттенское расст
    """
    return abs(a % n - b % n) + abs(a // n - b // n)


def make_vector(arr):
    res = []
    for i in arr:
        for j in i:
            res.append(j)
    return res


def manh(puzz):
    distance = 0
    try:
        m = eval(puzz)
    except TypeError:
        m = puzz
    for i in range(3):
        for j in range(3):
            if m[i][j] == 0:
                continue
            distance += abs(i - (m[i][j] / 3)) + abs(j - (m[i][j] % 3))
    return distance


if __name__ == '__main__':
    puzzle = str([[1, 2, 3], [4, 0, 8], [7, 6, 5]])
    end = str([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    puzz_breadth_first(puzzle, end)
