import networkx as nx
import matplotlib.pyplot as plt
from graph_creation import create_graph

def add_weights(G):
    weighted_edges = [
        ("Station1", "Station2", 7),
        ("Station2", "Station3", 10),
        ("Station3", "Station4", 5),
        ("Station4", "Station5", 3),
        ("Station5", "Station1", 8),
        ("Station1", "Station3", 4),
        ("Station2", "Station4", 6)
    ]
    G.add_weighted_edges_from(weighted_edges)
    return G

def dijkstra_shortest_path(G, source, target):
    shortest_path = nx.dijkstra_path(G, source=source, target=target)
    shortest_path_length = nx.dijkstra_path_length(G, source=source, target=target)
    return shortest_path, shortest_path_length

def visualize_shortest_path(G, shortest_path):
    path_edges = list(zip(shortest_path, shortest_path[1:]))
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.title("Найкоротший шлях за алгоритмом Дейкстри")
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    G = add_weights(G)
    
    source = "Station1"
    target = "Station4"
    
    shortest_path, shortest_path_length = dijkstra_shortest_path(G, source, target)
    
    print(f"Найкоротший шлях за алгоритмом Дейкстри: {shortest_path}")
    print(f"Довжина найкоротшого шляху: {shortest_path_length}")
    
    visualize_shortest_path(G, shortest_path)
