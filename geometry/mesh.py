from geometry.node import Node
from geometry.element import Element

class Mesh:
    def __init__(self):
        # Przechowujemy węzły i elementy w słownikach:
        self.nodes: dict[int, Node] = {}
        self.elements: dict[int, Element] = {}

    def add_node(self, node_id: int, x: float, y: float):
        """Dodaj nowy węzeł do siatki."""
        if node_id in self.nodes:
            raise ValueError(f"Node with ID {node_id} already exists.")
        self.nodes[node_id] = Node(node_id, x, y)

    def add_element(self, element_id: int, node_ids: list[int]):
        """Dodaj nowy element do siatki."""
        if element_id in self.elements:
            raise ValueError(f"Element with ID {element_id} already exists.")

        # Upewnij się, że wszystkie węzły istnieją:
        for nid in node_ids:
            if nid not in self.nodes:
                raise ValueError(f"Node with ID {nid} does not exist in the mesh.")

        self.elements[element_id] = Element(element_id, node_ids)

    def get_node_coordinates(self, node_id: int):
        """Zwraca współrzędne (x, y) wybranego węzła."""
        node = self.nodes.get(node_id)
        if not node:
            raise ValueError(f"Node with ID {node_id} not found.")
        return (node.x, node.y)

    def compute_element_length(self, element_id: int) -> float:
        """Jeśli element to odcinek (2 węzły), oblicz długość."""
        element = self.elements.get(element_id)
        if not element:
            raise ValueError(f"Element with ID {element_id} not found.")

        if len(element.node_ids) != 2:
            raise ValueError("Element is not a 2-node line.")

        x1, y1 = self.get_node_coordinates(element.node_ids[0])
        x2, y2 = self.get_node_coordinates(element.node_ids[1])

        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return length

    def compute_element_area(self, element_id: int) -> float:
        """Jeśli element to trójkąt (3 węzły), oblicz jego pole."""
        element = self.elements.get(element_id)
        if not element:
            raise ValueError(f"Element with ID {element_id} not found.")

        if len(element.node_ids) != 3:
            raise ValueError("Element is not a 3-node triangle.")

        x1, y1 = self.get_node_coordinates(element.node_ids[0])
        x2, y2 = self.get_node_coordinates(element.node_ids[1])
        x3, y3 = self.get_node_coordinates(element.node_ids[2])

        # Pole trójkąta wzorem determinanty:
        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        return area

    def load_from_file(self, file_path: str):
        """Wczytuje węzły i elementy z pliku tekstowego o prostej strukturze."""
        with open(file_path, 'r') as f:
            mode = None  # 'NODES' lub 'ELEMENTS'
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    # Sprawdzamy, czy linia to # NODES lub # ELEMENTS
                    if line.upper().startswith('# NODES'):
                        mode = 'NODES'
                    elif line.upper().startswith('# ELEMENTS'):
                        mode = 'ELEMENTS'
                    continue

                if mode == 'NODES':
                    parts = line.split()
                    node_id = int(parts[0])
                    x = float(parts[1])
                    y = float(parts[2])
                    self.add_node(node_id, x, y)

                elif mode == 'ELEMENTS':
                    parts = line.split()
                    elem_id = int(parts[0])
                    node_ids = list(map(int, parts[1:]))
                    self.add_element(elem_id, node_ids)

    def __repr__(self):
        return f"Mesh(\n  nodes={list(self.nodes.values())},\n  elements={list(self.elements.values())}\n)"


