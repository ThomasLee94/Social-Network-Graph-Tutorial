# !python

# essential facts and functionalities of graphs 

from vertex import Vertex
from queue import LinkedQueue

class Graph(object):
    def __init__(self):
        """ 
            Initialises a graph object with an empty dictionary.
        """

        # vert_dict:
        # "key" -> "John"
        # {
        #   "key": vertex_obj
        # }

        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, key: str) -> object:
        """
            Add a new vertex object to the graph with
            the given key and return the vertex
        """

        if key not in self.vert_dict.keys():
            # create new vertex and add to vertex dict
            self.vert_dict[key] = Vertex(key)
            # increment number of verticles
            self.num_vertices += 1
        return self.vert_dict[key]

    def get_vertex(self, key: str):
        """return the vertex if it exists"""

        return key in self.vert_dict.keys()

    def add_edge(self, vertex_a: str, vertex_b: str, weight=0):
        """
            Add an edge from vertex a to vertex b with a weight

            Args:
                vertex_a: the "from" vertex, starting point of edge
                vertex_b: the "to" vertex, end point of edge
                weight: value of edge
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
        return vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        

    def get_vertices(self):
        """
            Return all the vertices in the graph
        """
        return self.vert_dict.keys()
    
    def breadth_first_search_level(self, n: int, vertex_key: str)->[str]:

        """
            Find all neighbours from a starting vertex at breadth level n

            Args:
                n: the degrees of seperation from vertex vertex_key  
                vertex_key: single str, first iteration of recursive call stack. 
                            Treat as root node, will only be inputted once.
            Returns:
                all nodes at level n starting at vertex_key as root.  
        """

        if n < 1:
            return [vertex_key]

        # check if vertex exists in graph
        if vertex_key not in self.vert_dict:
            raise ValueError("This vertex is not in graph!")

        # Queue to keep track of verticies
        # Tail is front of queue
        queue = LinkedQueue()

        # keeping track of visits
        visited = set()

        # keeping track of distance between child and parent verticies
        distance = {
            vertex_key: 0
        }
        
        queue.enqueue(vertex_key)
        visited.add(vertex_key)

        while not queue.is_empty():
            # Dequeue front vertex
            vertex = queue.dequeue()

            for neighbour in self.vert_dict[vertex].neighbours:
                if neighbour.id not in visited:
                    # adding str's, not objects
                    queue.enqueue(neighbour.id)
                    visited.add(neighbour.id)
                    # adding distance
                    distance[neighbour.id] = 1 + distance[vertex]
                    
        # returned a filtered list from distance dict of values == n
        func = lambda vertex_key: distance[vertex_key] == n 
        start_list = distance.keys()
        return list(filter(func, start_list))  

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


# Driver code


if __name__ == "__main__":
    g = Graph()

    # Add verticies
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")

    # Add edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("C", "D")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "E")

    output = g.breadth_first_search_level(n=2,vertex_key="A")
    print(output)
