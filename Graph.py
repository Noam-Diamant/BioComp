import itertools

class Edge(object):
    """Edge class for graph implementation"""
    def __init__(self, src, dst):
        self._src = src
        self._dst = dst

    def __str__(self):
        return f"{self._src} {self._dst}"

    def __eq__(self, other):
        return (self._src, self._dst) == (other.get_source(), other.get_target())

    def __hash__(self):
        return hash((self._src, self._dst))

    def get_source(self):
        return self._src

    def get_target(self):
        return self._dst


# Graph class for each of our sub-graphs :)
class Graph(object):
    """Graph implementation using lists"""
    def __init__(self, edges=None, size=None):
        # Initialize empty graph
        self._edge_list = []
        self._node_list = []
        
        # Handle initialization cases
        if size is not None and edges is None:
            self._node_list = self._create_nodes(size)
        elif edges is not None and size is not None:
            self._node_list = self._create_nodes(size)
            for e in edges:
                self.add_edge(Edge(e[0], e[1]))

    def _create_nodes(self, size):
        return [n for n in range(1, size + 1)]

    def __str__(self):
        if not self._edge_list:
            return ""  # Return empty string for empty graph
        edges_str = ''.join(str(e) + '\n' for e in sorted(self._edge_list, 
                        key=lambda e: (e.get_source(), e.get_target())))
        return edges_str.rstrip('\n')

    def __eq__(self, other):
        if not (len(self._node_list) == len(other.get_nodes()) and 
                len(self._edge_list) == len(other.get_edges())):
            return False

        for perm in other.permute_graph():
            if (all(n in perm.get_nodes() for n in self._node_list) and 
                all(e in perm.get_edges() for e in self._edge_list)):
                return True
        return False

    def add_node(self, node):
        if node not in self._node_list:
            self._node_list.append(node)

    def add_edge(self, edge):
        if (edge not in self._edge_list and 
            edge.get_target() in self._node_list and 
            edge.get_source() in self._node_list):
            self._edge_list.append(edge)

    def get_nodes(self):
        return self._node_list

    def get_edges(self):
        return self._edge_list

    def _dfs_visit(self, node, visited):
        visited[node - 1] = True
        for edge in self._edge_list:
            if edge.get_source() == node and not visited[edge.get_target() - 1]:
                self._dfs_visit(edge.get_target(), visited)
            elif edge.get_target() == node and not visited[edge.get_source() - 1]:
                self._dfs_visit(edge.get_source(), visited)

    def is_connected(self):
        if not self._node_list:
            return True
        visited = [False] * len(self._node_list)
        self._dfs_visit(self._node_list[0], visited)
        return all(visited)

    def permute_graph(self):
        import itertools
        result = []
        for p in itertools.permutations(self._node_list):
            g = Graph()
            g._node_list = list(p)
            for edge in self._edge_list:
                src_idx = edge.get_source() - 1
                dst_idx = edge.get_target() - 1
                g.add_edge(Edge(p[src_idx], p[dst_idx]))
            result.append(g)
        return result