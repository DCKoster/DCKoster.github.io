layout: page
title: Analysis
permalink: /analysis/

# Analysis
For the Analysis, the three different starting points (2, 1, 1), (1, 2, 1) and (1, 1, 2) are incorporated into a Kripke Model. As it is not possible for these worlds to reach each other, they will be shown in separate figures to provide a better understanding of what is happening at each step. 

The first starting point will be (2, 1, 1). This starting point is in the form (b+c, b, c). As explained for the formal model, it is connected to the node (b+c, b + 2*c, c) through a relation for b and the node (b+c, b, 2*b + c) through a relation for c. 
The nodes will continue to branch out, with each node having one relation for a, one for b and one for c. The starting state of this part of the Kripke Model can be seen in figure INSERT.

![Minion](https://github.com/DCKoster/DCKoster.github.io/tree/main/assets/1_1.png)


After the first public announcement, in which Achmed announces that he does not know his number, the option for (2, 1, 1) is removed from the model. This is because Achmed would know his number if he were to see two ones, and Bert and Carl, perfect logicians as they are, would realise this as well. The second state can be seen in figure INSERT. 

![Minion](https://guides.github.com/assets/1_2.png)

Bert is second to announce that he does not know his number. He logically reasoned that the numbers he is seeing, are not a multiple of the states in which he is sure what the numbers would be. For Bert this is the state (2, 3, 1). This is visualised in figure INSERT, as there are no relations for Bert outgoing of this state, but there are for all other states. Figure INSERT shows the third state, which occurs after Bert his announcement. 

![Minion](https://guides.github.com/assets/1_3.png)

Carl is the third one to announce he does not know his number. Again, he logically reasoned that the numbers on the heads of the other two are not multiples of the states he is sure he knows the number. These are states (2, 3, 5) and (2, 1, 3) for Carl. The result of his announcement is in figure INSERT

![Minion](https://guides.github.com/assets/1_4.png)

After the three public announcements that Achmed, Bert and Carl do not know their number, Achmed announces that he now knows his number and that it is 50. All states in which Achmed can be sure to know his number are written down, which are (4, 3, 1), (8, 3, 5) and (4, 1, 3). 

![Minion](https://guides.github.com/assets/1_5.png)

The second starting point is (1, 2, 1). This starting point is in the form (a, a+c, c). It is connected to the node (a + 2*c, a+c, c) through a relation for a and the node (a, a+c, 2*a + c) through a relation for c. The starting state has the same Minion structure as the previous part, as can be seen in figure INSERT. 
![Minion](https://guides.github.com/assets/2_1.png)

The first public announcement of Achmed does not influence the model, as there is no world in which he can be sure that he knows his number. The second public announcement by Bert does, as the starting point (1, 2, 1) is reasoned not to be the true state. The resulting model is shown in figure INSERT. 

![Minion](https://guides.github.com/assets/2_2.png)

The third public announcement by Carl influences the model in the same way, removing all states in which Carl can be absolutely sure that he knows the model. This state is (1 ,2, 3). The model after the third announcement is shown in figure INSERT. 

![Minion](https://guides.github.com/assets/2_3.png)

Lastly, Achmed now announces he knows his number again, which leaves the states (3, 2, 1) and (5, 2, 3) to be written down. 

![Minion](https://guides.github.com/assets/2_4.png)

The third starting point is (1, 1, 2). This starting point is in the form (a, b, a+b). It is connected to the node (a + 2*b, b, a+c) through a relation for a and the node (a, a + 2*b, a+b) through a relation for b. Again, the starting state has the same Minion structure as the previous two parts and is depicted in figure INSERT. 
![Minion](https://guides.github.com/assets/3_1.png)

This time, the first and second public announcements, from Achmed and Bert respectively, do not influence the model as they both do not have any worlds they are certain to know their numbers. The third one by Carl does influence it and removes the starting points, (1, 1, 2). This first step is depicted in figure INSERT. The last announcement by Achmed provides one state, in which he is entirely sure which number he has, to write down: (3, 1, 2). This is also depicted in figure INSERT. 
![Minion](https://guides.github.com/assets/3_3.png)




After going through all public announcement through every starting point, the states  (4, 3, 1), (8, 3, 5), (4, 1, 3), (3, 2, 1), (5, 2, 3) and (3, 1, 2) are written down. According to the logic, Achmed knows that one of these states is the actual state. Now the fact that Achmed says his number is 50 comes into play. In the actual state his number, the first number of the triplet, should be a divisor for 50 which can be either 1, 2, 5, 10, 25 or 50. Only for the state (5, 2, 3) the first number is a divisor of 50, resulting in the conclusion that this is the actual state. 
