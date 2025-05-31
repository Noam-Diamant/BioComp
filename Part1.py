import itertools
import time
from Graph import Graph, Edge


def get_edge_combinations(n, k):
    """Get all possible k-sized edge combinations for n nodes"""
    vertex_pairs = list(itertools.permutations(range(1, n + 1), 2))
    return list(itertools.combinations(vertex_pairs, k))


def run_dfs(start_node, edge_list, mark_visited):
    """Run DFS from start_node"""
    mark_visited[start_node - 1] = True
    for e in edge_list:
        src, dst = e[0], e[1]
        if src == start_node and not mark_visited[dst - 1]:
            run_dfs(dst, edge_list, mark_visited)
        elif dst == start_node and not mark_visited[src - 1]:
            run_dfs(src, edge_list, mark_visited)


def check_connectivity(edge_list, vertex_count):
    """Check if graph is connected"""
    mark_visited = [False] * vertex_count
    run_dfs(1, edge_list, mark_visited)
    return all(mark_visited)


def get_edge_count_range(vertex_count):
    """Get min and max possible edges for connected graph"""
    return (vertex_count - 1,  # Tree
            vertex_count * (vertex_count - 1))  # Complete directed


def get_all_connected_graphs(vertex_count):
    """Get all possible connected graphs"""
    result = {}
    min_e, max_e = get_edge_count_range(vertex_count)
    
    for e_count in range(min_e, max_e + 1):
        all_combinations = get_edge_combinations(vertex_count, e_count)
        connected = [edges for edges in all_combinations 
                    if check_connectivity(edges, vertex_count)]
        result[e_count] = connected
    
    return result


def get_edge_permutations(edge_list, vertex_count):
    """Get all edge permutations"""
    result = []
    vertices = list(range(1, vertex_count + 1))
    
    for vertex_perm in itertools.permutations(vertices):
        new_edges = []
        for edge in edge_list:
            src_idx = edge[0] - 1
            dst_idx = edge[1] - 1
            new_edges.append((vertex_perm[src_idx], vertex_perm[dst_idx]))
        result.append(new_edges)
    
    return result


def get_unique_graphs(vertex_count):
    """Get all unique non-isomorphic connected graphs"""
    if vertex_count < 1:
        print("Invalid size - must 1 or greater")
        return None

    all_connected = get_all_connected_graphs(vertex_count)
    min_e, max_e = get_edge_count_range(vertex_count)
    result = []

    for e_count in range(min_e, max_e + 1):
        edge_sets = all_connected[e_count]
        
        if not edge_sets:
            continue
            
        if len(edge_sets) == 1:
            result.append(Graph(edges=edge_sets[0], size=vertex_count))
            continue

        unique_edge_sets = []
        for edges in edge_sets:
            if not any(set(perm) in unique_edge_sets 
                      for perm in get_edge_permutations(edges, vertex_count)):
                unique_edge_sets.append(set(edges))

        for edges in unique_edge_sets:
            result.append(Graph(edges=list(edges), size=vertex_count))

    return result


def display_graphs(graph_list, size, output_path=None):
    """Display all graphs"""
    output = []
    output.append(f"n={size}")
    output.append(f"count={len(graph_list)}")
    
    for i, g in enumerate(graph_list, 1):
        output.append(f"#{i}")
        graph_str = str(g)
        if graph_str:  # If graph is not empty
            output.append(graph_str)
    
    text = '\n'.join(output) + '\n'
    print(text, end='')
    
    if output_path:
        with open(output_path, 'a') as f:
            f.write(text)


def main():
    output_file = "./graphs.txt"
    timings = []
    
    for n in range(1, 6):
        t_start = time.time()
        graphs = get_unique_graphs(n)
        timings.append(float("{:.5f}".format(time.time() - t_start)))
        display_graphs(graphs, n, output_file)
        with open(output_file, "a") as f:
            f.write(f"Execution time: {timings[-1]} seconds\n")


if __name__ == '__main__':
    main()