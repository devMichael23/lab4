from SocialNetwork import SocialNetwork
import matplotlib.pyplot as plt
import networkx as nx

def find(network:SocialNetwork, user, count)->(list, int):
    userFriends = network.getVertexForKey(user)
    strangerCount = 0
    strangers = []
    for man in network.getGraph():
        if man.key != user and user not in network.getVertices(man.key):
            quantity = 0
            manFriends = network.getVertexForKey(man.key)
            for f in userFriends:
                if f in manFriends:
                    quantity += 1
            if quantity == count:
                strangerCount += 1
                strangers.append(man.key)
    return strangers, strangerCount


net = SocialNetwork(100)
for i in net.getGraph():
    print(i)
print()
print("Количество незнакомцев с заданным количеством общих знакомых: ", find(net, 1, 1))

nx.draw(net.getDrawGraph())
plt.show()

print()
print("Количество незнакомцев с заданным количеством общих знакомых: ", find(net, 1, 1))