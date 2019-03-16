from SocialNetwork import SocialNetwork

def find(network:SocialNetwork, user, count):
    userFriends = network.graph.vertices[user].connected.keys()
    strangers = 0
    for man in network.graph:
        if man.key != user and user not in network.graph.vertices[man.key]:
            quantity = 0
            manFriends = network.graph.vertices[man.key].connected.keys()
            for f in userFriends:
                if f in manFriends:
                    quantity += 1
            if quantity == count:
                strangers += 1
    return strangers


net = SocialNetwork(10)
for i in net.graph:
    print(i)

print(find(net, 1, 1))