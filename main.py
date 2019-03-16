from SocialNetwork import SocialNetwork

def find(network:SocialNetwork, user, count):
    userFriends = network.getVertexForKey(user)
    strangers = 0
    for man in network.getGraph():
        if man.key != user and user not in network.getVertices(man.key):
            quantity = 0
            manFriends = network.getVertexForKey(man.key)
            for f in userFriends:
                if f in manFriends:
                    quantity += 1
            if quantity == count:
                strangers += 1
    return strangers


net = SocialNetwork(10)
for i in net.getGraph():
    print(i)
print()
print("Количество незнакомцев с заданным количеством общих знакомых: ", find(net, 1, 1))