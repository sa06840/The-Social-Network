
#Mini Facebook

#Constructing Social Network

import csv

def readcsv(filename):
    matrix = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    return matrix

def constructing_social_network(matrix):
    social_network = {}
    for i in matrix[0]:
        if i != '':
            social_network[i] = []
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if int(matrix[i][j]) != 0:
                social_network[matrix[i][0]].append((matrix[0][j], int(matrix[i][j])))
    return social_network

filename = 'friendships.csv'
matrix = readcsv(filename)
print('Social Network: ')
print(constructing_social_network(matrix), '\n')

#checking friends list
def get_friends_list(social_network,user):
    friends_list= []
    for i in social_network[user]:
        friend = i[0]
        friends_list.append(friend)
    return friends_list 

social_network = constructing_social_network(matrix)
user = "Shah Jamal Alam"
print("Friends of" + str(user) + ': ' + str(get_friends_list(social_network, user)), '\n')