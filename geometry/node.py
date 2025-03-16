class Node:
    def __init__(self, node_id: int, x: float, y: float):
        self.id = node_id
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node(id={self.id}, x={self.x}, y={self.y})"
