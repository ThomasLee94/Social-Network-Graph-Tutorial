# !python

# essential facts and functionalities of graphs 

from classes.graph import Graph

class Digraph(Graph):
    """ essential facts and functionalities of a directed graph"""

    def add_edge(self, vertex_a: str, vertex_b: str, weight=0):
        """
        add an edge between both vertex a to vertex b with a weight
        """
        
        # check if vertices exist in graph
        if vertex_a not in self.vert_dict.keys():
            # raise error if vertex_a does not exist
            raise ValueError("This vertex does not exist in graph!")

        if vertex_b not in self.vert_dict.keys():
            # raise error if vertex_b does not exist
            raise ValueError("This vertex does not exist in graph!")

        vertex_a_obj = self.vert_dict[vertex_a]
        vertex_b_obj = self.vert_dict[vertex_b]

        # making vertex_b a neighbour to vertex_a by adding an edge
        vertex_a_obj.add_neighbour(vertex_b_obj, weight)
        # increment edge count
        self.num_edges +=1 
        

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()
    