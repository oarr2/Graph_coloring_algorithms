import time
color_list = []

#fill these values with read_values method
adj_list = []
n_vertex = 0
n_edges = 0

def get_v_neighbors(vertex, processed_vertex):
    global adj_list
    v_neighbors = set({})
    for v_neighbor in adj_list[vertex]:
        if not v_neighbor in processed_vertex:
            v_neighbors.add(v_neighbor)
    return v_neighbors

def read_values(n, p):
    global adj_list
    global n_vertex
    global n_edges
    with open("../testCases/test_" + str(n) + "_" + str(p) + ".txt", "r") as f:
    #with open("../testCases/test_100_10.txt", "r") as f:
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

#this can be optimized using a better structure to get the max_degree
def get_vertex (processed_vertex, temp_vertex_set):
    vertex = -1
    max_degree = -1
    for v_index in range(len(adj_list)):
        degree = len(adj_list[v_index])
        if not v_index in processed_vertex and not v_index in temp_vertex_set:
            if(degree >= max_degree):
                max_degree = degree
                vertex = v_index
    return vertex

def remove_from_set(vertex_set, temp_vertex_set, temp_vertex):
    for vertex in temp_vertex_set:
        if vertex in vertex_set:
            vertex_set.remove(vertex)
    if temp_vertex in vertex_set:
            vertex_set.remove(temp_vertex)
    return vertex_set

def rfl(vertex_set):
    last_color = -1
    processed_vertex = set({})
    while len(vertex_set) != 0:
        last_color+=1
        color_class = set({})
        temp_vertex_set = set({})
        while len(vertex_set) != 0:
            vertex = get_vertex(processed_vertex, temp_vertex_set)
            processed_vertex.add(vertex)
            color_class.add(vertex)
            temp_vertex_set.update(get_v_neighbors(vertex, processed_vertex))
            vertex_set = remove_from_set(vertex_set, temp_vertex_set, vertex)
        color_list.append(color_class)
        vertex_set = temp_vertex_set
    #print('the color list is')
    #print(color_list)
    return len(color_list)

def get_vertex_set():
    global adj_list
    vertex_set = set({})
    for vertex in range(len(adj_list)):
        vertex_set.add(vertex)
    return vertex_set

def write_values(values):
    with open("rfl_results.txt", "w") as f:
        f.write("Chromatic_number Edge_Probability Time")
        for line in values:
            f.write("\n")
            f.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]))

def run():
    
    num_vertex = [100, 1000, 2000, 4000]
    global color_list
    values = []
    for n in num_vertex:
        for p in range(1, 11):
            start = time.time()
            color_list = []
            read_values(n, p)  
            vertex_set = get_vertex_set()
            chr_num = rfl(vertex_set)
            #print("The chromatic number is " + str(chr_num) + " and probability of " + str(p/10))
            end = time.time()    
            values.append([chr_num, p/10, end - start])
    write_values(values)
if __name__ == '__main__':
    run()