# Consider the following algorithm. The input is a connected undirected graph with edge costs (distinct, if you prefer). The algorithm operates in phases, where each phase involves adding edges to a tree constructed so far and decreasing the count of vertices in the graph (when only 1 vertex remains, the Minimum Spanning Tree is essentially an empty set). Within a phase, we identify the least expensive edge ev incident on each vertex v in the current graph. Let F = {ev} be the collection of all such edges for the present phase. We create a new (smaller) graph by contracting all the edges in F — this causes each connected component of F to become a single vertex in the new graph, while any resulting self-loops are discarded. Let T represent the accumulation of all edges that are contracted in any phase of this algorithm. Is T assured to be a Minimum-Cost Spanning Tree? Offer a proof or demonstrate a counterexample.
