class Element:
    def __init__(self, element_id: int, node_ids: list[int]):
        """

        :param element_id:
        :param node_ids:

        """
        self.id = element_id
        self.node_ids = node_ids
    def __repr__(self):
        return f"Element(id={self.id}, node_ids={self.node_ids})"