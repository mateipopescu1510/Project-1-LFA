# Project-1-LFA
* The data is stored in the dfa class
* The graph is kept as n structures of the from [nodeIndex, bool, (nextNode1, letter), (nextNode2, letter)...], where n represents the number of nodes and the bool value whether the node is a final state
* [node, bool] - default if theres no next node
* [node, (next1, l), (next2, l), ..., bool]
* [0, False, (1, a), (2, b)]
* [3, False, (5, c)]
* [4, False, (4, a), (5, c)]
* [5, True] 
