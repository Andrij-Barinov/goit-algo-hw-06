import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    
    stations = ["Station1", "Station2", "Station3", "Station4", "Station5"]
    G.add_nodes_from(stations)
    
    edges = [
        ("Station1", "Station2"),
        ("Station2", "Station3"),
        ("Station3", "Station4"),
        ("Station4", "Station5"),
        ("Station5", "Station1"),
        ("Station1", "Station3"),
        ("Station2", "Station4")
    ]
    G.add_edges_from(edges)
    
    return G

def analyze_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())
    
    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print("Ступінь кожної вершини:")
    for node, degree in degrees.items():
        print(f"{node}: {degree}")

def visualize_graph(G):
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    plt.title("Транспортна система міста")
    plt.show()

if __name__ == "__main__":
    G = create_graph()
    analyze_graph(G)
    visualize_graph(G)
