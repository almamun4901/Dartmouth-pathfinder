# Name: Md Al Mamun
# Date: 11/13/2022
# Purpose: Lab4

#vertex class for the lab

from cs1lib import *

VERTEX_RADIUS = 5
EDGE_WIDTH = 3

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.adjacent_list = []
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        string = ""
        for vertex in self.adjacent_list:
            string = string + ", " + vertex.name

        string = string.strip(',')

        return str(self.name)+";"+" Location: "+str(self.x)+", "+str(self.y)+";"+" Adjacent vertices:"+ string

    def draw_vertex(self, r=0, g=0, b=1):  # Function to draw the vertex
        disable_stroke()  # Disables stroke, which is important for the graph
        set_fill_color(r, g, b)  # set the color and draw a circle with VERTEX_RADIUS
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    def draw_edges(self, point, r=0, g=0, b=1):  # Function to draw the edges between self and all vertices in the adjacency list
        enable_stroke()  # Enables stroke so line is visible
        set_stroke_color(r, g, b)  # Set color, width and then, in a for loop, draw a line between self and every other adjacent vertex
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, point.x, point.y)

    def draw_edge_lines(self, r, g, b):
        for element in self.adjacent_list:
            self.draw_edges(element,0,0,1)

    def smallest_square(self, x, y):  # Return a boolean indicating whether the mouse is pointing to the self vertex or not
        if self.x - VERTEX_RADIUS <= x <= self.x + VERTEX_RADIUS and self.y - VERTEX_RADIUS <= y <= self.y + VERTEX_RADIUS:
            return True
        else:
            return False