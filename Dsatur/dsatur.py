color_list = []

#fill these values with read_values method
adj_list = []
n_vertex = 0
n_edges = 0

def read_values():
    global adj_list
    global n_vertex
    global n_edges
    with open("../testCases/example_test.txt", "r") as f:
        index = 0
        line_value = []
        for line in f:
            line_value = line.split()
            if(index == 0):
                n_vertex = int(line_value[0])
                n_edges = int(line_value[1])
                index = 1
                adj_list = [[] for i in range(n_vertex)]
            else:
                adj_list[int(line_value[0])].append(int(line_value[1]))
                adj_list[int(line_value[1])].append(int(line_value[0]))

#this can be optimized using a better data Structure
def get_vertex(sat_degree_list, processed_vertex):
    vertex = 0
    max_sat_degree = 0
    for v_index in range(len(sat_degree_list)):
        if not v_index in processed_vertex:
            sat_degree = len(sat_degree_list[v_index])
            if sat_degree >= max_sat_degree:
                max_sat_degree = sat_degree
                vertex = v_index
    return vertex

#this can be optimized using a better graph container (list of sets)
def is_independent_set(color_set, vertex):
    global adj_list
    for cur_vertex in color_set:
        if vertex in adj_list[cur_vertex]:
            return False
    return True

def dsatur(vertex_set):
    #init the sat_degree_list
    sat_degree_list = [[] for vertex in vertex_set]
    #start the algorithm
    processed_vertex = set({})
    while len(vertex_set) != 0:
        vertex = get_vertex(sat_degree_list, processed_vertex)
        last_color = 0
        for color_set in color_list:
            if is_independent_set(color_set, vertex) == True:
                color_set.add(vertex)
                processed_vertex.add(vertex)
                break
            else:
                last_color+=1
        if(last_color >= len(color_list)):
            new_color_set = {vertex}
            color_list.append(new_color_set)
            processed_vertex.add(vertex)
        vertex_set.remove(vertex)
    print('The color list is:')    
    print(color_list)
    return len(color_list)

def get_vertex_set():
    global adj_list
    vertex_set = set({})
    for vertex in range(len(adj_list)):
        vertex_set.add(vertex)
    return vertex_set

def run():
    read_values()  
    vertex_set = get_vertex_set()
    chr_num = dsatur(vertex_set)
    print("The chromatic number is " + str(chr_num))

if __name__ == '__main__':
    run()