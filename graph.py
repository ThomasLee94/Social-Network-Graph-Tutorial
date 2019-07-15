# !python

# essential facts and functionalities of graphs 

from vertex import Vertex

class Graph:
    def __init__(self):
        """ 
        initializes a graph object with an empty dictionary.
        """
        # {
        #   "key": vertex_obj
        # }
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, key: str):
        """
        add a new vertex object to the graph with
        the given key and return the vertex
        """

        if key not in self.vert_dict.keys():
            # create new vertex and add to vertex dict
            self.vert_dict[key] = Vertex(key)
            # increment number of verticles
            self.num_vertices += 1
        return self.vertDict[key]

    def get_vertex(self, key: str):
        """return the vertex if it exists"""

        return key in self.vert_dict.keys()

    def add_edge(self, vertex_a: str, vertex_b: str, weight=0):
        """
        add an edge from vertex a to vertex b with a weight
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

        for key in self.vert_dict.keys():
            

        if vertex_a not in self.vert_dict.keys():
            # add vertex_a if its not in graph
            vertex_a_obj = Vertex(vertex_a)

            if vertex_b not in self.vert_dict.keys():
                # add vertex_b if not in graph
                vertex_b_obj = Vertex(vertex_b)
            
                try:
                    vertex_a_obj.add_neighbor(vertex_b_obj, weight)
                except ValueError:
                    print("Error")


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()

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
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.get_id(), w.get_id()))
