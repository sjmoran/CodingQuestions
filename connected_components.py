from collections import deque, defaultdict


def bfs(G, root, explored, components):
    q = deque([])
    q.append(root)
    explored.add(root)
    components[root] = [root]
    while len(q) > 0:
        node = q.popleft()
        neighbours = G[node]
        for node in neighbours:
            if node not in explored:
                q.append(node)
                explored.add(node)
                components[root].append(node)
    return explored, components


if __name__ == "__main__":

    G = {0: [1, 2], 1: [0, 6], 2: [0], 3: [4], 4: [3], 6: [9, 1], 9: [6]}
    print G
    explored = set([])
    components = defaultdict(list)

    for root, _ in G.items():
        if root in explored:
            print "Skipping: " + str(root)
        else:
            print "BFS from : " + str(root)
            explored, components = bfs(G, root, explored, components)

    for _, graph in components.iteritems():
        print graph
