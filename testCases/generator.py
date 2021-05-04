#importing the networkx library
import networkx as nx

def generate_graph(n_vertex, p):
    G = nx.erdos_renyi_graph(n_vertex, p)
    matrix = nx.adj_matrix(G)
    matrix = matrix.toarray()
    vertex = len(matrix)
    edges = 0
    for line in matrix:
        for val in line:
            if val == 1:
                edges += 1
    edges = edges//2
    with open("test_" + str(n_vertex) + "_" + str(int(p*10)) + ".txt", "w") as f:
        i = 0
        j = 0
        extra_edges = set({})
        print(str(vertex) + " " + str(edges))
        f.write(str(vertex) + " " + str(edges))
        for line in matrix:
            j = 0
            for column in line:
                if column == 1:
                    pair = (i,j)
                    if not pair in extra_edges: 
                        f.write("\n")
                        f.write(str(i) + " " + str(j))
                        extra_edges.add((i,j))
                        extra_edges.add((j,i))
                j += 1
            i += 1

def run():
    for p in range(1, 11):
        generate_graph(100, p/10)

    for p in range(1, 11):
        generate_graph(1000, p/10)
    
    for p in range(1, 11):
        generate_graph(2000, p/10)

if __name__ == "__main__":
    run()