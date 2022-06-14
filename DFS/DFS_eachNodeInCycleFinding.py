# Problem: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # stack = list()
        color = dict()
        adj = dict()
        
        # creating color dictionary ----------------------
        for each in recipes:
            color[each] = "white"
        for each in ingredients:
            for i in each:
                color[i] = "white"
        for each in supplies:
            color[each] = "green"
        print(color)
        
        def dfs(node):
            if color[node] == "red" or color[node] == "green": 
                return color[node]
            
            if color[node] == "gray":
                color[node] = "red"
                return color[node]
            
            if color[node] == "white":
                color[node] = "gray"
                # stack.append(node)
                if node in adj:
                    for i in adj[node]:
                        if dfs(i) == "red":
                            color[node] = "red"
                            return "red"
                    color[node] = "green"
                    # stack.pop()
                    return color[node]
                else:
                    if color[node] == "green":
                        return "green"
                    else:
                        return "red"  
            
        # making the graph ----------------------
        for each in range(len(recipes)):
            adj[recipes[each]] = set(ingredients[each])
        print(adj)
        
        # going through each node in recipes ----------------------
        fin = list()
        for each in recipes:
            stack = list()
            if dfs(each) == "green":
                fin.append(each)
        
        return fin