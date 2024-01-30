import networkx as nx

class NodeFourPersons():
    def __init__(self, data, index):
      self.left = None
      self.right = None
      self.middle = None
      self.data = data
      self.index = index

    def create_tree_foursum(self, depth):
        if depth == 0:
            return 

        [a,b,c,d] = [self.data[0], self.data[1], self.data[2], self.data[3]]

        if self.index == 0:
            left_tuple = (a,a+c+d,c,d)
            self.left = NodeFourPersons(left_tuple, 1)
            self.left.create_tree_foursum(depth-1)

            middle_tuple = (a,b,a+b+d,d)
            self.middle = NodeFourPersons(middle_tuple, 2)
            self.middle.create_tree_foursum(depth-1)
    
            right_tuple = (a,b,c,a+b+c)
            self.right = NodeFourPersons(right_tuple, 3)
            self.right.create_tree_foursum(depth-1)

        if self.index == 1:
            left_tuple = (b+c+d,b,c,d)
            self.left = NodeFourPersons(left_tuple, 0)
            self.left.create_tree_foursum(depth-1)

            middle_tuple = (a,b,a+b+d,d)
            self.middle = NodeFourPersons(middle_tuple, 2)
            self.middle.create_tree_foursum(depth-1)
    
            right_tuple = (a,b,c,a+b+c)
            self.right = NodeFourPersons(right_tuple, 3)
            self.right.create_tree_foursum(depth-1)

        if self.index == 2:
            left_tuple = (b+c+d,b,c,d)
            self.left = NodeFourPersons(left_tuple, 0)
            self.left.create_tree_foursum(depth-1)

            middle_tuple = (a,a+c+d,c,d)
            self.middle = NodeFourPersons(middle_tuple, 1)
            self.middle.create_tree_foursum(depth-1)
    
            right_tuple = (a,b,c,a+b+c)
            self.right = NodeFourPersons(right_tuple, 3)
            self.right.create_tree_foursum(depth-1)

        if self.index == 3:
            left_tuple = (b+c+d,b,c,d)
            self.left = NodeFourPersons(left_tuple, 0)
            self.left.create_tree_foursum(depth-1)

            middle_tuple = (a,a+c+d,c,d)
            self.middle = NodeFourPersons(middle_tuple, 1)
            self.middle.create_tree_foursum(depth-1)
    
            right_tuple = (a,b,a+b+d,d)
            self.right = NodeFourPersons(right_tuple, 2)
            self.right.create_tree_foursum(depth-1)

        return

    def delete_root(self, index):
        left_subtree = None
        middle_subtree = None
        right_subtree = None

        if self.index == index:
            left_subtree = self.left
            middle_subtree = self.middle
            right_subtree = self.right
    
        return left_subtree, middle_subtree, right_subtree, self

    # Print the tree
    def PrintTreeFour(self):
        if self.left:
            self.left.PrintTreeFour()

        if self.middle:
            self.middle.PrintTreeFour()

        if self.right:
            self.right.PrintTreeFour()
        print(self.data, self.index)