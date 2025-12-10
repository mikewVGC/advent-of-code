
import math


class Connection():
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.distance = self.calc_distance(node1, node2)
        self.enabled = False

    def calc_distance(self, node1, node2):
        return math.sqrt(
            math.pow(node1.x - node2.x, 2) + math.pow(node1.y - node2.y, 2) + math.pow(node1.z - node2.z, 2)
        )


class Node():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.connections = {}

    def get_code(self):
        return f"{self.x}-{self.y}-{self.z}"

    def add_connection(self, node):
        code = node.get_code()
        if code not in self.connections:
            self.connections[code] = Connection(self, node)

    def has_connection(self, node):
        code = node.get_code()
        return code in self.connections



coords = {}
with open("2025/input/day08-example", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        coord = list(map(lambda x: int(x), line.split(',')))
        node = Node(*coord)
        coords[node.get_code()] = node


# find all distances between each node... is this a good idea?
for i, coord in coords.items():
    for k, node in coords.items():
        if i == k:
            continue

        if coord.has_connection(node):
            continue

        coord.add_connection(node)
        node.add_connection(coord)


# now find the shortest X * 2 distances
shortest = None
shortchecks = {}
shortlist = []
while True:
    for coord in coords.values():
        for code, connection in coord.connections.items():
            if shortest == None or (connection.distance < shortest.distance and connection.enabled == False):
                shortest = connection

    shortest.enabled = True
    shortlist.append(shortest)
    shortest = None

    if len(shortlist) == 10:
        break

for conn in shortlist:
    print(conn.node1.get_code(), conn.node2.get_code())
print('====')


# now figure out how many clusters we have
clusters = []
for conn in shortlist:
    if len(clusters) == 0:
        clusters.append([ conn ])
        continue

    # very dumb, but search clusters
    for cluster in clusters:
        add_to_current_cluster = False
        new_cluster = False
        for c in cluster:
            if (
                c.node1.get_code() == conn.node1.get_code() or
                c.node1.get_code() == conn.node2.get_code() or
                c.node2.get_code() == conn.node1.get_code() or
                c.node2.get_code() == conn.node2.get_code()
            ):
                add_to_current_cluster = True
                break
            else:
                new_cluster = True
                break

        if add_to_current_cluster:
            cluster.append(conn)
            break

        if new_cluster:
            clusters.append([ conn ])
            break

result = 0
for cluster in clusters:
    #print(len(cluster))
    for c in cluster:
        print(c.node1.get_code(), c.node2.get_code())
    print('---')

print(f"Part 1: {result}")
