# Name: Md Al Mamun
# Date: 11/13/2022
# Purpose: Lab4

# import functions and libraries
from cs1lib import *
from load_graph import *
from breadthFirst_search import *
from vertex import Vertex

# setting window
WINDOW_X = 1012
WINDOW_Y = 811

#boolean values
visible = False
pressed = False

#initialize values
mx = 0
my = 0
move_x = 0
move_y = 0

#loading vertex graphs
vertex_dict = load_graph('dartmouth_graph.txt')

#initialize vertexes
start_vertex = None
goal_vertex = None

# mouse pressed function
def mpressed(x, y):
    global mx,my, pressed
    pressed = True
    if pressed == True:
        mx = x
        my = y

#moving mouse function
def mouse_move(cx, cy):
    global move_x, move_y

    move_x = cx
    move_y = cy

#main draw function
def myDraw():
    global visible, start_vertex, goal_vertex

    #laod the image only once
    if visible == False:
        map_img = load_image('dartmouth_map.png')
        draw_image(map_img, 0, 0)
        visible = True


    #draw the blue vertex and edges
    for item in vertex_dict:
        vertex_dict[item].draw_vertex(0,0,1)
        vertex_dict[item].draw_edge_lines(0,0,1)

    #draw red start vertex and set the start point
    for item in vertex_dict:
        if pressed == True and vertex_dict[item].smallest_square(mx,my):
            start_vertex = vertex_dict[item]
            start_vertex.draw_vertex(1,0,0)

    #set the goal vertex
    for item in vertex_dict:
        if vertex_dict[item].smallest_square(move_x, move_y) and start_vertex != None :
            goal_vertex = vertex_dict[item]
            goal_vertex.draw_vertex(1,0,0)


    #draw the shortest path using BFS
    if start_vertex != None and goal_vertex != None:
        path = bfs(start_vertex,goal_vertex)

    #draw path
        i = 0
        while i < len(path) - 1:
            path[i].draw_vertex(1,0,0)
            path[i].draw_edges(path[i + 1], 1, 0, 0)
            i = i + 1


start_graphics(myDraw, width=WINDOW_X, height= WINDOW_Y, mouse_press=mpressed, mouse_move=mouse_move)