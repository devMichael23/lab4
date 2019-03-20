from SocialNetwork import SocialNetwork
import matplotlib.pyplot as plt
import networkx as nx

countUser = 250

def findN(network:SocialNetwork, user, count):
    userFriends = network.Graph[user]
    strangers = []
    for man in network.Graph.graph:
        for manKey in man:
            if manKey != user and manKey not in userFriends:
                quantity = 0
                manFriends = man
                for f in userFriends:
                    if f in manFriends:
                        quantity += 1
                if quantity == count:
                    strangers.append(manKey)
    return strangers

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


net = SocialNetwork(countUser, 4)

# print()
# print("Количество незнакомцев с заданным количеством общих знакомых: ", find(net, 1, 1))

# lstColor = find(net,1,1)
print(findN(net, 1,1))

nx.draw(net.getGraph(), node_size=300, font_weight='normal', font_size=7, with_labels=True)
plt.show()

