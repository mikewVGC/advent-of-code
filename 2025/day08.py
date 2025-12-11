
import math

class Connection():
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.distance = self.calc_distance(node1, node2)
        self.enabled = False
        self.dupe_check = False

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
with open("2025/input/day08", "r") as file:
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
            if shortest == None or (connection.distance < shortest.distance and connection.enabled == False and connection.dupe_check == False):
                shortest = connection

    dupe_found = False
    for short in shortlist:
        if (
            short.node1.get_code() == shortest.node2.get_code() and
            short.node2.get_code() == shortest.node1.get_code()
        ):
            dupe_found = True
            break

    if dupe_found == False:
        shortest.enabled = True
        shortlist.append(shortest)
    else:
        shortest.dupe_check = True

    shortest = None

    if len(shortlist) == 1000: # change this to 10 for example
        break

    # this loop is slow so adding a counter... easier than fixing it
    if len(shortlist) % 100 == 0:
        print(f"{len(shortlist)} shorties so far")

# now figure out how many clusters we have
clusters = []
for conn in shortlist:
    if len(clusters) == 0:
        clusters.append({
            conn.node1.get_code(): True,
            conn.node2.get_code(): True,
        })
        continue

    # very dumb, but search clusters
    found_cluster = False
    for cluster in clusters:
        add_to_current_cluster = False
        for c in cluster.keys():
            if (
                c == conn.node1.get_code() or
                c == conn.node2.get_code()
            ):
                add_to_current_cluster = True
                break

        if add_to_current_cluster:
            found_cluster = True
            cluster[conn.node1.get_code()] = True
            cluster[conn.node2.get_code()] = True

    if found_cluster == False:
        clusters.append({
            conn.node1.get_code(): True,
            conn.node2.get_code(): True,
        })

# merge clusters that share nodes
while True:
    ops = []
    for i, cluster in enumerate(clusters):
        for c in cluster.keys():
            for ii, ccluster in enumerate(clusters):
                if ii == i:
                    continue

                for cc in ccluster.keys():
                    if cc == c:
                        ops.append([ i, ii ])

    if len(ops) == 0:
        break

    for op in ops:
        clusters[op[0]].update(clusters[op[1]])
        clusters[op[1]] = {}

    ops = []


# okay last loop, lets count how many unique nodes are in each cluster
cluster_counts = []
for cluster in clusters:
    cluster_counts.append(len(cluster.keys()))

cluster_counts.sort(reverse=True)

# jk one more to get the top 3
result = 1
for i in cluster_counts[:3]:
    result *= i

print(f"Part 1: {result}")
