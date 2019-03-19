from Graph import Graph, Vertex
import random
import networkx as nx


class SocialNetwork:
    def __init__(self, count):
        self.count = count
        self.graph = Graph()
        self.Graph = nx.Graph()
        for i in range(1, self.count+1):
            self.graph.addVertex(i)
            self.Graph.add_node(str(i))
        for i in range(1, self.count+1):
            if self.graph.vertices[i].getCount() <= 2:
                num = self.pickNumber(4)
            else:
                continue
            for j in range(1, num+1):
                ran = random.randint(1, self.count)
                while ran in self.graph.vertices[i]:
                    ran = random.randint(1, self.count)
                while ran == i:
                    ran = random.randint(1, self.count)
                if self.graph.vertices[i].getCount() > 3:
                    break
                else:
                    self.graph.addEdge(i, ran)
                    self.graph.addEdge(ran, i)
                    self.Graph.add_edge(str(i), str(ran))

    def getVertices(self, key):
        return self.graph.vertices[key]

    def getVertexForKey(self, key):
        return self.graph.vertices[key].connected.keys()

    def getGraph(self):
        return self.graph

    def getDrawGraph(self):
        return self.Graph

    def pickNumber(self, last):
        return int(random.randint(1, last))

    def getSize(self):
        return self.count
