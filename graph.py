# !python

from vertex import Vertex

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

class Graph:
    def __init__(self):
        """ 
        initializes a graph object with an empty dictionary.
        """
        # {
        #   "string": vertex_obj
        # }
        self.vertDict = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """

        if key not in self.vertDict.keys():
            # create new vertex and add to vertex dict
            self.vertDict[key] = Vertex(key)
            # increment number of verticles
            self.numVertices += 1
        return self.vertDict[key]

    def getVertex(self, key):
        """return the vertex if it exists"""

        return key in self.vertDict.keys()

    def addEdge(self, vertex_a: str, vertex_b: str, weight=0):
        """
        add an edge from vertex a to vertex b with a weight
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

        if vertex_a not in self.vertDict:
            vertex_a_obj = Vertex(vertex_a)

        if vertex_b not in self.vertDict:
            vertex_b_obj = Vertex(vertex_b)
            
        try:
            vertex_a_obj.addNeighbor(vertex_b_obj, weight)
        except ValueError:
            print("Error")


    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertDict.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
