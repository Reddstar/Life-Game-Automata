import time

def start_generations(raw_data, rules=1, show_evolving=False, evolving_delay=2):
    """Transforms the raw data in a matrix and evolve generations as the generations number"""

    matrix = get_matrix_from_raw(raw_data)
    generation = 0
    steady_state = False
    while not steady_state:
        new_matrix = evolve_automata(matrix, rules)
        steady_state = check_stable_state(matrix, new_matrix)
        matrix = new_matrix
        if show_evolving:
            print (matrix)
            time.sleep(evolving_delay)
    
    return ''.join(matrix)

def get_matrix_from_raw(raw_data):
    """Transforms the raw input into the automata matrix"""

    return list(raw_data+'#')
    

def check_stable_state(old_cells, new_cells):
    """Checks if new generation cells are equal to previous generation cells, 
    if so, the system has arrived on a steady state"""

    same_cells = True
    for x in range(len(old_cells)):
        if old_cells[x] != new_cells[x]:
            same_cells = False

    return same_cells

def evolve_automata(matrix, rules=1):
    """
    Evolves the current celular automata applying the appropriate rules
    1: Sucessor rules
    0: Zero rules
    """

    new_gen_matrix = []
    for x in range(len(matrix)):
        if rules == 1:
            cell = apply_successor_rules(x, matrix)
        elif rules == 0:
            cell = apply_zero_rules(x, matrix)
        elif rules == 2:
            cell = apply_predecessor_rules(x, matrix)
        new_gen_matrix.append(cell)
    
    return new_gen_matrix


def apply_successor_rules(cell_position, matrix):
    """
    Applies the successor rules to a cell and returns the updated cell
    A cell # who has any number to the left and not any neighbors to the right, it will become ''.
    A cell # who has a '' or 0 to the right, it will become '0'
    A cell 1 who has # to the right, it will become '#'
    A cell 0 who has # to the right, it will become '1'
    """

    cell = matrix[cell_position]
    right_neighbor = get_right_neighbor(cell_position, matrix)
    left_neighbor = get_left_neighbor(cell_position, matrix)

    if cell == '#':
        if right_neighbor == None and (left_neighbor == '1' or left_neighbor == '0'):
            cell = ''
        elif right_neighbor == '' or right_neighbor == '0':
            cell = '0'
    elif cell == '1':
        if right_neighbor == '#':
            cell = '#'
    elif cell == '0':
        if right_neighbor == '#':
            cell = '1'

    return cell

def apply_predecessor_rules(cell_position, matrix):
    """
    Applies the successor rules to a cell and returns the updated cell
    A cell # who has any number to the left and not any neighbors to the right, it will become ' '.
    A cell # who has a ' ' or 1 to the right, it will become '1'
    A cell 0 who has # to the right, it will become '#'
    A cell 1 who has # to the right, it will become '0'
    """

    cell = matrix[cell_position]
    right_neighbor = get_right_neighbor(cell_position, matrix)
    left_neighbor = get_left_neighbor(cell_position, matrix)

    if cell == '#':
        if right_neighbor == None and (left_neighbor == '1' or left_neighbor == '0'):
            cell = ''
        elif right_neighbor == '' or right_neighbor == '1':
            cell = '1'
    elif cell == '0':
        if right_neighbor == '#':
            cell = '#'
    elif cell == '1':
        if right_neighbor == '#':
            cell = '0'

    return cell


def apply_zero_rules(cell_position, matrix):
    """
    Applies the zero rules to a cell and returns the updated cell
    All cells except for # and '', will become 0
    """
    cell = matrix[cell_position]
    if cell == '#' or cell == '':
        return ''
    else:
        return '0'

def get_right_neighbor(x, matrix):
    """Gets right neighbor of a cell by its given position"""

    if x >= (len(matrix) - 1):
        return None
    else:
        return matrix[x + 1]

def get_left_neighbor(x, matrix):
    """Gets the left neighbor of a cell by its given position"""

    if x <= 0:
        return None
    else:
        return matrix[x - 1]


def Z(x):
    return start_generations(x, 0)

def S(x):
    return start_generations(x, 1)

def Pred(x):
    if x == Z(x):
        return x
    else:
        return start_generations(x, 2)

def Add(x, y):
    if x == Z(x):
        return y
    else:
        return S(Add(Pred(x), y))
    
def Prod(x, y):
    if x == Z(x):
        return Z(x)
    else:
        return Add(y, Prod(Pred(x), y))

def Exp(x, y):
    if x == Z(x):
        return S(Z(x))
    else:
        return Prod(y, Exp(Pred(x), y))

if __name__ == "__main__":
    print (Exp("0011", "0010"))
