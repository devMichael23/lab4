from SocialNetwork import SocialNetwork
import matplotlib.pyplot as plt
import networkx as nx
import random
import pylab as pl
pl.ion()

countUser = 100

def find(network:SocialNetwork, user:int, count:int)->list:
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
def listOfColor(lst:list, count:int, user:int)->list:
    lstColors = []
    i=0
    while i < count:
        lstColors.append('purple')
        i += 1
    for j in lst:
        lstColors[j]='r'
    lstColors[user] = 'green'
    return lstColors

def main(network:SocialNetwork, ls):

    nx.draw(network.getGraph(), node_size=300, node_color=ls, edge_color='blue', font_color='yellow', font_weight='normal', font_size=7, with_labels=True)


net = SocialNetwork(countUser)
size = len(list(net.getNodes()))

plt.show()

for i in range(size):
    pl.clf()
    ls = listOfColor(find(net, i, 1), countUser, i)
    main(net, ls)
    pl.show()
    pl.pause(1)

