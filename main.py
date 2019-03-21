from SocialNetwork import SocialNetwork
import matplotlib.pyplot as plt
import networkx as nx

countUser = 250

def find(network:SocialNetwork, user, count)->list:
    userFriends = list(network.getNeighbors(user))
    strangers = []
    size = len(list(network.getNodes()))
    for man in range(size):
        if man != user and man not in userFriends:
            quantity = 0
            manFriend = list(network.getNeighbors(man))
            for f in userFriends:
                if f in manFriend:
                    quantity += 1
            if quantity == count:
                strangers.append(man)
    return strangers

#lst - список незнакомцев, count - число вершин графа
def listOfColor(lst:list, count, user)->list:
    lstColors = []
    i=0
    while i < count:
        lstColors.append('purple')
        i += 1
    for j in lst:
        lstColors[j]='r'
    lstColors[user] = 'green'
    return lstColors


net = SocialNetwork(countUser)

lstColor = find(net,1,1)

nx.draw(net.getGraph(), node_size=300, node_color=listOfColor(lstColor, countUser, 1), edge_color='blue', font_color='yellow', font_weight='normal', font_size=7, with_labels=True)
plt.show()

