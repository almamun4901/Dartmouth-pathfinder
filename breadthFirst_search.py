# Name: Md Al Mamun
# Date: 11/13/2022
# Purpose: Lab4

from collections import *
from vertex import Vertex


def bfs(start, goal):
    q = deque()
    back_pointer = {}

    q.append(start)

    back_pointer[start] = None



    while len(q) > 0:
        curr_v = q.popleft()

        for vertex in curr_v.adjacent_list:
            if vertex not in back_pointer:
                q.append(vertex)
                back_pointer[vertex] = curr_v

        if goal in back_pointer:
            break

    path = []
    v = goal
    while v is not None:
        path.append(v)
        v = back_pointer[v]


    return path
