import networkit as nk

from src.config import GRAPH_SEED

def characterize_graph(G: nk.Graph):
    n = G.numberOfNodes()
    m = G.numberOfEdges()

    cc = nk.components.ConnectedComponents(G)
    cc.run()

    component_sizes = cc.getComponentSizes()

    largest_component = max(component_sizes.values())

    isolates = sum(
        1
        for u in G.iterNodes()
        if G.degree(u) == 0
    )

    return {
        "nodes": n,
        "edges": m,
        "avg_degree": 2 * m / n,
        "components": len(component_sizes),
        "largest_component": largest_component,
        "lcc_fraction": largest_component / n,
        "isolates": isolates,
        "isolates_fraction": isolates / n,
        "max_degree": max(G.degree(u) for u in G.iterNodes()),
    }

def graph_seed(n, beta, repetition):
    """
    Generates different seed for graph generation, based on number of nodes, beta and repetition
    """
    return (
        GRAPH_SEED
        + n
        + int(beta * 1000)
        + repetition * 1_000_000
    )