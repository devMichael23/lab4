from Graph import Graph, Vertex
import random
import time

class SocialNetwork:
    def __init__(self, count):
        self.graph = Graph()
        for i in range(1, count+1):
            self.graph.addVertex(i)
        for i in range(1, count+1):
            if self.graph.vertices[i].getCount() <= 2:
                num = self.pickNumber(4)
            else:
                continue
            for j in range(1, num+1):
                ran = random.randint(1, count)
                while ran in self.graph.vertices[i]:
                    ran = random.randint(1, count)
                while ran == i:
                    ran = random.randint(1, count)
                if self.graph.vertices[i].getCount() > 3:
                    continue
                else:
                    self.graph.addEdge(i, ran)
                    self.graph.addEdge(ran, i)

    def getVertices(self, key):
        return self.graph.vertices[key]

    def getVertexForKey(self, key):
        return self.graph.vertices[key].connected.keys()

    def getGraph(self):
        return self.graph

    def pickNumber(self, last):
        return int(random.randint(1, last))
