link_matrix = [
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0]]


def get_indices_links(matrix):
    result_matrix = []
    for raw in matrix:
        indices = [i for i, x in enumerate(raw) if x == 1]
        result_matrix.append(indices)
    return result_matrix


def get_input_sequence(input_vector, indices):
    sequence = []
    for raw in indices:
        sequence.append(input_vector[raw[0]])
        sequence.append(input_vector[raw[1]])
    return sequence


logic = [lambda x, y: x or y,
         lambda x, y: x and y,
         lambda x, y: not x or y,
         lambda x, y: x or y,
         lambda x, y: x and y,
         lambda x, y: not x or y]


def state(input_vector):
    result_vector = []
    indices = get_indices_links(link_matrix)
    sequence = get_input_sequence(input_vector, indices)
    # print(sequence)
    for logix_idx, link_idx in enumerate(range(0, len(sequence), 2)):
        a, b = sequence[link_idx], sequence[link_idx + 1]
        result_vector.append(int(logic[logix_idx](a, b)))
    return result_vector


for i in range(64):
    vector = list('{0:06b}'.format(i))
    attractors = []
    # vector = [1, 1, 0, 1, 0, 1]
    state_id = 0
    while vector not in attractors:
        print(state_id, "State", *vector)
        attractors.append(vector)
        vector = state(vector)
        state_id += 1
    print(state_id, "State", *vector)
    print("Len Attractor:", len(attractors) - attractors.index(vector))
    print("="*30)
