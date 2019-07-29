from classes.util.read_file import graph_from_file
from classes.graph import Graph, fill
from classes.digraph import Digraph
import argparse

def chapter_1(filename: str) -> Graph:
    """ 
        Builds graph according to data text file 
        and returns graph to be manipulated
    """
    graph, verticies, edges_str = graph_from_file(filename)

     # fill graph instance with edges and verticies
    return fill(graph, verticies, edges_str)

def chapter_2(filename: str, vertex_a: str):
    """ 
        Returns neighbours of given vertex_a graph as a list
        of strings.
    """

    # build graph
    graph = chapter_1(filename)

    # return neighbours as a list of strings
    keys_obj = graph.vert_dict[vertex_a].adj_dict_neighbours.keys()
    keys_str = map(keys_obj, key = lambda vertex: vertex.id)
    return keys_str

def chapter_3(filename: str, vertex_a: str, n: int):
    """
        Returns the neighbours at level n from vertex_a 
    """

    # build graph
    graph = chapter_1(filename)

    return graph.breadth_first_search_level(vertex_a, n)

def chapter_4(filename: str, vertex_a: str, vertex_b: str, visited_list: [str], visited_set):
    """
        Executes a depth first search to find a path
        from vertex_a to vertex_b 
    """

    # build graph
    graph = chapter_1(filename)

    output_list = graph.find_path(vertex_a, vertex_b, visited_list, visited_set)

    return output_list

def chapter_5(filename: str, vertex_a: str, vertex_b: str):
    """
        Executes a breadth first search to find the shortest
        path between veretex_a and vertex_b. 
    """
    # build graph
    graph = chapter_1(filename)

    # get dict
    dict_ = graph.find_shortest_path(vertex_a, vertex_b)

    parent = dict_[vertex_b]
    output = list()

    # append vertex_b
    output.append(vertex_b)

    # walking backwards in "parent" dict
    while parent != vertex_a:
        output.append(parent)
        parent = dict_[parent]
    
    # prepending vertex_a
    output.append(vertex_a)
    output = output[::-1]

    print(f"Vertices in shortest path: {output}")
    print(f"Number of edges in shortest path: {len(output)-1}")

def chapter_6(filename: str)-> set:
    # build graph
    graph = chapter_1(filename)

    output_set = graph.clique

    print(f"verticies in maximal clique: {output_set}")
    return output_set
    
# CHAPTER 1
# chapter_1("graph_data.txt")

# CHAPTER 2
# chapter_2("graph_data.txt", "A")

# CHAPTER 3
# chapter_3("graph_data.txt", "A", 3)

# CHAPTER 4
# visited_list = list()
# visited_set = set()
# chapter_4("graph_data.txt", "A", "C", visited_list, visited_set)

# CHAPTER 5
# chapter_5("graph_data.txt", "A", "D")

# CHAPTER 6
chapter_6("graph_data.txt")
