

def nk_to_demds(G, path):
    """
    DemDS file format:
        `<number_of_nodes>` `<number_of_edges>`
        `<node>` `<node>` 
        `<node>` `<node>`
        ...
    """
    n = G.numberOfNodes()
    m = G.numberOfEdges()

    with open(path, "w") as f:
        f.write(f"{n} {m}\n")

        for u, v in G.iterEdges():
            f.write(f"{u + 1} {v + 1}\n")



def nk_to_numds(G, path):
    """
    NuMDS file format:
        p edge `<number_of_nodes>` `<number_of_edges>`
        e `<node>` `<node>` 
        e `<node>` `<node>`
        ...
    """

    n = G.numberOfNodes()
    m = G.numberOfEdges()

    with open(path, "w") as f:
        f.write(f"p edge {n} {m}\n")

        for u, v in G.iterEdges():
            f.write(f"e {u + 1} {v + 1}\n")