
#Mini Facebook


#Helper Functions
# functions
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
age = '35'
country = 'New Zealand'
department = 'Data Structures and Algorithms'
hobbies = 'Cooking, Snooker'



#Checking Friends List

def get_friends_list(social_network, user):
    friends_list= []
    for i in social_network[user]:
        friend = i[0]
        friends_list.append(friend)
    return friends_list 

social_network = constructing_social_network(matrix_of_friendships)
print("Friends of " + str(user) + ': ' + str(get_friends_list(social_network, user)), '\n')


#Button For Viewing Friends

def button_get_friends_list(clicked):
    user = E1.get()
    filename = 'friendships.csv'
    matrix_of_friendships = readcsv(filename)
    social_network = constructing_social_network(matrix_of_friendships)
    res = get_friends_list(social_network, user)
    label = Label(F2, text = 'Friends of ' + user + ' = ' + str(res))
    label.pack()

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

def fixing_user_profile(profiles, user, age, country, department, hobbies):
    for i in range(len(profiles[user])):
        if profiles[user][i][0] == 'Age':
            profiles[user][i] = ('Age', str(age))
        elif profiles[user][i][0] == 'Country':
            profiles[user][i] = ('Country', country)
        elif profiles[user][i][0] == 'Department':
            profiles[user][i] = ('Department', department)
        elif profiles[user][i][0] == 'Hobbies':
            profiles[user][i] = ('Hobbies', hobbies)
    return profiles

filename = 'profiles.csv'
matrix_of_profiles = readcsv(filename)
profiles_temp = constructing_profiles(matrix_of_profiles)
profiles = fixing_user_profile(profiles_temp, user, age, country, department, hobbies)
print('Profiles: ')
print(profiles, '\n')



#Getting User's Profile

def get_user_profile(profiles, user):
    print('Profile of ' + user + ': ')
    for i in profiles[user]:
        print(i[0] + ': ' + i[1])

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
        for j in user_profile[1:]:
            if j in i_profile[1:]:
                counter = counter + 1
        age_difference = abs(int(user_profile[0]) - int(i_profile[0]))
        fixed_age_difference = age_difference//10
        new_cost = cost[i] - counter + fixed_age_difference
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

#GUI

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle

root = Tk()
root.title("MINI-FACEBOOK")
root.geometry('1300x1000')


Label(root, text="FriendsConnect", font=("Arial bold", 30), fg="black").pack()
F1= Frame(root,borderwidth=2, relief="solid")
F1.pack(side="left", expand=True, fill="both")
F2= Frame(root,borderwidth=2, relief="solid")
F2.pack(side="right", expand=True, fill="both")
# Label(F2, text="welcome", font=("Trebuchet",30)).grid(row=0,column=0)

Label(F1,text="Enter your Name:").grid(row=0,column=0)
E1= Entry(F1,bd=2)
E1.grid(row=0,column=1,padx=13,pady=10)

Label(F1,text="Enter your Age:").grid(row=1,column=0)
E2= Entry(F1,bd=2)
E2.grid(row=1,column=1,padx=13,pady=10)

Label(F1,text="Enter your Country:").grid(row=2,column=0)
E3= Entry(F1,bd=2)
E3.grid(row=2,column=1,padx=13,pady=10)

Label(F1,text="Enter your Hobbies:").grid(row=3,column=0)
E4= Entry(F1,bd=2)
E4.grid(row=3,column=1,padx=13,pady=10)

View_Friends=Button(F1, text='View My Friendlist', command="c", padx=13, pady=10)
View_Friends.grid(row=20,column=0,sticky=NSEW,padx=13,pady=10)
View_Friends.bind('<Button-1>', button_get_friends_list)

#Define a function to clear the Entry Widget Content
def clear_text():
   E1.delete(0, END), E2.delete(0, END), E3.delete(0, END), E4.delete(0, END)

#Create a button to clear the Entry Widget
clearButton = Button(F1,text="Clear", command=clear_text, font=('Helvetica bold',10))
clearButton.grid(row=21,column=0,sticky=NSEW,padx=13,pady=10)


root.mainloop()