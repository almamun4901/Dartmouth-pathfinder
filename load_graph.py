# Name: Md Al Mamun
# Date: 11/13/2022
# Purpose: Lab4

# load graph function to read the file

from vertex import Vertex

def load_graph(file_name):

    file = open(file_name, 'r')
    #vertex dictionary
    vdict = {}

    #reading file line by line and spliting
    for line in file:
        #spliting by ;
        section_split = line.split(';')
        #spliting x and y
        co_ordinates = section_split[2].split(',')

        vertices_name = section_split[0]

        #vertex obejcts
        vertex = Vertex(vertices_name, co_ordinates[0].strip(), co_ordinates[1].strip())
        vdict[vertices_name] = vertex

    #print(vdict)
    file.close()

    #new loop for getting the adjacents
    file = open(file_name)
    for line in file:
        section_split = line.split(';')
        vertices_name = section_split[0]
        #spliting adjacents
        adjacents = section_split[1].strip().split(',')
        #print(adjacents)
        for adj_vertices in adjacents:
            new = adj_vertices.strip()
            vdict[vertices_name].adjacent_list.append(vdict[new])

    return vdict

    file.close()




#load_graph('dartmouth_graph.txt')