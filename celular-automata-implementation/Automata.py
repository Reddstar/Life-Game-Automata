def start_generations(raw_data, generations):
    parts = initial_configuration.split(" ")
    matrix = get_matrix_from_raw(raw_data)
    for i in range(generations):
        try:
            matrix = 

def evolve_automata(matrix):
    pass

def get_vertical_neighboors(position):
    x = position[0]
    y = position[1]
    

def get_matrix_from_raw(raw_data):
    matrix = []
    for i in range(4):
        matrix.append(list(parts[i]))
    return matrix


def show_current_configuration(configuration_matrix):
    for x in range(len(configuration_matrix)):
        for y in range(len(configuration_matrix[0])):
            print (configuration_matrix[x][y], end=' ')
        print ("")

start_generations("0001 0010 0101 0000 # 0000 0000 0000 0000", 1)