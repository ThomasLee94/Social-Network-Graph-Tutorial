#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """

        # {
        #   vertex_obj: weight
        # }

        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex: object, weight=0):
        """add a neighbor along a weighted edge"""
        # TODO check if vertex is already a neighbor
        # TODO if not, add vertex to neighbors and assign weight.

        if vertex not in self.neighbors.keys():
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        # TODO return the neighbors

        return self.neighbors.keys()

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex: object):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this
        
        return self.neighbors[vertex]