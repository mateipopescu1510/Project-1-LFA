class dfa:
    graph = []
    def __init__(self, nodes):
        for i in range(nodes):
            nodeInfo=[]
            nodeInfo.append(i) # node index
            nodeInfo.append(False) # final node?
            self.graph.append(nodeInfo)
    def put(self):
        print(self.graph)
    def addEdge(self, edge):
        nextNode = (edge[1], edge[2])
        self.graph[edge[0]].append(nextNode)
    def initialState(self, k):
        self.begin = k
    def finalState(self, k):
        self.graph[k][1] = True
    def checkNextLetter(self, k, word):
        #TODO check if theres a next edge for the current letter
        if not word:
            if self.graph[k][1]:
                return True
            return False
        if len(self.graph[k]) == 2:
            return False
        for e in range(2, len(self.graph[k])):
            if word[0] == self.graph[k][e][1]:
                #newPath = path
                #newPath.append(k)
                return self.checkNextLetter(self.graph[k][e][0], word[1:])
        return False
    def checkWord(self, word):
        currentState = self.begin
        path = []
        path.append(self.begin)
        #print(begin, word, path)
        result = self.checkNextLetter(begin, word)
        return result

cin = open('input.txt', 'r')
init = cin.readline().split()
nodes = int(init[0])
edges = int(init[1])
print(f"nodes = {nodes}")
print(f"edges = {edges}")
G = dfa(nodes)

for i in range(edges):
    edge = cin.readline().split()
    edge[0], edge[1] = int(edge[0]), int(edge[1])
    G.addEdge(edge)

begin = int(cin.readline())
G.initialState(begin)

finalStates = [int(k) for k in cin.readline().split()]
finalStates.pop(0)
for k in finalStates:
    G.finalState(k)

G.put()
numberOfWords = int(cin.readline())

for i in range(numberOfWords):
    word = cin.readline()[:-1]
    print(word)
    print(G.checkNextLetter(G.begin, word))




