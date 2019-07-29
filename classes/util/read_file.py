from classes.digraph import Digraph
from classes.graph import Graph
from classes.vertex import Vertex

def graph_from_file(filepath):
	""" 
		Opens a text file and returns:
			graph: graph instance
			verticies: list 
			edges: list of tuples
	"""

	with open(filepath) as f:
		lines = f.read().splitlines()
		g_type, verticies, edges = lines[0], lines[1].split(','), lines[2:]
	
		if g_type == "G":
			graph = Graph()
			return graph, verticies, edges
		elif g_type == "D":
			graph = Digraph()
			return graph, verticies, edges
		else:
			raise ValueError("Graph type is not specified!")


def string_to_tuple(string):
	"""
		turns a string into a tuple 
	"""
    # Remove front and back parenthesis:
	string = string[1:-1]

    # Split by commas:
	elements = string.split(',')

	return tuple(elements)