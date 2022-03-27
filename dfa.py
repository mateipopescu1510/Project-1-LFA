class dfa:
    graph = []

    def __init__(self, nodes):
        for i in range(nodes):
            nodeInfo = []
            nodeInfo.append(i)
            nodeInfo.append(False)
            self.graph.append(nodeInfo)

    def put(self):
        print(self.graph)

    def addEdge(self, edge):
        nextNode = (edge[1], edge[2])
        self.graph[edge[0]].append(nextNode)

    def setInitialState(self, q):
        self.initialState = q

    def finalState(self, q):
        self.graph[q][1] = True

    def checkNextLetter(self, q, word, path):
        if not word:
            if self.graph[q][1]:
                path.append(q)
                return path
            return False
        if len(self.graph[q]) == 2:
            return False
        for edge in range(2, len(self.graph[q])):
            if word[0] == self.graph[q][edge][1]:
                newPath = path
                newPath.append(q)
                return self.checkNextLetter(self.graph[q][edge][0], word[1:], newPath)
        return False

    def checkWord(self, word):
        currentState = self.initialState
        path = []
        path.append(self.initialState)
        result = self.checkNextLetter(initialState, word, path)
        if result:
            print(True, *result)
        else:
            print(result)


cin = open("input.txt")
init = cin.readline().split()
numberOfNodes = int(init[0])
numberOfEdges = int(init[1])

G = dfa(numberOfNodes)

for i in range(numberOfEdges):
    edge = cin.readline().split()
    edge[0], edge[1] = int(edge[0]), int(edge[1])
    G.addEdge(edge)

initialState = int(cin.readline())
G.setInitialState(initialState)

finalStates = [int(q) for q in cin.readline().split()]
finalStates.pop(0)
for q in finalStates:
    G.finalState(q)

numberOfWords = int(cin.readline())
for i in range(numberOfWords):
    word = cin.readline()[:-1]
    G.checkWord(word)
