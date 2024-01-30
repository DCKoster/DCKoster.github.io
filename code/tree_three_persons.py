import networkx as nx

class Node:
   def __init__(self, data, index):
      self.left = None
      self.right = None
      self.data = data
      self.index = index

   def create_tree_threesum(self, depth):
        if depth == 0:
            return 

        if self.index == 0:
            left_tuple = (self.data[0], self.data[0] + self.data[2], self.data[2])
            self.left = Node(left_tuple, 1)
            self.left.create_tree_threesum( depth-1)

            right_tuple = (self.data[0], self.data[1], self.data[0] + self.data[1])
            self.right = Node(right_tuple, 2)
            self.right.create_tree_threesum( depth-1)
    
        if self.index == 1:
            left_tuple = (self.data[1]+self.data[2], self.data[1], self.data[2])
            self.left = Node(left_tuple, 0)
            self.left.create_tree_threesum( depth-1)

            right_tuple = (self.data[0], self.data[1], self.data[0] + self.data[1])
            self.right = Node(right_tuple, 2)      
            self.right.create_tree_threesum( depth-1)

        if self.index == 2:
            left_tuple = (self.data[1]+self.data[2], self.data[1], self.data[2])
            self.left = Node(left_tuple, 0)
            self.left.create_tree_threesum( depth-1)

            right_tuple = (self.data[0], self.data[0] + self.data[2], self.data[2])
            self.right = Node(right_tuple, 1)      
            self.right.create_tree_threesum( depth-1)

        return
   
   def delete_root(self, index):
    left_subtree = None
    right_subtree = None
    if self.index == index:
        left_subtree = self.left
        right_subtree = self.right
    
    return left_subtree, right_subtree, self
       
   def create_graph(self, G=None, pos=None, x=0, y=0, layer=1):
        if G is None:
            G = nx.Graph()
            pos = {}

        current_id = str(self.data)  # Convert tuple to string for node identification
        pos[current_id] = (x, y)

        if self.left or self.right:  # Check if the node has children
            if self.left:
                self.left.create_graph(G, pos, x - 2 ** (5 - layer), y - 1, layer + 1)
                left_id = str(self.left.data)
                G.add_edge(current_id, left_id)

            if self.right:
                self.right.create_graph(G, pos, x + 2 ** (5 - layer), y - 1, layer + 1)
                right_id = str(self.right.data)
                G.add_edge(current_id, right_id)
        else:  # If the node has no children, add it to the graph
            G.add_node(current_id, index=self.index)

        return G, pos

# Print the tree
   def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    
    if self.right:
        self.right.PrintTree()
    print(self.data, self.index)