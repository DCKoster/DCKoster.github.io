layout: page 
title: Introduction
permalink: /introduction/

# Introduction 
In this project we analyze the riddle “Who has the Sum?” which was invented by Jonathan Welton. The riddle goes as follows [1]:

Achmed, Bert, and Carl all have a positive integer on their forehead. They can only see the foreheads of others. One of the numbers is the sum of the other two. All the previous is common knowledge, all agents are perfect logicians, they always speak the truth, which is also common knowledge. They now successively make the truthful announcements: 
1. Achmed: 	‘‘I don’t know my number.’’ 
2. Bert: 	‘‘I don’t know my number.’’ 
3. Carl : 	‘‘I don’t know my number.’’ 
4. Achmed: 	‘‘I know my number. It is 50.’’ 
What are the other numbers?

Our research question is what the answer to this riddle is, and by deducing this answer, determining how complex it is for humans. To answer the question, we use Kripke possible worlds semantics. We first create a Kripke model that represents the initial state of information before any announcements are made. Then, as announcements are made, the number of possible worlds in the model decreases according to public announcement logic, until there is only one world where Achmed knows his number, and it is 50. The numbers of Bert and Carl in that world will be the answer to the riddle.

By using Kripke semantics, we will obtain a clear `timeline’ of the Kripke model, where each transition following a public announcement simplifies the model. This aids in answering our research question of how complex this riddle is for humans to figure out (without writing it out).
