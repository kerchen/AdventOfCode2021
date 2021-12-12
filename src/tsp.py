

class CaveSystem:
    def __init__(self, connections: list):
        self.nodes = dict()
        for link in connections:
            node_names = link.split('-')
            for i in range(2):
                if node_names[i] not in self.nodes.keys():
                    self.nodes[node_names[i]] = []
            self.nodes[node_names[0]].append(node_names[1])
            self.nodes[node_names[1]].append(node_names[0])

    def node_count(self) -> int:
        return len(self.nodes.keys())

    def are_directly_connected(self, a_node: str, b_node: str) -> bool:
        return b_node in self.nodes[a_node]
