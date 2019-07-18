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
    
    def breadth_first_search_level(
        self, n: int, vertex_key: str = "", vertex_keys: LinkedQueue(str) = ""
        )->[str]:

        """
            Find all neighbours from a starting vertex at breadth level n

            Args:
                n: the degrees of seperation from vertex vertex_key  
                vertex_key: single str, first iteration of recursive call stack. Treat as root node.
                vertex_keys: LinkedQueue object, a queue to keep track of neighbours.
            Returns:
                all nodes at level n starting at vertex_key as root.  
        """

        # list or dict to keep track of visited nodes
        # only decrement when we visit all nodes in [vertex_key]

        # check if vertex exists in graph
        if vertex_keys:
            for vertex_key in vertex_keys:
                if vertex_key not in self.vert_dict:
                    raise ValueError("This vertex is not in graph!")

        # output
        output = []
        
        # Queue to keep track of verticies
        queue = LinkedQueue()

        # adding nieghbours of start_vertex to queue
        for vertex_key in vertex_keys:
            temp_list = list()
            for neighbour in self.vert_dict[vertex_key].neighbours:
                queue.enqueue(neighbour)
                # setting output to all neighbours at current n level
                temp_list.append(neighbour)
                output = temp_list
            
        # decrement n, only after getting all the neighbours for 
        n -= 1

        if n < 1:
            return output
            
        vertex_keys = queue.dequeue

        return self.breadth_first_search_level(vertex_keys, n)

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

    breadth_first_search_level(vertex_key="A",n=2)
