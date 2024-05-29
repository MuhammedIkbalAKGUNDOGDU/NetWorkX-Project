import networkx as nx
import matplotlib.pyplot as plt

# Boş bir grafik oluşturun
G = nx.Graph()

# Düğümleri (İstanbul'daki bazı önemli noktalar) ekleyin
nodes = [
    "Taksim Meydanı", "Sultanahmet", "Beşiktaş", 
    "Kadıköy", "Üsküdar", "Levent", 
    "Maslak", "Kartal", "Maltepe", 
    "Ataşehir", "Şişli"
]

G.add_nodes_from(nodes)

# Kenarları (bu noktalar arasındaki yollar) ekleyin
edges = [
    ("Taksim Meydanı", "Beşiktaş"),
    ("Taksim Meydanı", "Sultanahmet"),
    ("Beşiktaş", "Levent"),
    ("Beşiktaş", "Üsküdar"),
    ("Kadıköy", "Üsküdar"),
    ("Kadıköy", "Ataşehir"),
    ("Kadıköy", "Maltepe"),
    ("Üsküdar", "Levent"),
    ("Levent", "Maslak"),
    ("Maslak", "Şişli"),
    ("Kartal", "Maltepe"),
    ("Maltepe", "Ataşehir"),
    ("Ataşehir", "Şişli"),
]

G.add_edges_from(edges)

# Grafiği çizdirin
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Düğümleri düzenlemek için bir düzenleyici kullanın
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("İstanbul Şehri Graph")
plt.show()
