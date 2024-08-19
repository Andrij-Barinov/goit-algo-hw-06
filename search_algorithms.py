import networkx as nx
from graph_creation import create_graph

def dfs_search(G, start_node):
    dfs_edges = list(nx.dfs_edges(G, source=start_node))
    dfs_path = [edge[1] for edge in dfs_edges]
    dfs_path.insert(0, start_node)
    return dfs_path

def bfs_search(G, start_node):
    bfs_edges = list(nx.bfs_edges(G, source=start_node))
    bfs_path = [edge[1] for edge in bfs_edges]
    bfs_path.insert(0, start_node)
    return bfs_path

if __name__ == "__main__":
    G = create_graph()
    
    start_node = "Station1"
    
    dfs_path = dfs_search(G, start_node)
    bfs_path = bfs_search(G, start_node)
    
    print(f"DFS шлях: {dfs_path}")
    print(f"BFS шлях: {bfs_path}")
    
    # Порівняння шляхів
    print(f"Шлях DFS: {dfs_path}")
    print(f"Шлях BFS: {bfs_path}")
