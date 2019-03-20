import random
import networkx as nx


class SocialNetwork:
    def __init__(self, countUser, countEdge):
        self.countUser = countUser
        self.countEdge = countEdge
        self.Graph = nx.Graph()
        for i in range(1, self.countUser+1):
            self.Graph.add_node(i)
        for i in range(1, self.countUser+1):
            leng = (2*countEdge)/(countUser*(countUser-1))
            if leng >= 1:
                continue
            else:
                ran = random.randint(1, self.countUser)
                while ran in self.Graph[i]:
                    ran = random.randint(1, self.countUser)
                while ran == i:
                    ran = random.randint(1, self.countUser)
                if leng > 3:
                    continue
                else:
                    self.Graph.add_edge(i, ran)