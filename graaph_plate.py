#Recursive
def DFS(root):
    #END Condition
    if not root:
        return
    visit(root)
    for node in root.adjacent: 
        if not node.visited:
            DFS(node)
#Iterative, implemented using a stack
def DFS_iter():
    root.visited = 1
    stack = []
    stack.append(root)
    while stack:
        n=stack.pop()
        visit(n)
        n.visited=1
        for node in n.adjacent:
            if not node.visited:
                stack.append(node)

#implement using a queue
def BFS(root):
    q = [root]
    root.visited = 1
    while q:
        n=q.pop()
        visit(n) #finish visit
        for node in n.adjacent:
            if not node.visited:
                node.visited = 1 #start to visit 
                q.insert(0,node)
# a mutant for trees to visit it level by level
def BFS(root):
    q = [root]
    root.visited = 1
    level = 0
    while q:
        n=q.pop()
        visit(n) #finish visit
        for node in n.adjacent:
            if not node.visited:
                node.visited = 1 #start to visit 
                q.insert(0,node)

