import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from root_nodes import *
from tree_four_persons import *
from tree_three_persons import *
from tree_product import *

# Method that shows the trees
def show_trees(trees):
    for tree in trees:
        # Create the graph and position
        G, pos = tree.create_graph()

        # Draw the tree
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_size=1000, font_weight="bold", font_size=10)

        plt.show()


# Method that creates the trees for three sum riddle
def create_trees_three_persons():
    # Create the three trees
    root_Achmed = Node((2,1,1), 0)
    root_Achmed.create_tree_threesum(3)

    root_Bert = Node((1,2,1), 1)
    root_Bert.create_tree_threesum(3)

    root_Carl = Node((1,1,2), 2)
    root_Carl.create_tree_threesum(3)

    # Deletion and visualization process
    trees = [root_Achmed, root_Bert, root_Carl]

    return trees

# Method that creates the trees for four sum riddle
def create_trees_four_persons(roots):
    trees = []
    for root in roots:
        tree = NodeFourPersons((root), np.argmax(root))
        tree.create_tree_foursum(2)
        trees.append(tree)
    return trees

# Main method that processes the three sum riddle
def three_persons():
    no_answer = True
    trees = create_trees_three_persons()
    print("THREE SUM RIDDLE")

    see_trees = int(input("\nDo you want to see the trees?\n"
                        "Enter number:\n"
                        "(0: No)\n"
                        "(1: Yes)\n"))

    if see_trees:
        show_trees(trees)

    while True:  # Process all the different announcements
        user_input = int(input(
            "\nEnter number: (0: (Achmed says: I do not know my number), "
            "1: (Bert says: I do not know my number), "
            "2: (Carl says: I do not know my number), "
            "3: Final number known)\n"))

        if user_input == 3:
            break
        
        new_trees = []
        for tree in trees:
            left_tree, right_tree, full_tree = tree.delete_root(index=user_input)
            if left_tree:
                new_trees.append(left_tree)
            if right_tree:
                new_trees.append(right_tree)
            if left_tree is None and right_tree is None:
                new_trees.append(full_tree)
        trees = new_trees

        if see_trees:
            show_trees(trees)

    name = int(input("Who knows the number?: (0: Achmed, 1: Bert, 2: Carl)\n"))
    answer = int(input("Enter the final number:\n"))

    print("\nThe final answer(s) are:")

    i = 1
    # Get the final results
    for tree in trees:
        if tree.index == name:
            if answer % tree.data[name] == 0: 
                no_answer = False
                factor = int(answer / tree.data[name])
                print("Solution " + str(i) + ":")
                print("\tAchmed has: " + str(tree.data[0] * factor) + "\n", 
                      "\tBert has: " + str(tree.data[1] * factor) + "\n",
                       "\tCarl has: " + str(tree.data[2] * factor) + "\n\n")
                i += 1

    if no_answer:
        print("None")

def product_riddle():
    no_answer = True
    see_trees = int(input("\nDo you want to see the trees?\n"
                        "Enter number:\n"
                        "(0: No)\n"
                        "(1: Yes)\n"))

    root_nodes = []
    user_inputs = []
    roots = generate_roots_product(root_nodes)

    trees = []
    for root in roots:
        tree = NodeProduct((root), np.argmax(root))
        tree.create_tree_product(2)
        trees.append(tree)

    if see_trees:
        show_trees(trees)

    while True:  # Process all the different announcements
        user_input = int(input(
            "\nEnter number: (0: (Achmed says: I do not know my number), "
            "1: (Bert says: I do not know my number), "
            "2: (Carl says: I do not know my number), "
            "3: Final number known)\n"))

        user_inputs.append(int(user_input))

        if user_input == 3:
            break
        
        new_trees = []
        for tree in trees:
            left_tree, right_tree, full_tree = tree.delete_root(index=user_input)
            if left_tree:
                new_trees.append(left_tree)
            if right_tree:
                new_trees.append(right_tree)
            if left_tree is None and right_tree is None:
                new_trees.append(full_tree)
        trees = new_trees

        if see_trees:
            show_trees(trees)

    name = int(input("Who knows the number?: (0: Achmed, 1: Bert, 2: Carl)\n"))
    answer = int(input("Enter the final number:\n"))

    i = 1
    print("\nThe final answer(s) are:")

    # Get the final results
    for tree in trees:
        if tree.index == name:
            if name not in user_inputs:
                if tree.data[name] == answer: 
                    no_answer = False
                    print("Solution " + str(i) + ":")
                    print("\tAchmed has: " + str(tree.data[0]) + "\n", 
                        "\tBert has: " + str(tree.data[1]) + "\n",
                        "\tCarl has: " + str(tree.data[2]) + "\n\n")
                    i += 1
            else:
                if tree.data[name] == answer and all(tree.data[i] != 1 for i in range(3)): 
                    no_answer = False
                    print("Solution " + str(i) + ":")
                    print("\tAchmed has: " + str(tree.data[0]) + "\n", 
                        "\tBert has: " + str(tree.data[1]) + "\n",
                        "\tCarl has: " + str(tree.data[2]) + "\n\n")
                    i += 1               

    if no_answer:
        print("None")

def four_persons():
    root_nodes = []
    all_triples = generate_roots_foursum(root_nodes)
    filtered_triples = filter_multiples(all_triples)
    trees = create_trees_four_persons(filtered_triples)

    print("\n\nFOUR SUM RIDDLE")
    while True:  # Process all the different announcements
        user_input = int(input(
            "\nEnter number: (0: (Achmed says: I do not know my number), "
            "1: (Bert says: I do not know my number), "
            "2: (Carl says: I do not know my number), "
            "3: (Dana says: I do not know my number), "
            "4: Final number known)\n"))

        if user_input == 4:
            break
        
        new_trees = []
        for tree in trees:
            left_tree, middle_tree, right_tree, full_tree = tree.delete_root(index=user_input)
            if left_tree:
                new_trees.append(left_tree)
            if middle_tree:
                new_trees.append(middle_tree)
            if right_tree:
                new_trees.append(right_tree)
            if left_tree is None and middle_tree is None and right_tree is None:
                new_trees.append(full_tree)
        trees = new_trees

    name = int(input("Who knows the number?: (0: Achmed, 1: Bert, 2: Carl, 3: Dana)\n"))
    answer = int(input("Enter the final number:\n"))

    i = 1
    print("\nThe final answer(s) are:")   

    # Get the final results
    for tree in trees:
        if tree.index == name:
            if answer % tree.data[name] == 0: 
                no_answer = False
                factor = int(answer / tree.data[name])
                print("Solution " + str(i) + ":")
                print("\tAchmed has: " + str(tree.data[0] * factor) + "\n", 
                      "\tBert has: " + str(tree.data[1] * factor) + "\n",
                       "\tCarl has: " + str(tree.data[2] * factor) + "\n",
                        "\tDana has: " + str(tree.data[3] * factor) + "\n")
                i += 1

    if no_answer:
        print("None")

if __name__ == "__main__":
    user_input = int(input("Which riddle do you want to do?: (0: Three sum, 1: Four sum, 2: Product)\n"))  
    if user_input < 0 or user_input > 2:
        print("Error: Please enter a valid number.")
        exit()
    if user_input == 0:
        three_persons()
    if user_input == 1:
        four_persons()
    if user_input == 2:
        product_riddle()
