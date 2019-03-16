from Graph import Graph, Vertex
import random

class SocialNetwork:
    def __init__(self, count):
        self.graph = Graph()
        for i in range(1, count+1):
            self.graph.addVertex(i)
        for i in range(1, count+1):
            for j in range(1, self.pickNumber()+1):
                ran = random.randint(1, count)
                if ran in self.graph:
                    ran = random.randint(1, count)
                if ran == i:
                    ran = random.randint(1, count)
                self.graph.addEdge(i, ran)

    def getVertices(self, key):
        return self.graph.vertices[key]

    def getVertexForKey(self, key):
        return self.graph.vertices[key].connected.keys()

    def getGraph(self):
        return self.graph

    def pickNumber(self):
        return int(random.randint(1, 4))
