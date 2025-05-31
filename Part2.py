from math import factorial
import itertools
from Graph import Graph, Edge
from Part1 import get_unique_graphs


def count_motif_appearances(graph: Graph, motif: Graph) -> int:
    """
    Count how many times motif appears in the graph
    Args:
        graph: The full graph to search in
        motif: The subgraph to look for
    Returns:
        Number of appearances of motif in graph
    """
    appearances = 0
    for perm in graph.permute_graph():
        if all(edge in perm.get_edges() for edge in motif.get_edges()):
            appearances += 1
            
    # Divide by the number of ways to arrange the remaining nodes
    remaining_nodes = len(graph.get_nodes()) - len(motif.get_nodes())
    return appearances // factorial(remaining_nodes)


def find_all_motifs(graph: Graph, motif_size: int) -> list:
    """
    Find all motifs of given size in the graph and count their appearances
    Args:
        graph: The graph to search in
        motif_size: Size of motifs to find
    Returns:
        List of tuples (motif, count) for each possible motif
    """
    # Get all possible motifs of the given size
    possible_motifs = get_unique_graphs(motif_size)
    
    # If graph is smaller than motif size, no motifs can exist
    if len(graph.get_nodes()) < motif_size:
        return [(motif, 0) for motif in possible_motifs]
    
    # Count appearances of each motif
    motif_counts = []
    for motif in possible_motifs:
        count = count_motif_appearances(graph, motif)
        motif_counts.append((motif, count))
    
    return motif_counts


def display_motifs(motifs: list, size: int) -> None:
    """
    Formats and prints the results of motif analysis in the graph.
    Displays each motif's frequency of appearance along with its structure.
    
    Args:
        motifs: List of tuples where each tuple contains (motif_graph, appearance_count)
        size: Number of vertices in each motif
    """
    print(f"Motif size = {size}")
    print(f"Motifs count = {len(motifs)}")
    
    for idx, (motif, count) in enumerate(motifs, 1):
        print(f"#{idx}")
        print(f"count={count}")
        if str(motif):  # If motif has edges
            print(motif)


def read_input_graph() -> tuple[Graph, int]:
    """
    Read graph from input in the format:
    1 2
    2 3
    1 4
    And read motif size n
    Returns:
        Tuple of (graph, motif_size)
    """
    # Read motif size
    n = int(input().strip())
    
    # Read edges until empty line or EOF
    edges = []
    nodes = set()
    try:
        while True:
            line = input().strip()
            if not line:
                break
            src, dst = map(int, line.split())
            edges.append((src, dst))
            nodes.add(src)
            nodes.add(dst)
    except EOFError:
        pass
    
    # Create graph
    graph = Graph()
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(Edge(*edge))
    
    return graph, n


def main():
    # Read input
    graph, motif_size = read_input_graph()
    
    # Find and display motifs
    if motif_size >= 1:
        motifs = find_all_motifs(graph, motif_size)
        display_motifs(motifs, motif_size)
    else:
        print("Invalid size - must be 1 or greater")


if __name__ == '__main__':
    main()