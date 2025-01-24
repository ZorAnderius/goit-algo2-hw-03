import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph (capacity_matrix: list, flow_matrix: list) -> None:
    G = nx.DiGraph()
    num_nodes = len(capacity_matrix)

    for u in range(num_nodes):
        for v in range(num_nodes):
            if capacity_matrix[u][v] > 0:
                G.add_edge(u, v, capacity=capacity_matrix[u][v], flow=flow_matrix[u][v])

    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold',
            arrowsize=20)
    labels = {(u, v): f"{data['flow']}/{data['capacity']}" for u, v, data in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()