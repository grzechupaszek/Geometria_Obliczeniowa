import matplotlib.pyplot as plt
from geometry.mesh import Mesh


def plot_mesh(mesh: Mesh):
    # Rysujemy wszystkie węzły
    x_coords = [node.x for node in mesh.nodes.values()]
    y_coords = [node.y for node in mesh.nodes.values()]
    plt.scatter(x_coords, y_coords, color='blue', marker='o', label='Nodes')

    # Rysujemy elementy
    for element in mesh.elements.values():
        node_ids = element.node_ids

        # Jeśli element to linia (2 węzły)
        if len(node_ids) == 2:
            x1, y1 = mesh.get_node_coordinates(node_ids[0])
            x2, y2 = mesh.get_node_coordinates(node_ids[1])
            plt.plot([x1, x2], [y1, y2], color='black')
        # Jeśli element to wielokąt (3 lub więcej węzłów)
        elif len(node_ids) >= 3:
            # Pobieramy współrzędne węzłów według kolejności z pliku
            coords = [mesh.get_node_coordinates(nid) for nid in node_ids]
            # Dodajemy pierwszy punkt na koniec, by domknąć kształt
            coords.append(coords[0])
            plt.plot([p[0] for p in coords], [p[1] for p in coords], color='black')

    plt.legend()
    plt.title("Mesh Visualization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')
    plt.show()
