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

def listOfColor(lst:list, count)->list:
    lstColors = []
    i=0
    while i < count:
        lstColors.append('purple')
        i += 1
    for j in lst:
        if j == 0:
            lstColors[j] == 'r'
        else:
            lstColors[j-1]='r'
    return lstColors


net = SocialNetwork(250)
for i in net.getGraph():
    print(i)

print()
print("Количество незнакомцев с заданным количеством общих знакомых: ", find(net, 1, 1))

lstColor, count = find(net,1,1)

nx.draw(net.getDrawGraph(), node_color=listOfColor(lstColor, 250), edge_color='blue', node_size=300, font_weight='normal', font_size=7, with_labels=True)
plt.show()

