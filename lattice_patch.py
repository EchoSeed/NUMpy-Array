
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def build_lattice_graph(glyph_log):
    G = nx.Graph()
    for glyph in glyph_log:
        gid = glyph["id"]
        G.add_node(gid, entropy=glyph.get("entropy", 0), tags=glyph.get("tags", []))
        for link in glyph.get("links", []):
            G.add_edge(gid, link)
    return G

def get_entropy_array(G):
    entropies = np.array([G.nodes[n].get("entropy", 0) for n in G.nodes])
    if len(entropies) == 0:
        return np.ones(len(G.nodes))
    entropies = np.clip(entropies, 0, None)
    norm = entropies / (np.max(entropies) or 1.0)
    return norm * 300

def render_lattice(G):
    pos = nx.spring_layout(G, seed=42)
    node_sizes = get_entropy_array(G)
    node_colors = ["#00bfff" if "origin" in G.nodes[n].get("tags", []) else "#cccccc" for n in G.nodes]

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, edge_color="#888")
    plt.title("EchoSeed Symbolic Lattice")
    plt.show()
