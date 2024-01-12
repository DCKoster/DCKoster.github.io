# Formal Model
The model will be presented as a S53 Kripke Model: ⟨S, π, Ra, Rb, Rc⟩. Each world w in S represents a set of three positive integers which are possible values on the heads of the three participants, in the order of Achmed, Bert, Carl. Since one of these three values has to be the sum of the other two, a world (a, b, c) follows one of these three rules:
a = b + c 
b = a + c
c = a + b

Since it is an S5 model, all accessibility relations are equivalence relations (symmetric, transitive, reflexive). Reflexive and transitive relations are not drawn. Edges represent symmetric arrows. Furthermore, there is either 0 or 1 edge between each world, where the edge represents a symmetric relation for one of the three agents. This is because each of the three persons knows they have either the sum or the difference of the two values they see on the others’ heads. Therefore, the only edges for one person are between two such possible worlds, and these never overlap with the equivalence relations of the others.

The riddle does not state any upper bound for the numbers. The only constraint is that they are positive integers, so larger than 0. To create an accurate model with Kripke semantics, the initial Kripke model would therefore have to include an infinite number of worlds.

However, all models which branch out from a world where the numbers follow the pattern (2x, x, x), are similar to all other models branching out from (2x, x, x), where the models can be made identical by dividing all numbers by x. For example, the worlds (2, 1, 1), (2, 3, 1), and (2, 1, 3) in the part of the model displayed below could be replaced with the worlds (10, 5, 5), (10, 15, 5), and (10, 5, 15) by multiplying all numbers by 5.



In the same way, all models branching out from (x, 2x, x) are logically the same, and also those branching from (x, x, 2x).

For any triple (x, y, z) where one number is the sum of the other two, if the largest number is replaced by the difference of the other two numbers, and this action is repeated enough times, it will always result in a triple (2w, w, w), (w, 2w, w), or (w, w, 2w). For example, applying this to the world (2, 3, 1) above, it results in (2, 1, 1). Therefore, a model that branches out from the worlds (2, 1, 1), (1, 2, 1), and (1, 1, 2) will include all worlds (if it is infinite). Later in the strategy section, it will become clear that this model does not have to branch out infinitely to come to the solution to the riddle.

This “branching out” is done in the following, systematic way. Each world has 3 relations to other worlds, 1 for each agent, because as explained before, the agents know they have either the sum or the difference of the other two numbers that they can see. The only exceptions are the “root” worlds (2, 1, 1), (1, 2, 1), and (1, 1, 2), where one of the agents knows their number is 2, because the difference of 1 and 1 would be 0, which is not allowed.

Since each world has 3 connections to other worlds, each world w  = (x, y, z) branches out (downwards) to two other worlds u and v, where
If max(x,y,z) = x: u = (x, x+z, z) and v = (x, y, x+y)
If max(x,y,z) = y: u = (y+z, y, z) and v = (x, y, x+y)
If max(x,y,z) = z: u = (y+z, y, z) and v = (x, x+z, z).

After creating the initial model in 3 separate parts by branching out from the 3 different root worlds, the public announcement logic language 𝓛K[ ] [2] will be used to restrict the model to fewer worlds as announcements are made.
