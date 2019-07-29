#!python
 
# Vertex Class
    # A helper class for the Graph class that defines vertices and vertex neighbors.

class Vertex:

    def __init__(self, vertex: str):
        """
        initialize a vertex and its neighbors.

        neighbors: set of vertices adjacent to self, 
        stored in a dictionary with vertex_obj-weight 
        as a key-value pair.
        """

        # neighbours:
        # {
        #   vertex_obj: weight
        # }

        self.id = vertex
        self.neighbours = {}

    def add_neighbor(self, vertex: object, weight=0):
        """add a neighbor along a weighted edge"""

        if vertex not in self.neighbours.keys():
            # if vertex does not exist, create new key-value pair
            self.neighbours[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbours])

    def get_neighbors(self) -> [object]:
        """returns all vertices (nodes) connected to this vertex (node)"""

        return self.neighbours.keys()

    def get_id(self) -> object:
        """return the id of this vertex"""

        return self.id

    def get_edge_weight(self, vertex: object) -> int:
        """return the weight of this edge"""
        
        return self.neighbours[vertex]