import random
import networkx as nx


class SocialNetwork:
    # Конструктор сети, countUser - количество пользователей в сети
    def __init__(self, countUser:int):
        # Инициализация поля количества пользователей
        self.countUser = countUser
        # Инициализация пустого графа
        self.graph = nx.Graph()
        for i in range(self.countUser):
            # Добавление в граф всех пользователей
            self.graph.add_node(i)
        for i in range(self.countUser):
            # Инициализация поля, количество знакомых каждого пользователя
            neighbors = len(list(self.graph.neighbors(i)))
            # Если количесто знакомых < 4
            if neighbors < 4:
                # Инициализация поля допустимого количества связей
                edges = random.randint(1, 4 - neighbors)
                # Пока количество связей > 0
                while edges > 0:
                    # Инициализация поля знакомого пользоватедя
                    neighbor = random.randint(0, self.countUser-1)
                    # Если знакомый - это сам пользователь, или количество соседей > 3
                    if neighbor == i or len(list(self.graph.neighbors(neighbor))) > 3:
                        # Пропустить
                        continue
                    # Иначе
                    else:
                        # Добавить связь между пользователем и знакомым
                        self.graph.add_edge(i, neighbor)
                        # Уменьшить количество допустимых связей на 1
                        edges -= 1

    # Метод взятия сгенерированного графа
    def getGraph(self):
        return self.graph

    # Метод взятия знакомых определенного пользователя, key - пользователь
    def getNeighbors(self, key:int):
        return self.graph.neighbors(key)

    # Метод взятия количества всех пользователей
    def getNodes(self):
        return self.graph.nodes()