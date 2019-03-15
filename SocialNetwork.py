from Graph import Graph, Vertex
import random

class SocialNetwork:
    def __init__(self, count):
        self.network = Graph()
        for i in range(1, count+1):
            self.network.addVertex(i)
        for i in range(1, count+1):
            for j in range(1, self.pickNumber()+1):
                ran = random.randint(1, count)
                if ran in self.network:
                    ran = random.randint(1, count)
                if ran == i:
                    ran = random.randint(1, count)
                self.network.addEdge(i, ran)

    def getNetwork(self):
        return self.network

    def pickNumber(self):
        return int(random.randint(1, 4))
