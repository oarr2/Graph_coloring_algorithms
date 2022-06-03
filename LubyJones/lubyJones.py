'''
-color list (shared)
-random list (not shared)
-vertex list (not shared)
-arrayList (not shared)
'''
from random import Random
import multiprocessing
from multiprocessing import Barrier, Process
from socket import timeout
import time

from lubyJonesThread import write_values

random = Random()
process_count = 4

def init_values(adj_list, n_vertex):
    vertex_set = set([])
    weight_list = []
    for vertex in range(len(adj_list)):
        vertex_set.add(vertex)
    
    temp_index = 0
    random_set = set({})
    while temp_index < n_vertex:
        r_number = random.randint(1, 100*n_vertex)
        if not r_number in random_set:
            temp_index += 1
            random_set.add(r_number)
    
    for weight in random_set:
        weight_list.append(weight)
    
    return [vertex_set, weight_list]

def read_values(adj_list, n, p):
    n_vertex, n_edges = [0,0]
    with open("../testCases/test_" + str(n) + "_" + str(p) + ".txt", "r") as f:
    #with open("../testCases/example_test.txt", "r") as f:
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
    return [n_vertex, n_edges, adj_list]

def find_max(process_id, color_list, weight_list, adj_list, work_start, work_complete):
    while True:
        start = time.time()
        work_start.wait()
        #print("here in my while true")
        for v_index in range(process_id, len(weight_list), process_count):
            if is_max(v_index, weight_list, adj_list, color_list):
                #color_list[v_index] = color
                color_vertex(v_index, adj_list, color_list)
        work_complete.wait()
        end = time.time()
    #print("find max", end - start)
    
def find_min(process_id, color_list, weight_list, adj_list):
    for v_index in range(process_id, len(color_list), process_count):
        if is_min(v_index, weight_list, adj_list):
            color_vertex(v_index, adj_list, color_list)

def color_vertex(vertex, adj_list, color_list):
    new_color = -1
    min_color = -1
    max_color = -1
    temp_c_set = set({})
    for neighbor in adj_list[vertex]:
        if color_list[neighbor] != -1:
            temp_c_set.add(color_list[neighbor])
            if min_color == -1:
                min_color = color_list[neighbor]
            else:
                min_color = min(min_color, color_list[neighbor])
            max_color = max(max_color, color_list[neighbor])
    for i in range(min_color - 1, max_color + 2):
        if i >= 0:
            if not i in temp_c_set:
                new_color = i
                break
    color_list[vertex] = new_color 


def is_min(vertex, weight_list, adj_list):
    for neighbor in adj_list[vertex]:
        if weight_list[vertex] > weight_list[neighbor]:
            return False
    return True

def is_max(vertex, weight_list, adj_list, color_list):
    if color_list[vertex] != -1:
        return False
    for neighbor in adj_list[vertex]:
        if color_list[neighbor] != -1:
            continue
        if weight_list[vertex] < weight_list[neighbor]:
            return False
    return True

def luby_jones(color_list, weight_list, adj_list, work_start, work_complete):
    
    for process_id in range(process_count):
        start = time.time()
        p = Process(target=find_max, args=(process_id, color_list, weight_list, adj_list, work_start, work_complete))
        p.start()
        end = time.time()
        print("luby_jones", end - start)
    
    while -1 in color_list:
        #print("while color")
        work_start.wait()
        #print("here i am")
        work_complete.wait()
    work_start.abort()
    
        

def run():
    multiprocessing.set_start_method('spawn')
    values = []
    num_vertex = [100, 1000, 2000, 4000]
    for n in num_vertex:
        for p in range(1, 11):
            work_start = Barrier(process_count + 1)
            work_complete = Barrier(process_count + 1)
            start = time.time()
            adj_list = []
            n_vertex, n_edges, adj_list = read_values(adj_list, n, p)
            vertex_set,weight_list = init_values(adj_list, n_vertex)
            color_list = multiprocessing.Array('i', [-1] * n_vertex, lock=False)
            print("start with ", n, " vertex and ", p, "probability")
            main_process = Process(target=luby_jones, args=([color_list, weight_list, adj_list, work_start, work_complete]))
            main_process.start()
            main_process.join()
            print("end")
            colors = set({})
            for colo in color_list:
                colors.add(colo)
            print("the chromatic number is", len(colors), "the probability is", p)
            end = time.time()
            values.append([len(colors), p/10, end - start])
    write_values(values)
if __name__ == '__main__':
    
    
    run()