
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

def get_cost(social_network, profiles, user):
    cost = {}
    unknown = []
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
    return cost



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
print('\n')



#User's Connection

def get_users_connection(social_network, user, target_user):
    cost = {}
    unknown = []
    path = []
    parent = {}
    lst_of_lowest = []
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
        lst_of_lowest.append(lowest)
        for neighbour in get_neighbours(social_network, lowest):
            c1 = cost[lowest] + neighbour[1]
            c2 = cost[neighbour[0]]
            if c1 < c2:
                cost[neighbour[0]] = c1
                parent[neighbour[0]] = lowest
    lst_of_lowest.remove(user)
    for i in lst_of_lowest:
        path.append((parent[i], i))
    for i in range(len(path)):
        if path[i][0] == user and path[i][1] == target_user:
            result = []
            result.append(path[i])
            return result
        elif path[i][1] == target_user:
            path[i], path[len(path)-1] = path[len(path)-1], path[i]
            break
    shortest_path = []
    reversed_path = []
    for i in range(len(path), 0, -1):
        reversed_path.append(path[i-1])
    edge = reversed_path[0]
    shortest_path.append(edge)
    for i in reversed_path:
        if edge[0] == i[1]:
            shortest_path.insert(0, i)
            edge = i
            if i[0] == user:
                return shortest_path

target_user = 'Rameez Ragheb'
print('Path from ' + user + ' to ' + target_user + ': ' + str(get_users_connection(social_network, user, target_user)), '\n')



#Add a Friend

def add_friend(social_network, profiles, user, friend):
    cost_dictionary = get_cost(social_network, profiles, user)
    cost = cost_dictionary[friend]
    social_network[user].append((friend, cost))
    return social_network

friend = 'Sajal Rana'
print('Social Network: ')
print(add_friend(social_network, profiles, user, friend), '\n')



#Remove a Friend

def unfriend(social_network, user, remove_friend):
    for i in social_network[user]:
        if remove_friend == i[0]:
            social_network[user].remove(i)
    return social_network

remove_friend = 'Waqar Saleem'
print('Social Network: ')
print(unfriend(social_network, user, remove_friend))