
#Mini Facebook


#Helper Functions

def get_profile_in_list(profiles, user):
    lst = []
    for i in profiles[user]:
        elem = i[1].split(', ')
        for j in elem:
            lst.append(j)
    return lst

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

def get_neighbours(G, node):
    neighbours = []
    for i in G[node]:
        neighbours.append(i)
    return neighbours



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
matrix_of_friendships = readcsv(filename)
print('Social Network: ')
print(constructing_social_network(matrix_of_friendships), '\n')



#User

user = 'Shah Jamal Alam'



#Checking Friends List

def get_friends_list(social_network, user):
    friends_list= []
    for i in social_network[user]:
        friend = i[0]
        friends_list.append(friend)
    return friends_list 

social_network = constructing_social_network(matrix_of_friendships)
print("Friends of " + str(user) + ': ' + str(get_friends_list(social_network, user)), '\n')



#Checking Mutual Friends

def get_mutual_friends(social_network, user1, user2):
    mutual_friends = []
    user1_friends = get_friends_list(social_network, user1)
    for i in social_network[user2]:
        if i[0] in user1_friends:
            mutual_friends.append(i[0])
    return mutual_friends

user2 = 'Waqar Saleem'
print('Mutual Friends of ' + str(user) + ' and ' + str(user2) + ': ' + str(get_mutual_friends(social_network, user, user2)), '\n')



#Constructing User Profiles

def readcsv(filename):
    matrix = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    return matrix

def constructing_profiles(matrix):
    profiles = {}
    for i in range(1, len(matrix[0])):
        for j in range(1, len(matrix)):
            if not(matrix[0][i] in profiles):
                profiles[matrix[0][i]] = [(matrix[j][0], matrix[j][i])]
            else:
                profiles[matrix[0][i]].append((matrix[j][0], matrix[j][i]))
    return profiles

filename = 'profiles.csv'
matrix_of_profiles = readcsv(filename)
print('Profiles: ')
print(constructing_profiles(matrix_of_profiles), '\n')



#Getting User's Profile

def get_user_profile(profiles, user):
    print('Profile of ' + user + ': ')
    for i in profiles[user]:
        print(i[0] + ': ' + i[1])

profiles = constructing_profiles(matrix_of_profiles)
get_user_profile(profiles, user)
print('\n')



#Recommending Friends

def get_recommended_friends(social_network, profiles, user):
    cost = {}
    unknown = []
    recommended_friends = []
    for node in social_network:
        cost[node] = 100000
        unknown.append(node)
    cost[user] = 0
    while not(is_empty(unknown)):
        lowest = None
        for node in unknown:
            if lowest is None:
                lowest = node
            elif cost[node] < cost[lowest]:
                lowest = node
        unknown.remove(lowest)
        for neighbour in get_neighbours(social_network, lowest):
            c1 = cost[lowest] + neighbour[1]
            c2 = cost[neighbour[0]]
            if c1 < c2:
                cost[neighbour[0]] = c1
    user_profile = get_profile_in_list(profiles, user)
    for i in cost:
        counter = 0
        i_profile = get_profile_in_list(profiles, i)
        for j in user_profile:
            if j in i_profile:
                counter = counter + 1
        new_cost = cost[i] - counter
        cost[i] = new_cost
    user_friends = get_friends_list(social_network, user)
    user_friends.append(user)
    for i in cost:
        if i not in user_friends:
            recommended_friends.append((i, cost[i]))
    recommended_friends = sorted(recommended_friends, key=lambda item: item[1])
    for i in range(1, len(recommended_friends)+1):
        recommended_friend = recommended_friends[i-1][0]
        print(str(i) + '. ' + recommended_friend)

print('Recommended Friends for ' + str(user) + ': ')
get_recommended_friends(social_network, profiles, user)