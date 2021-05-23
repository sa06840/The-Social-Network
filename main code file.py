
# The Social Network

#Helper Functions

def get_profile_in_list(profiles, user):  #---> The get_profile_in_list function takes the profiles dictionary and a user's name as inputs.
    lst = []                              #     It then iterates through the user's profile and appends the user's information in a list while
    for i in profiles[user]:              #     ignoring the category of the information. It then outputs this list.
        elem = i[1].split(',')
        for j in elem:
            print(j.lstrip())
            lst.append(j.strip())
    return lst

def is_empty(lst):    #--> The is_empty function takes a list as an input and returns true if it is empty. If it is not empty, it returns False.
    if len(lst) == 0:
        return True
    else:
        return False

def get_neighbours(G, node):   #--> The get_neighbours functions take a graph(G) and a node as inputs. Since the graph is in the form of an
    neighbours = []            #    adjacency list, the function iterates through the node(user)'s adjacent nodes and appends them in a list.
    for i in G[node]:          #    This list which contains the adjacent nodes of the input node is then returned.
        neighbours.append(i)
    return neighbours

def get_cost(social_network, user):            #--> The get_cost function takes the social_network and user's name as inputs.
    cost = {}                                  #    It then runs Dijkstra's algorithm on the social_network with the user as the starting node
    unknown = []                               #    and calculates the mimimum cost of going from the user to every other person in the social_network.
    for node in social_network:                #    The cost of every person is stored in the cost dictionary in which the person's name is the key and their
        cost[node] = 100000                    #    cost from the user is the value. This cost dictionary is the returned.
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
    return cost

def case_sensitivity(name):          #--> The case_sensitivity makes sure that the code works despite the case used by the user in the input.
    lowered_name = name.lower()
    fixed_name = lowered_name.title()
    fixed_name = fixed_name.strip()
    return fixed_name

def user_not_in_socialnetwork(name):   #--> The user_not_in_socialnetwork function is called whenever the input name is not in the social_network.
    label = Label(F2, text = 'Sorry, the user that you are looking for is not in the social network.')
    label.pack()

def iserror(func, social_network, user, target_user):   #--> The is_error function is called in order to check if the get_user_connection function
    try:                                                #    returns an error or not.
        func(social_network, user, target_user)
        return False
    except Exception:
        return True


#Constructing Social Network

import csv
import random

def readcsv(filename):                      #--> The readcsv function takes the friendships.csv file as an input and returns an adjacency matrix
    matrix = []                             #    which displays the connections between the users.
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    return matrix

def constructing_social_network(matrix):   #--> The constructing_social_network function takes the adjacency matrix of the social_network
    social_network = {}                    #    as an input and converts it into an adjacency list. It then returns the social_network in the
    for i in matrix[0]:                    #    form of an adjacency list.
        if i != '':
            social_network[i] = []
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if int(matrix[i][j]) != 0:
                social_network[matrix[i][0]].append((matrix[0][j], int(matrix[i][j])))
    return social_network

filename = 'friendships.csv'
matrix_of_friendships = readcsv(filename)
social_network = constructing_social_network(matrix_of_friendships)


#Test Case

user = 'Shah Jamal Alam'          #--> This is a test case which acts as an input for the functions initially. You are free to alter it but do not delete it.
age = '35'
country = 'New Zealand'
department = 'Data Structures and Algorithms'
hobbies = 'Cooking, Snooker'


#Add a Friend

def add_friend(social_network, profiles, user, friend):       #--> The add_friend function takes the social_network, profiles dictionary, user's name and
    if get_friends_list(social_network, user) == []:          #    friend's name as inputs. It then adds the friend in the user's friend list and adds the user
        weight = random.randint(1,10)                         #    in the friend's friend list. The friend's cost from the user is also added for further use.
        social_network[user].append((friend, weight))         #    It then returns the updated social_network.
        social_network[friend].append((user, weight))
        return social_network
    cost_dictionary = get_cost(social_network, user)
    cost = cost_dictionary[friend]
    social_network[user].append((friend, cost))
    social_network[friend].append((user, cost))
    return social_network  



#Button for Adding a Friend

def button_addfirend(clicked):                                 #---> The button_addfriend function takes 2 input from the user, one is his name and   
    friend=E6.get()                                            #     other is the name of the friend which he wants to add to his friends list. 
    friend = case_sensitivity(friend)                          #     This is neccessary to understand for a user that he should type a name which is in the social network
    user=E1.get()                                              #     if friend will be already in users friend list it will return ' is already in you friend list'
    user = case_sensitivity(user)                              #     and if friend is not in the friend list but in the social network then this button will add the friend in users friend list    
    if friend not in social_network or user not in social_network:
        user_not_in_socialnetwork(friend)
        return
    elif friend in get_friends_list(social_network, user):
        res = friend + ' is already in your friendlist.'
        label = Label(F2, text = res)
        label.pack()
        return
    add_friend(social_network, profiles, user, friend)


#Remove a Friend

def unfriend(social_network,user,remove_friend):      #--> The unfriend function takes the social_network, user's name and friend's name as inputs.
    for i in social_network[user]:                    #    It then removes the friend from the user's friend list and removes the user from the friend's
        if remove_friend == i[0]:                     #    friend list. It then returns the updated social_network.
            social_network[user].remove(i)
    for j in social_network[remove_friend]:
        if user == j[0]:
            social_network[remove_friend].remove(j)
    return social_network



#Button for Removing a Friend                          

def button_unfriend(clicked):                         #---> The button_unfriend takes 2 input from user, one is for a friend to which he wants to remove from his freind list
    remove_friend = E6.get()                          #      and other for user to inout his name it is similar to add friend function in which frind must be in the sociakl network  
    remove_friend = case_sensitivity(remove_friend)   #      if friend is not in the list of users friend list then it will give ' is not in your friendlist.' 
    user = E1.get()                                   #      if it is in the list then simply it will remove it by calling unfriend function
    user = case_sensitivity(user)
    if remove_friend not in social_network or user not in social_network:
        user_not_in_socialnetwork(remove_friend)
        return
    elif remove_friend not in get_friends_list(social_network, user):
        res = remove_friend + ' is not in your friendlist.'
        label = Label(F2, text = res)
        label.pack()
        return
    unfriend(social_network, user, remove_friend)


#Getting Friends List

def get_friends_list(social_network, user):   #--> The get_friends_list function takes the social_network and user's name as inputs.
    friends_list= []                          #    It then iterates through the people that are connected to the user and appends their name
    for i in social_network[user]:            #    in a list. This list is then returned. 
        friend = i[0]
        friends_list.append(friend)
    return friends_list 

#Button For Viewing Friends

def button_get_friends_list(clicked):          #    The button_get_friends_list is taking input from user his name user should be in the social network, this functuion call the get_friends_list
    user = E1.get()                            #    function if the user have no friends so it will return 'You have no friends.' otherwise it will return the list of friends a user have in this social network.
    user = case_sensitivity(user)              #    below we have used features from tkinter and this function will display in the right hand side of the screen which is frame 2 
    if user not in social_network:
        user_not_in_socialnetwork(user)
        return
    res = get_friends_list(social_network, user)
    if res == []:
        label = Label(F2, text = 'You have no friends.')
        label.pack()
    else:
        my_listbox = Listbox(F2, width=50, height=20)
        my_listbox.pack(pady = 15)
        title = 'Friendlist of  ' + user + ': '
        my_listbox.insert(0, title)
        my_listbox.insert(1, '')
        for i in range(0, len(res)):
            ans = str(i+1) + '. ' + res[i]
            my_listbox.insert('end', ans)
        my_listbox.insert('end', '')
        my_listbox.insert('end', 'Total Friends = ' + str(i+1))


#Checking Mutual Friends

def get_mutual_friends(social_network, user1, user2):           #--> The get_mutual_friends function takes the social_network, user's name and another person's name
    mutual_friends = []                                         #    as inputs. It then iterates through both of their friend lists and appends the common ones in a new list.
    user1_friends = get_friends_list(social_network, user1)     #    This list of mutual friends is then returned.
    for i in social_network[user2]:
        if i[0] in user1_friends:
            mutual_friends.append(i[0])
    return mutual_friends



#Button for Getting Mutual Friends

def button_get_mutual_friends(clicked):                          #--. This button_get_mutual_function is taking two input one for user it self and anyother person in the social network
    user1 = E1.get()                                             #    both the user must be in the social network if not then add them in to social network then this button function calls the get_mutual_friends function
    user1 = case_sensitivity(user1)                              #    if both the user dont have any common friend then it will return on the right hand side of the screen that you and user2 dont have any mutual friends
    user2 = E6.get()                                             #    if they have any mutual friend then it will give the list for mutual friend on the right hand side by clicking mutual friends button 
    user2 = case_sensitivity(user2)
    if user2 not in social_network or user1 not in social_network:
        user_not_in_socialnetwork(user2)
        return
    res = get_mutual_friends(social_network, user1, user2)
    if res == []:
        res = 'You and ' + user2 + ' do not have any mutual friends.'
        label = Label(F2, text = res)
        label.pack()
        return
    my_listbox = Listbox(F2, width=50, height=20)
    my_listbox.pack(pady = 15)
    title = 'Mutual Friends of  ' + user1 + ' and ' + user2 + ': '
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for i in range(0, len(res)):
        ans = str(i+1) + '. ' + res[i]
        my_listbox.insert('end', ans)
    my_listbox.insert('end', '')
    my_listbox.insert('end', 'Total Mutual Friends = ' + str(i+1))


#Constructing User Profiles

def readcsv(filename):                   #--> The readcsv file function takes the profiles.csv file as an input and converts it into an adjacecny
    matrix = []                          #    matrix which contains the profile of every user. This matrix is then returned.
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(row)
    return matrix

def constructing_profiles(matrix):                                      #--> The constructing_profiles function takes the profiles adjacency matrix as an input and converts it into a dictionary
    profiles = {}                                                       #    which consists of the profiles of every user. This profiles dictionary is then returned.
    for i in range(1, len(matrix[0])):
        for j in range(1, len(matrix)):
            if not(matrix[0][i] in profiles):
                profiles[matrix[0][i]] = [(matrix[j][0], matrix[j][i])]
            else:
                profiles[matrix[0][i]].append((matrix[j][0], matrix[j][i]))
    return profiles

def fixing_user_profile(profiles, user, age, country, department, hobbies):                                        #--> The fixing_user_profile function takes the profiles dictionary and the user's information as inputs.
    if user not in profiles:                                                                                       #    It then uses this information to update and save the user's profile. If the user is not in the social_network,
        profiles[user] = [('Age', age), ('Country', country), ('Department', department), ('Hobbies', hobbies)]    #    it adds the user to the social_network and creates a profile for them using the information provided by the user.
        social_network[user] = []                                                                                  #    This profile is then added to the profiles dictionary. The updated profiles dictionary is then returned.
    else:
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



#Button for saving profile

def save_user_profile(clicked):
    user = E1.get()
    user = case_sensitivity(user)
    if user == '':
        label = Label(F2, text = 'Please enter your name.')
        label.pack()
        return
    age = E2.get()
    if '-' in age:
        label = Label(F2, text = 'Please enter a valid age.')
        label.pack()
        return
    elif age.isdigit() == False and age != '':
        label = Label(F2, text = 'Please enter a number for your age.')
        label.pack()
        return
    age = case_sensitivity(age)
    country = E3.get()
    country = case_sensitivity(country)
    department = E4.get()
    department = case_sensitivity(department)
    hobbies = E5.get()
    hobbies = case_sensitivity(hobbies)
    profiles = fixing_user_profile(profiles_temp, user, age, country, department, hobbies)


#Getting Profile

def get_user_profile(profiles, user):     #--> The get_user_profile function takes the profiles dictionary and user's name as inputs.
    print('Profile of ' + user + ': ')    #    It then iterates through the user's profile and prints their information. This function is not used in the GUI.
    for i in profiles[user]:              #    We have kept it if the user wants the output in the terminal.
        print(i[0] + ': ' + i[1])



#Button for getting user's profile
# The button_get_user_profile function takes the user's name and the friend's name as inputs. This friend can be any person in 
# the social_network. 
# If the user is not in the social_network, it calls the user_not_in_socialnetwork function and terminates. If the user is in the social_network 
# and they have not inputted a friend's name, the user's profile is displayed. However, if they have inputted a friend's name, 
# the friend's profile is displayed as long as they are in the social_network. 
# If the friend is not in the social_network, the user_not_in_socialnetwork function is called and the function terminates.
#   ^^   ^^
#   ||   ||   
#   ||   || 
def button_get_user_profile(clicked):      
    user = E1.get()
    user = case_sensitivity(user)
    if user not in social_network:
        user_not_in_socialnetwork(user)
        return
    friend = E6.get()
    friend = case_sensitivity(friend)
    if friend:
        if friend not in social_network:
            user_not_in_socialnetwork(friend)
            return
        else:
            res = profiles[friend]
            title = 'Profile of ' + friend + ': '
            my_listbox = Listbox(F2, width=50)
            my_listbox.pack(pady = 15)
            my_listbox.insert(0, title)
            my_listbox.insert(1, '')
            for item in res:
                ans = item[0] + ' = ' + item[1]
                my_listbox.insert('end', ans)
    else:
        res = profiles[user]
        title = 'Profile of ' + user + ': '
        my_listbox = Listbox(F2, width=50)
        my_listbox.pack(pady = 15)
        my_listbox.insert(0, title)
        my_listbox.insert(1, '')
        for item in res:
            ans = item[0] + ' = ' + item[1]
            my_listbox.insert('end', ans)
    

#Recommending Friends

def get_recommended_friends(social_network, profiles, user):     #--> The get_recommended_friends function takes the social_network, profiles dictionary and user's name as an input. It then
    cost = {}                                                    #    runs Dijkstra's algorithm on the social_network graph with the user as the starting node and finds the minimum cost from
    unknown = []                                                 #    the user to every other person in the social_network. It then adds this minimum cost to the cost dictionary in which the person's name
    recommended_friends = []                                     #    is the key and the value is the minimum cost. After this the function calculates the similarities between the user's profile and the profile
    for node in social_network:                                  #    of every other person in the social_network. It subtracts this similarity from the cost of the respective person and updates the cost
        cost[node] = 100000                                      #    dictionary accordingly. This function then iterates through this dictionary and appends those people (along with their cost)
        unknown.append(node)                                     #    who are not in the user's friend list (does not append the user), in the recommended friends list. This recommended friends list is then sorted
    cost[user] = 0                                               #    on the basis of the cost and returned. The most recommdend person comes first whereas the least recommended person comes last.
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
        fixed_age_difference = 0                                              # The four next lines of code ensure that the age difference between the user and every other person in the social network
        if user_profile[0] != '':                                             #  is also taken into account while recommending friends.
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
    return recommended_friends



# Button for getting recommended friends

def button_for_recommended_friends(clicked):            # The button_for_recommended_friends takes the input from user as his name which must be in the social network 
    user=E1.get()                                       # and calls the function get_recommended_friends which return the recommended friends in the the listbox widget
    user = case_sensitivity(user)
    if user not in social_network:
        user_not_in_socialnetwork(user)
        return
    res=get_recommended_friends(social_network, profiles, user)
    my_listbox = Listbox(F2, width=50, height = 20)
    my_listbox.pack(pady = 15)
    title = 'Recommended Friends for ' + user + ': '
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for i in range(len(res)):                           # The for loop here will give us the recommended friends in each seperate line
        ans = str(i+1) + '. ' + res[i][0]
        my_listbox.insert('end', ans)


#User's Connection

def get_users_connection(social_network, user, target_user):    #--> The get_users_connection function takes the social_network, user's name and target user's name as inputs.
    cost = {}                                                   #    It then runs Dijkstra's algorithm on the social_network graph with the user as the starting node and target_user
    unknown = []                                                #    as the end node. By calculating the cost of every person from the user, storing them in a dictionary, keeping a record
    path = []                                                   #    of the parent nodes and back-tracking, this function returns the shortest path from the user to the target_user.
    parent = {}                                                 #    This tells the user how they are connected to a specific person in the social_network.
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



#Button for user connection

def button_get_users_connection(clicked):       # It is taking inouts for user itself to type his name and the target user to which he wants a connection target and user must be in social network
    user = E1.get()                             # We add the extra information by telling if there is an error in get connection then there is no connection between user and target user
    user = case_sensitivity(user)               # if there is, then it will give in the listbox in right hand side.
    target_user = E6.get()
    target_user = case_sensitivity(target_user)
    if target_user not in social_network or user not in social_network:
        user_not_in_socialnetwork(target_user)
        return
    if iserror(get_users_connection, social_network, user, target_user):
        label = Label(F2, text = 'There is no connection between ' + user + ' and ' + target_user + '.')
        label.pack()
        return
    res = get_users_connection(social_network, user, target_user)
    my_listbox = Listbox(F2, width=50, height=20)
    my_listbox.pack(pady = 15)
    title = 'Path from ' + user + ' to  ' + target_user
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for i in range(len(res)):
        ans = str(i+1) + '. ' + res[i][0]           #these things add to return the connection in seperate line with each given the connection with user
        my_listbox.insert('end', ans)
        my_listbox.insert('end', '              |')
        my_listbox.insert('end', '             V')
    last = str(i+2) + '. ' + target_user
    my_listbox.insert('end', last)

# GUI Implementations 

from tkinter import *   
import tkinter.messagebox
from tkinter import ttk
import pickle

root = Tk()           # this will create a window and between this and main loop we have to work for GUI
root.title("TSN")
root.geometry('1920x1080')

# Functions for Clearing Window

def ClearInfo():      # Clears the output shown on Frame 2
    for widget in F2.winfo_children():
        widget.destroy()
        
def clear_text():
   E1.delete(0, END), E2.delete(0, END), E3.delete(0, END), E4.delete(0, END), E5.delete(0, END), E6.delete(0, END) # Clears the names which user added 
  
# Displays the image shown "the social network"
canvas1 = Canvas( root, width = 20, height = 20)    
b = PhotoImage(file = "tsn.png")                   
canvas1.create_image( 0, 0, image = b)
Label(root, image=b, width='2000', height='115', bg='#405898').pack()

# Frames
F1= Frame(root,borderwidth=2, relief='sunken', bg='#405898', bd='10') # Frame 1: left hand side for user to input and buttons displayed
F1.pack(side="left", expand=True, fill="both")
F2= Frame(root,borderwidth=2, relief="sunken", bg='#405898', bd='20') # Frame 2: right hand side uses to display the output 
F2.pack(side="right", expand=True, fill="both")

# ALL THE BUTTONS IMPLEMENTED
# Note that here if you see row and column equal to some number that is the number for each row and column like where selected item will be represented in the frame

#Entry 1: Name
Label(F1,text="Enter your Name:", bg='#405898', bd='3', font=('calibri bold', 15), fg='white').grid(row=0, sticky=W,padx=10)#--> use to tell the use to input his name
E1= Entry(F1,bd=2)                    #--> create an Entry for user to write his name 
E1.grid(row=0,column=1,padx=5,pady=12)

#Entry 2: Age
Label(F1,text="Enter your Age:", bg='#405898', bd='3', font=('calibri bold', 15), fg='white').grid(row=1,sticky=W, padx=10)#--> use to tell the user to input his age
E2= Entry(F1,bd=2)      #--> create an Entry for user to write his age
E2.grid(row=1,column=1,padx=13,pady=12)

#Entry 3: Country
Label(F1,text="Enter your Country:", bg=('#405898'), bd='3', font=('calibri bold', 15), fg='white').grid(row=2,sticky=W, padx=10)#--> use to tell the user to input his country
E3= Entry(F1,bd=2)        #--> create an Entry for user to write his country
E3.grid(row=2,column=1,padx=13,pady=12)

#Entry 4: Department
Label(F1,text="Enter your Department:", bg='#405898', bd='3', font=('calibri bold', 15), fg='white', anchor='center').grid(row=3,sticky=W, padx=10)#--> use to tell the user to input his department
E4= Entry(F1,bd=2)      #--> create an Entry for user to write his department
E4.grid(row=3,column=1,padx=13,pady=12)

#Entry 5: Hobbies
Label(F1,text="Enter your Hobbies:", bg='#405898', bd='3', font=('calibri bold', 15), fg='white').grid(row=4,sticky=W, padx=10)#--> use to tell the user to input his hobbies
E5= Entry(F1,bd=2)           #--> create an Entry for user to write his hobbies
E5.grid(row=4,column=1,padx=13,pady=12)

#Entry 6: Friend's Name
Label(F1, text="Enter your friend name's:", bg='#405898', bd='3', font=('calibri bold', 15), fg='white').grid(row=40, sticky=W, padx=10)#--> use to tell the user to input his freind name
E6=Entry(F1,bd=2)          #--> create an Entry for user to write his friend name
E6.grid(row=40,column=1,padx=13,pady=12)

# View Friendlist button                                   
View_Friends=Button(F1, text='View My Friendlist', command="c", padx=13, pady=10, activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
View_Friends.grid(row=60,column=0,sticky=NSEW,padx=13,pady=10)  #these three lines create the button in frame 1 which is left hand side of the screen and from where when user click the button it will diplay the output for that particular function
View_Friends.bind('<Button-1>', button_get_friends_list)

# Clear the entered data button
clearButton = Button(F1,text="Clear Entry Data", command=clear_text, padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
clearButton.grid(row=100,column=1,sticky=NSEW,padx=13,pady=10) # simillarly creating a button for clear enrty

# Clear the information on the right button
Clear=Button(F1, text='Clear', command=ClearInfo, padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2, height=1, width=1)
Clear.grid(row=100,column=0,sticky=NSEW,padx=13,pady=10) #again creating button for clear information

# Save a profile button
Save_Profile=Button(F1, text='Save Profile', command="c", padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
Save_Profile.grid(row=60,column=1,sticky=NSEW,padx=13,pady=10) # these 3 line for crearting button for save profile in which we call here save_user_profile function which will display when user click it
Save_Profile.bind('<Button-1>', save_user_profile)

# View a profile button
View_Profile=Button(F1, text='View Profile', command="c", padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
View_Profile.grid(row=80,column=1,sticky=NSEW,padx=13,pady=10) # button for view profile when user click it then the code display the output of the function which we have called here
View_Profile.bind('<Button-1>', button_get_user_profile)

# Friend recommendation button
View_recommended_friends=Button(F1, text='Recommended Friends', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
View_recommended_friends.grid(row=80,column=0,sticky=NSEW,padx=13,pady=10) #simillarly here creating a button and calling it 
View_recommended_friends.bind('<Button-1>', button_for_recommended_friends)

# Add a friend button
Add_friend=Button(F1, text='Add Friend', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
Add_friend.grid(row=40,column=2,sticky=NSEW,padx=10,pady=10) #we have create 10 buttons and almost in every button we use simillar technique except calling a different function in every button 
Add_friend.bind('<Button-1>', button_addfirend)

# Unfriend button 
Unfriend=Button(F1, text='Unfriend', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#8B0000', fg='white', font=('calibri bold', 15), bd=2, width=10)
Unfriend.grid(row=60,column=2,sticky=NSEW,padx=10,pady=10,)
Unfriend.bind('<Button-1>', button_unfriend)

# Mutual Friends button
View_Mutual_Friends=Button(F1, text='Mutual Friends', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
View_Mutual_Friends.grid(row=80,column=2,sticky=NSEW,padx=13,pady=10)
View_Mutual_Friends.bind('<Button-1>', button_get_mutual_friends)

# User's connection button
View_Users_Connection=Button(F1, text="User's Connection", command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#778899', fg='white', font=('calibri bold', 15), bd=2)
View_Users_Connection.grid(row=100,column=2,sticky=NSEW,padx=13,pady=10)
View_Users_Connection.bind('<Button-1>', button_get_users_connection)

root.mainloop() # Keeps the GUI running