import sys
sys.stdin = open("input.txt", "r")

firsstLine = input().strip().split(' ')
n = int(firsstLine[0])
m = int(firsstLine[1])
print('n:', n, 'm:',m)


def dfs(start_node):
    if start_node in visited:
        return 
    else: 
        visited.add(start_node)
        print(start_node)
        
        if start_node in G:
            for n in G[start_node]:
                dfs(n)

G = {}

for i in range(0, m):
    Line = input().strip().split()
    u = int(Line[0])
    v = int(Line[1])

    # For u node
    if u not in G:
        G[u] = []
    G[u].append(v)

    # For v node - bidirectional
    # if v not in G:
    #     G[v] = []
    # G[v].append(u)

print(G)

visited = set()
start_node = int(input())
print(start_node)

print("visiting sequence: ")
dfs(start_node)