from SocialNetwork import SocialNetwork
import matplotlib.pyplot as plt
import networkx as nx
import random
import pylab as pl

# Вызов метода для непрерывной анимации
pl.ion()

# Инициализация поля количества пользователей
countUser = 100

# Метод поиска незнакомцев с определенным количеством общих с заданным пользователем
# network - сгенерированная социальная сеть, user - исходных пользователь,
# count - количество общих знакомых
def find(network:SocialNetwork, user:int, count:int)->list:
    userFriends = list(network.getNeighbors(user))
    strangers = []
    size = len(list(network.getNodes()))
    for man in range(size):
        if man != user and man not in userFriends:
            # Инициализация поля общих
            quantity = 0
            manFriend = list(network.getNeighbors(man))
            # Обход списка друзей пользователя
            for f in userFriends:
                # Если f также среди знакомых man
                if f in manFriend:
                    # Количество общих знакомых увеличить на 1
                    quantity += 1
            # Если количество общих знакомых равно заданному
            if quantity == count:
                strangers.append(man)
    return strangers

# Метод установки нужных цветов
# lst - список незнакомцев с общими знакомыми, count - число пользоватейлей сети, 
# user - исходный пользователь
def listOfColor(lst:list, count:int, user:int)->list:
    lstColors = []
    i=0
    while i < count:
        lstColors.append('purple')
        i += 1
    # Обход списка незнакомых
    for i in lst:
        # Цвет незнакомца с общими знакомыми - красный
        lstColors[i]='r'
    # Цвет исходного пользователя - зеленый
    lstColors[user] = 'green'
    return lstColors

# Функция рисовки графа, network - социальная сеть,
# ls - список цветов
def main(network:SocialNetwork, ls):
    nx.draw(network.getGraph(), node_size=300, node_color=ls, edge_color='blue', font_color='yellow', font_weight='normal', font_size=7, with_labels=True)

net = SocialNetwork(countUser)
# Инициализация поля количества пользователей социальной сети
size = len(list(net.getNodes()))

# Вызов метода для показа графа
pl.show()

for i in range(size):
    try:
        # Вызов метода для очистки рисунка
        pl.clf()
        # Инициализация поля списка цветов
        ls = listOfColor(find(net, i, 1), countUser, i)
        # Вызов метода для отрисовки социальной сети
        main(net, ls)
        pl.show()
        # Вызов метода для паузы между переходами к следующему пользователю
        pl.pause(0.1)
    # Обработка возможных исключений
    except:
        print("Программа завершена до завершения алгоритма поиска")
        exit(0)
print("Программа успешна завершена")
