class dfa:
    graph = []

    def __init__(self, numberOfNodes):
        for i in range(numberOfNodes):
            nodeInfo = []
            nodeInfo.append(i)
            nodeInfo.append(False)
            self.graph.append(nodeInfo)
            # [index, False]

    def addEdge(self, edge):
        # edge[1] = next index
        # edge[2] = letter
        nextNode = (edge[1], edge[2])
        self.graph[edge[0]].append(nextNode)
        # [index, bool, (nextIndex, letter)]

    def setInitialState(self, q):
        self.initialState = q

    def finalState(self, q):
        self.graph[q][1] = True
        # [index, False, ...] -> [index, True, ...]

    def checkNextLetter(self, q, word, path):
        if not word:
            if self.graph[q][1]: # if current state is final
                path.append(q)
                return path
            return False
        if len(self.graph[q]) == 2: # if the word still has letters but there are no more next edges
            return False 
        for edge in range(2, len(self.graph[q])): # all edges
            if word[0] == self.graph[q][edge][1]:
                newPath = path
                newPath.append(q)
                return self.checkNextLetter(self.graph[q][edge][0], word[1:], newPath)
                break
        return False

    def checkWord(self, word):
        currentState = self.initialState
        path = []
        path.append(self.initialState)
        result = self.checkNextLetter(initialState, word, path)
        if result:
            print(True, *result[1:])
        else:
            print(result)


cin = open("input.txt")

init = cin.readline().split()
numberOfNodes = int(init[0])
numberOfEdges = int(init[1])

Graph = dfa(numberOfNodes)

for e in range(numberOfEdges):
    edge = cin.readline().split()
    edge[0], edge[1] = int(edge[0]), int(edge[1])
    Graph.addEdge(edge)

initialState = int(cin.readline())
Graph.setInitialState(initialState)

finalStates = [int(q) for q in cin.readline().split()]
finalStates.pop(0)
for q in finalStates:
    Graph.finalState(q)

numberOfWords = int(cin.readline())
for i in range(numberOfWords):
    word = cin.readline()[:-1]
    if word == "#":
        Graph.checkWord("")
    else:
        Graph.checkWord(word)
