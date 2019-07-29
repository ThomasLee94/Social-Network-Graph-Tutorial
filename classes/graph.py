from classes.vertex import Vertex
from classes.queue import LinkedQueue
import classes.util.read_file as read_data
import heapq as pqueue
import random

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
        self.num_edges = 0

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
        vertex_a_obj.add_neighbor(vertex_b_obj, weight)
        vertex_b_obj.add_neighbor(vertex_a_obj, weight)
        
    def get_vertices(self):
        """
            Return all the vertices in the graph
        """
        return self.vert_dict.keys()
    
    def breadth_first_search_level(self, vertex_key: str, n: int)->[str]:

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
    
    def find_path(self, vertex_a: str, vertex_b: str, visited_list: [str], visited_set)->[str]:
        """
            Executes a depth first search on the given graph.
            Args
                vertex_a: start vertex
                vertex_b: to vertex
                visited_list: keeps track of visited verticies in order of traversal
                visited: set method to keep track of visited verticies.
            Returns
                If vertex_b is in any branch from vertex_a: return (True, verticies_list)
                If vertex_b not in any branch from vertex_a: return (False, verticies_list) 
        """

        # Catch all
        if vertex_a not in self.vert_dict:
            raise ValueError("This vertex is not in graph!")
        if vertex_b not in self.vert_dict:
            raise ValueError("This vertex is not in graph!")

        if vertex_a in self.vert_dict and vertex_a not in visited_set:
            # Add vertex_a to set
            visited_set.add(vertex_a)
            # add vertex to visited list in order
            visited_list.append(vertex_a)
            # if vertex_b is found
            if vertex_a == vertex_b:
                return visited_list 
            # add neighbours of vertex_a in stack
            for neighbour in self.vert_dict[vertex_a].adj_dict_neighbours:
                # visit neighbours recursively
                return self.find_path(neighbour.id, vertex_b, visited_list, visited_set)
        
        
    def find_shortest_path(self, vertex_a: str, vertex_b: str)-> object:

        """
            Executes a breadth for search on the given graph. 

            Args:
                vertex_a: from vertex.
                vertex_b: to vertex.
            Returns:
                a dict of containing parent and child verticies.
        """

        # Check if verticies exists in graph
        if vertex_a not in self.vert_dict:
            if vertex_b not in self.vert_dict:
                raise ValueError("This vertex is not in graph!")

        # Queue to keep track of verticies, enqueue vertex_a
        queue = LinkedQueue(vertex_a)

        # Keeping track of visits
        visited = set()
        # add vertex_a to set
        visited.add(vertex_a)

        # create dict to store parent and children verticies
        # parent = {
        #   child_vertex: parent_vertex
        # }
        child_parent_path = dict()
        
        # Iterating through queue
        while not queue.is_empty():
            # Dequeue front vertex
            vertex = queue.dequeue()
            
            # sorting keys in adjacency list to evaluate vertex.id
            keys = self.vert_dict[vertex].adj_dict_neighbours.keys()
            sorted_keys = sorted(keys, key = lambda vertex: vertex.id)
            # looping through neighbours
            for neighbour in sorted_keys:
                if neighbour.id not in visited:
                    # adding str's, not objects
                    queue.enqueue(neighbour.id)
                    visited.add(neighbour.id)
                    # creating key-value pair in parent dict
                    child_parent_path[neighbour.id] = vertex
                    
        return child_parent_path
    
    def clique(self):
        """
            This class method finds a single clique in the graph. 
        """

        # init set
        clique = set()

        # start with first vertex
        vertex = list(self.vert_dict.keys())[0]
        clique.add(vertex)

        for vertex_ in self.vert_dict:
            # check if vertex is not already in clique set
            if vertex_ not in clique:
                # using helper function
                if self.is_neighbour_of_all(vertex_, clique):
                    # add vertex_clique to clique if it is a neighbour to all verticies in set
                    print("added vertex to set")
                    clique.add(vertex_)
        return clique
    
    def is_neighbour_of_all(self, vertex_a: str, clique_set: (str))->bool:
        """
            Helper function for clique 
        """

        for vertex in clique_set:
            # comparing objects
            if self.vert_dict[vertex_a] not in self.vert_dict[vertex].neighbours:
                return False
        return True

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())

def fill(graph: Graph, verticies: [str], edges_and_weight: [str]) -> Graph:
    """
        Fills graph based on input verticies and edges and optional weights 
    """

    # creating edge_list iterable 
    edge_list = list()
    for edge in edges_and_weight:
        edge_list.append(read_data.string_to_tuple(edge))

    # add verticies
    for vertex in verticies:
        graph.add_vertex(vertex)
    
    # add edges and weights
    for tuple_ in edge_list:
        # if weight was not given, default to 0 
        if len(tuple_) == 2:
            graph.add_edge(tuple_[0], tuple_[1], 0)
        else:
            graph.add_edge(tuple_[0], tuple_[1], tuple_[2])
    
    return graph