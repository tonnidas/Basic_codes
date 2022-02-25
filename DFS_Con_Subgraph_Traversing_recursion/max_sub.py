import sys
# sys.stdin = open("maximal_sub.txt", "r")

def dfs(start_node):
    if start_node in visited:
        return 
    else: 
        visited.add(start_node)
        if start_node in G:
            for n in G[start_node]:
                dfs(n)


totalCases = int(input())
input() # blank line

for t in range(totalCases):

    G = {}
    big_node = input()
    c = ord(big_node)

    for i in range(65, c+1, 1):
        # print(chr(i))
        G[chr(i)] = []
        
    visited = set()
    count = 0

    while(True):
        try:
            Line = input()
        except EOFError:
            break

        if len(Line) == 0:
            break

        u = (Line[0])
        v = (Line[1])
        G[u].append(v)
        G[v].append(u)

    for k in G.keys():
        if k not in visited:
            dfs(k)
            count = count + 1
    
    print(count)
    if t != totalCases-1:
        print()