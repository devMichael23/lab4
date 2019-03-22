import random
import networkx as nx


class SocialNetwork:
    def __init__(self, countUser:int):
        self.countUser = countUser
        self.graph = nx.Graph()
        for i in range(self.countUser):
            self.graph.add_node(i)
        for i in range(self.countUser):
            neighbors = len(list(self.graph.neighbors(i)))
            if neighbors < 4:
                edges = random.randint(1, 4 - neighbors)
                while edges > 0:
                    neighbor = random.randint(0, self.countUser-1)
                    if neighbor == i or len(list(self.graph.neighbors(neighbor))) > 3:
                        continue
                    else:
                        self.graph.add_edge(i, neighbor)
                        edges -= 1

    def getGraph(self):
        return self.graph

    def getNeighbors(self, key:int):
        return self.graph.neighbors(key)

    def getNodes(self):
        return self.graph.nodes()