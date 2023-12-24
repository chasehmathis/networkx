r"""Function for computing the moral graph of a directed graph."""

import itertools

import networkx as nx
from networkx.utils import not_implemented_for

__all__ = ["find_all_treks", "combine_paths"]


@not_implemented_for("undirected")
@nx._dispatch
# def treks(G, A, B):
#     r"""Return the Moral Graph

#     Returns Treks of a given directed graph.

#     Parameters
#     ----------
#     G : NetworkX graph
#         Directed graph
#     A : Node1
#     B : Node2

#     Returns
#     -------
#     H : Set of treks from A to B

#     Raises
#     ------
#     NetworkXNotImplemented
#         If `G` is undirected.

#     Examples
#     --------
#     >>> G = nx.DiGraph([(1, 2), (2, 3), (2, 5), (3, 4), (4, 3)])
#     >>> G_moral = nx.moral_graph(G)
#     >>> G_moral.edges()
#     EdgeView([(1, 2), (2, 3), (2, 5), (2, 4), (3, 4)])

#     Notes
#     -----
#     A moral graph is an undirected graph H = (V, E) generated from a
#     directed Graph, where if a node has more than one parent node, edges
#     between these parent nodes are inserted and all directed edges become
#     undirected.

#     https://en.wikipedia.org/wiki/Moral_graph

#     References
#     ----------
#     .. [1] Wray L. Buntine. 1995. Chain graphs for learning.
#            In Proceedings of the Eleventh conference on Uncertainty
#            in artificial intelligence (UAI'95)
#     """

#     H = set()

#     for node in G.nodes:
#         source = node
#         left_path = tuple(nx.all_simple_edge_paths(G, source, A))
#         right_path = tuple(nx.all_simple_edge_paths(G, source, B))
#         print(left_path)
#         H.add((left_path, right_path))

#     # H = G.to_undirected()
#     # for preds in G.pred.values():
#     #     predecessors_combinations = itertools.combinations(preds, r=2)
#     #     H.add_edges_from(predecessors_combinations)
#     return H








@not_implemented_for("undirected")
def find_all_treks(graph, target1, target2):
    def combine_paths(path1, path2):
        """Combines two paths with a shared source into one path with the source in the middle."""
        # Reverse the first path and remove the last element (shared source)
        path1_reversed = path1[::-1][:-1]
        # Combine the paths with the shared source in the middle
        combined_path = path1_reversed + [path1[0]] + path2[1:]
        return combined_path
    """Finds all treks from any source to two targets in a directed graph."""
    treks = []
    paths = []
    for source in graph.nodes:
        all_paths_to_target1 = list(nx.all_simple_paths(graph, source, target1))
        all_paths_to_target2 = list(nx.all_simple_paths(graph, source, target2))

        for path1 in all_paths_to_target1:
            for path2 in all_paths_to_target2:
                path = combine_paths(path1, path2)
                paths.append(path)
                treks.append(graph.subgraph(path))
    
    return treks, paths
