def dfs(u, count):
    if u == 'end':
        return count + 1
    if u.islower():
        visited.append(u)

    for v in graph[u]:
        if v not in visited:
            count = dfs(v, count)

    if u in visited:
        visited.remove(u)
    return count


f = open("input.txt", "r")

graph = {}
visited = []

for line in f:
    u, v = line.strip().split('-')
    if v == 'start' or u == 'end':
        u, v = v, u
    try:
        graph[u].append(v)
    except KeyError as e:
        graph[u] = [v]
    if u != 'start' and v != 'end':
        try:
            graph[v].append(u)
        except KeyError as e:
            graph[v] = [u]

print(dfs('start', 0))
