#!/usr/bin/env python3
# -*- coding: utf-8 -*-

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'D', 'F', 'G'],
    'D': ['A', 'C', 'G'],
    'E': ['B'],
    'F': ['B', 'C'],
    'G': ['C', 'D']
}


def BFS(start, graph):
    queue = []
    visit = []
    queue.append(start)
    visit.append(start)
    while queue:
        node = queue.pop(0)
        nodes = graph[node]
        for i in nodes:
            if i not in visit:
                queue.append(i)
                visit.append(i)
        print(node, end='\t')
    print('\n')


def DFS(start, graph):
    stack = []
    visit = []
    stack.append(start)
    visit.append(start)
    while stack:
        node = stack.pop()
        nodes = graph[node]
        for i in nodes:
            if i not in visit:
                stack.append(i)
                visit.append(i)
        print(node, end='\t')
    print('\n')


BFS('A', graph)

DFS('A', graph)
