import os


def load_instance(filename: str):
    filepath = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(filepath, mode="r") as file:
        lines = file.readlines()
        header = lines[0].strip().split()
        n_nodes = int(header[0])
        edges = []
        node_set = set()
        for line in lines[1:]:
            i, j = line.strip().split()
            edges.append((int(i), int(j)))
            node_set.add(int(i))
            node_set.add(int(j))
    nodes = sorted(node_set)
    assert len(nodes) == n_nodes, "Wrong number of nodes specified"
    return {"nodes": nodes, "edges": edges}
