import matplotlib.pyplot as plt

def read_color_prob(prefix, a, b):
    points_x_100 = []
    points_y_100 = []
    points_x_1000 = []
    points_y_1000 = []
    points_x_2000 = []
    points_y_2000 = []
    with open('../Dsatur/dsatur_results.txt', 'r') as f:
        index = 0
        for line in f:
            if index > 0 and index <= 10:
                line = line.split()
                points_x_100.append(float(line[b]))
                points_y_100.append(float(line[a]))
            if index > 10 and index <= 20:
                line = line.split()
                points_x_1000.append(float(line[b]))
                points_y_1000.append(float(line[a]))
            if index > 20 and index <= 30:
                line = line.split()
                points_x_2000.append(float(line[b]))
                points_y_2000.append(float(line[a]))
            index += 1
    
    r_points_x_100 = []
    r_points_y_100 = []
    r_points_x_1000 = []
    r_points_y_1000 = []
    r_points_x_2000 = []
    r_points_y_2000 = []
    with open('../RFL/rfl_results.txt', 'r') as f:
        index = 0
        for line in f:
            if index > 0 and index <= 10:
                line = line.split()
                r_points_x_100.append(float(line[b]))
                r_points_y_100.append(float(line[a]))
            if index > 10 and index <= 20:
                line = line.split()
                r_points_x_1000.append(float(line[b]))
                r_points_y_1000.append(float(line[a]))
            if index > 20 and index <= 30:
                line = line.split()
                r_points_x_2000.append(float(line[b]))
                r_points_y_2000.append(float(line[a]))
            index += 1
            
    l_points_x_100 = []
    l_points_y_100 = []
    l_points_x_1000 = []
    l_points_y_1000 = []
    l_points_x_2000 = []
    l_points_y_2000 = []
    with open('../LubyJones/lubyJones_results.txt', 'r') as f:
        index = 0
        for line in f:
            if index > 0 and index <= 10:
                line = line.split()
                l_points_x_100.append(float(line[b]))
                l_points_y_100.append(float(line[a]))
            if index > 10 and index <= 20:
                line = line.split()
                l_points_x_1000.append(float(line[b]))
                l_points_y_1000.append(float(line[a]))
            if index > 20 and index <= 30:
                line = line.split()
                l_points_x_2000.append(float(line[b]))
                l_points_y_2000.append(float(line[a]))
            index += 1
            
    plt.plot(points_x_100, points_y_100, color='black', linewidth=1, linestyle="-.")
    plt.plot(r_points_x_100, r_points_y_100, color='red', linewidth=1, linestyle="--")
    plt.plot(l_points_x_100, l_points_y_100, color='green', linewidth=1, linestyle="-")
    plt.scatter(points_x_100, points_y_100, s=5, color='black')
    plt.scatter(r_points_x_100, r_points_y_100, s=5, color='red')
    plt.scatter(l_points_x_100, l_points_y_100, s=5, color='green')
    plt.xlabel("Probabilidad")
    plt.ylabel(prefix)
    plt.grid()
    plt.savefig(prefix + "graph_with_100.png")
    plt.show()
    plt.close()
    
    plt.plot(points_x_1000, points_y_1000, color='black', linewidth=1, linestyle="-.")
    plt.plot(r_points_x_1000, r_points_y_1000, color='red', linewidth=1, linestyle="--")
    plt.plot(l_points_x_1000, l_points_y_1000, color='green', linewidth=1, linestyle="-")
    plt.scatter(points_x_1000, points_y_1000, s=5, color='black')
    plt.scatter(r_points_x_1000, r_points_y_1000, s=5, color='red')
    plt.scatter(l_points_x_1000, l_points_y_1000, s=5, color='green')
    plt.xlabel("Probabilidad")
    plt.ylabel(prefix)
    plt.grid()
    plt.savefig(prefix + "graph_with_1000.png")
    plt.show()
    plt.close()
    
    plt.plot(points_x_2000, points_y_2000, color='black', linewidth=1, linestyle="-.")
    plt.plot(r_points_x_2000, r_points_y_2000, color='red', linewidth=1, linestyle="--")
    plt.plot(l_points_x_2000, l_points_y_2000, color='green', linewidth=1, linestyle="-")
    plt.scatter(points_x_2000, points_y_2000, s=5, color='black')
    plt.scatter(r_points_x_2000, r_points_y_2000, s=5, color='red')
    plt.scatter(l_points_x_2000, l_points_y_2000, s=5, color='green')
    plt.xlabel("Probabilidad")
    plt.ylabel(prefix)
    plt.grid()
    plt.savefig(prefix + "graph_with_2000.png")
    plt.show()
    plt.close()
    


read_color_prob("Cantidad de Colores",0 , 1)
read_color_prob("Tiempo (s)", 2, 1)