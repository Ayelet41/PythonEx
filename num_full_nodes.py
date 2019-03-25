#Number of Full Nodes in a Binary Tree
#Iterative way to count full nodes
class Node:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
class Tree:
    def __init__(self, root_node = None):
            self.root = root_node
    
    # Required collection modules have already been imported. 
    def number_of_full_nodes(self,root):
        q =deque()
        count=0
        if root:
            q.append(root)
            while q:
                node = q.pop()
                if node.data and node.right_child and node.left_child:
                    count += 1
                    q.append(node.right_child)
                    q.append(node.left_child)
                        
        return count
            
        
