#!/bin/python
import sys
import os
from collections import defaultdict

'''Complete the function below to return a list of image names that
represents the order in which builds should be carried out such that
an image is always built before all of its children.'''


def serialize_build_order(relations):
    print relations
    graph = {}
    for tuples in relations:
        for item in tuples:
            if tuples not in graph:
                graph[item] = []
    indegree = {}
    for tuples in relations:
        graph[tuples[1]].append(tuples[0])
        if tuples[0] not in indegree:
            indegree[tuples[0]] = 1
        else:
            indegree[tuples[0]] += 1
    for tuples in relations:
        if tuples[1] not in indegree:
            indegree[tuples[1]] = 0
    res = []
    q = []
    external = []
    new_indegree = defaultdict(int)
    for node, val in indegree.items():
        if val == 0:
            external.append(node)
            for neighbors in graph[node]:
                indegree[neighbors] -= 1
                new_indegree[neighbors] = indegree[neighbors]
        else:
            if node not in new_indegree:
                new_indegree[node] = val

    for node in new_indegree:
        if node not in external:
            if new_indegree[node] == 0:
                q.append(node)
    while q:
        z = q.pop()
        res.append(z)
        for nb in graph[z]:
            new_indegree[nb] -= 1
            if indegree[nb] == 0:
                q.append(nb)
    return res


serialize_build_order([('master','ubuntu'),('numpy','master'),('tensorflow','numpy')])