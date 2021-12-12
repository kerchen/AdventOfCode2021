

class CaveSystem:
    def __init__(self, connections: list):
        self.nodes = dict()
        for link in connections:
            node_names = link.split('-')
            for i in range(2):
                if node_names[i] not in self.nodes.keys():
                    self.nodes[node_names[i]] = set()
            self.nodes[node_names[0]].add(node_names[1])
            self.nodes[node_names[1]].add(node_names[0])

    def node_count(self) -> int:
        return len(self.nodes.keys())

    def are_directly_connected(self, a_node: str, b_node: str) -> bool:
        return b_node in self.nodes[a_node]

    def find_all_paths(self):
        all_paths = []
        current_path = []

        def can_extend(cave, path):
            if cave not in path:
                return True
            return False

        def follow_path(cave: str, path: list, found_paths) -> bool:
            if not can_extend(cave, path):
                return

            path.append(cave)
            if cave == 'end':
                found_paths.append(path)
                return

            for adjacent_cave in self.nodes[cave]:
                path_trial = path.copy()
                follow_path(adjacent_cave, path_trial, found_paths)

        follow_path('start', current_path, all_paths)
        return all_paths
