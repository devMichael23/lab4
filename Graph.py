class Vertex:
    def __init__(self, key):
        self.key = key
        self.connected = {}

    def addNeighbor(self, edge, weight=0):
        self.connected[edge] = weight

    def __str__(self):
        return str(self.key) + " connected: " + str([i.key for i in self.connected])

    def __contains__(self, key)->bool:
        return key in self.connected

    def __iter__(self):
        return iter(self.connected.values())

    def getConnections(self)->int:
        return self.connected.keys()

    def getId(self):
        return self.key

    def getWeight(self, edge):
        return self.connected[edge]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num = 0

    def addVertex(self, key):
        self.num += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertexForKey(self, key):
        return self.vertices[key].connected.keys()

    def __contains__(self, key) -> bool:
        return key in self.vertices

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertices:
            self.addVertex(fromVertex)
        if toVertex not in self.vertices:
            self.addVertex(toVertex)
        self.vertices[fromVertex].addNeighbor(self.vertices[toVertex], weight)

    def __iter__(self):
        return iter(self.vertices.values())

dc = {}
dc[1] = 1,2,3,4
dc[2] = 5,6,7,8
print(dc)