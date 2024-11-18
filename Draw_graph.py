import matplotlib.pyplot as plt
import networkx as nx

# Создание графа
G = nx.DiGraph()

# Добавление узлов класса и их методов
G.add_node("Laba4")
G.add_node("__init__(number)")
G.add_node("set_number(number)")
G.add_node("get_str_ending()")
G.add_node("add_time()")
G.add_node("number")


G.add_edges_from([
    ("Laba4", "__init__(number)"),
    ("__init__(number)", "set_number(number)"),
    ("set_number(number)", "number"),
    ("number", "get_str_ending()"),
    ("number", "add_time()"),
    ("get_str_ending()", "add_time()"),
])

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_color="black", arrows=True)
plt.title("Граф класса Laba4")
plt.show()