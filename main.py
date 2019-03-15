from SocialNetwork import SocialNetwork

def find(network:SocialNetwork, user, count):
    user_friends = network.network.vertices[user].connected.keys()
    strangers = 0
    for man in network.network:
        if man.key != user and user not in network.network.vertices[man.key]:
            count1 = 0
            man_friends = network.network.vertices[man.key].connected.keys()
            for f in user_friends:
                if f in man_friends:
                    count1 += 1
            if count1 == count:
                strangers += 1
    return strangers


net = SocialNetwork(10)
for i in net.network:
    print(i)

print(find(net, 1, 1))