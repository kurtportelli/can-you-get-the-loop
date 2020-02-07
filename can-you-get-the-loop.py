def loop_size(node):
    index = 0
    nodes = {}
    while node not in nodes:
        nodes[node] = index
        node = node.next
        index += 1
    return index - nodes[node]
