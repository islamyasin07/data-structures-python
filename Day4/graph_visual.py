import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edge("Ali", "Library")
G.add_edge("Sara", "Cafeteria")
G.add_edge("Library", "Study Room")

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=14, arrows=True)
plt.title("Student Movement Graph (Example)")
plt.show()
