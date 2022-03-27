# Project-1-LFA
* The data is stored in the dfa class
* The graph is kept as n structures of the form [nodeIndex, bool, (nextNode1, letter), (nextNode2, letter), ...], where n represents the number of nodes and the bool value whether the node is a final state
* [nodeIndex, False] - set by default
* "0 1 a" and "0 2 b" -> [0, False, (1, a), (2, b)]
* "3 5 c" -> [3, False, (5, c)]
* "4 4 a" and "4 5 c" -> [4, False, (4, a), (5, c)]

* For each word, the program prints either False or True followed by the path of the accepted word
