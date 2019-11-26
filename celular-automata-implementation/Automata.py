import time

def start_generations(raw_data, generations, show_evolving=False, evolving_delay=2):
    """Transforms the raw data in a matrix and evolve generations as the generations number"""

    matrix = get_matrix_from_raw(raw_data, 4)
    print ("==== Starting Configuration ====")
    show_given_configuration(matrix)
    print ("================================")
    generation = 0
    stop_evolving = False
    while generation < generations and not stop_evolving:
        try:
            matrix = [] + evolve_automata(matrix, 4)
            generation += 1
            if show_evolving:
                time.sleep(evolving_delay)
                show_given_configuration(matrix)
                print ("----------------")          
        except:
            print ("Unexpected Break")
            show_given_configuration(matrix)
            stop_evolving = True

    print ("===== Final Configuration =====")
    show_given_configuration(matrix)
    print ("===============================")
            

def evolve_automata(matrix, n):
    """Evolves the current celular automata applying Life Game rules"""

    new_gen_matrix = []
    for x in range(n):
        new_gen_line = []
        for y in range(n):
            cell_position = (x, y)
            cell = apply_rules(cell_position, matrix)
            new_gen_line.append(cell)
        gen_line = [] + new_gen_line
        new_gen_matrix.append(gen_line)
    
    return new_gen_matrix


def apply_rules(cell_position, matrix):
    """Apply rules to a cell and returns the updated cell"""

    x = cell_position[0]
    y = cell_position[1]
    cell = matrix[x][y]
    neighbors = get_vertical_neighborhood(cell_position, matrix)
    alive_cells = count_alive_cells(neighbors)

    if cell == '1' and (alive_cells <= 1 or alive_cells == 4):
        cell = '0'
    elif cell == '0' and alive_cells == 3:
        cell = '1'
    
    return cell

def count_alive_cells(neighbors):
    """Counts the number of cells which are alive in the neighborhood"""

    cell_count = 0
    for cell in neighbors:
        if cell == '1':
            cell_count += 1
    
    return cell_count


def get_vertical_neighborhood(position, matrix):
    """Gets the vertical neighbors of a cell by its given position"""

    x = position[0]
    y = position[1]
    all_positions = [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]
    valid_positions = check_valid_positions(all_positions, 0, len(matrix) - 1)
    neighbors = []
    for p in valid_positions:
        neighbors.append(matrix[p[0]][p[1]])
    
    return neighbors
    
def check_valid_positions(positions, min, max):
    """Return only the valid positions using the min and max coordinate possible"""

    valid_positions = []
    for position in positions:
        x = position[0]
        y = position[1]
        if (x >= min and x <= max) and (y >= min and y <= max):
            valid_positions.append(position)
    return valid_positions
    

def get_matrix_from_raw(raw_data, n):
    """Transforms the raw input into the automata matrix"""

    parts = raw_data.split(" ")
    matrix = []
    for i in range(n):
        matrix.append(list(parts[i]))
    return matrix


def show_given_configuration(configuration_matrix):
    """Shows give configuration formatted as matrix"""

    for x in range(len(configuration_matrix)):
        for y in range(len(configuration_matrix[0])):
            print (configuration_matrix[x][y], end=' ')
        print ("")

if __name__ == "__main__":
    start_generations("1011 1111 1111 1111 # 0000 0000 0000 0000", 4, True)