
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

def case_sensitivity(name):
    lowered_name = name.lower()
    fixed_name = lowered_name.title()
    return fixed_name

#Constructing Social Network

import csv
from os import remove

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
social_network = constructing_social_network(matrix_of_friendships)



#User

user = 'Shah Jamal Alam'
age = '35'
country = 'New Zealand'
department = 'Data Structures and Algorithms'
hobbies = 'Cooking, Snooker'


#Add a Friend

def add_friend(social_network, profiles, user, friend):
    cost_dictionary = get_cost(social_network, profiles, user)
    cost = cost_dictionary[friend]
    social_network[user].append((friend, cost))
    return social_network  


#friend = 'Sajal Rana'
#print('Social Network: ')
#print(add_friend(social_network, profiles, user, friend), '\n')


#Button for Adding a Friend

def button_addfirend(clicked):
    friend=E6.get()
    friend=case_sensitivity(friend)
    user=E1.get()
    user=case_sensitivity(user)
    add_friend(social_network, profiles, user, friend)



#Remove a Friend

def unfriend(social_network,user,remove_friend):
    for i in social_network[user]:
        if remove_friend == i[0]:
            social_network[user].remove(i)
    return social_network

#remove_friend = 'Waqar Saleem'
#print('Social Network: ')
#print(unfriend(social_network, user, remove_friend))


#Button for Removing a Friend

def button_unfriend(clicked):
    remove_friend=E6.get()
    remove_friend=case_sensitivity(remove_friend)
    user =E1.get()
    user=case_sensitivity(user)
    unfriend(social_network,user,remove_friend)
    # remove_friend = E6.get()
    # user = E1.get()
    # unfriend(social_network, user, remove_friend)



#Checking Friends List


def get_friends_list(social_network, user):
    friends_list= []
    for i in social_network[user]:
        friend = i[0]
        friends_list.append(friend)
    return friends_list 

#social_network = constructing_social_network(matrix_of_friendships)
#print("Friends of " + str(user) + ': ' + str(get_friends_list(social_network, user)), '\n')


#Button For Viewing Friends

def button_get_friends_list(clicked):
    user = E1.get()
    user=case_sensitivity(user)
    #filename = 'friendships.csv'
    #matrix_of_friendships = readcsv(filename)
    #social_network = constructing_social_network(matrix_of_friendships)
    res = get_friends_list(social_network, user)
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

def get_mutual_friends(social_network, user1, user2):
    mutual_friends = []
    user1_friends = get_friends_list(social_network, user1)
    for i in social_network[user2]:
        if i[0] in user1_friends:
            mutual_friends.append(i[0])
    return mutual_friends

user2 = 'Waqar Saleem'
print('Mutual Friends of ' + str(user) + ' and ' + str(user2) + ': ' + str(get_mutual_friends(social_network, user, user2)), '\n')

#Button for Getting Mutual Friends

def button_get_mutual_friends(clicked):
    user1 = E1.get()
    user1=case_sensitivity(user1)
    user2 = E6.get()
    user2=case_sensitivity(user2)
    res = get_mutual_friends(social_network, user1, user2)
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
print('Profiles: oqba')
print(profiles, '\n')


#Button for saving profile

def save_user_profile(clicked):
    user = E1.get()
    user=case_sensitivity(user)
    age = E2.get()
    age=case_sensitivity(age)
    country = E3.get()
    country=case_sensitivity(country)
    department = E4.get()
    department=case_sensitivity(department)
    hobbies = E5.get()
    hobbies=case_sensitivity(hobbies)
    profiles = fixing_user_profile(profiles_temp, user, age, country, department, hobbies)
    #res = profiles[user]
    #my_listbox = Listbox(F2, width=50)
    #my_listbox.pack(pady = 15)
    #title = 'Profile of ' + user + ': '
    #my_listbox.insert(0, title)
    #my_listbox.insert(1, '')
    #for item in res:
        #ans = item[0] + ' = ' + item[1]
        #my_listbox.insert('end', ans)


#Getting Profile

def get_user_profile(profiles, user):
    print('Profile of ' + user + ': ')
    for i in profiles[user]:
        print(i[0] + ': ' + i[1])

get_user_profile(profiles, user)
print('\n')


#Button for getting user's profile

def button_get_user_profile(clicked):
    user = E1.get()
    user=case_sensitivity(user)
    res = profiles[user]
    my_listbox = Listbox(F2, width=50)
    my_listbox.pack(pady = 15)
    title = 'Profile of ' + user + ': '
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for item in res:
        ans = item[0] + ' = ' + item[1]
        my_listbox.insert('end', ans)
    


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
    return recommended_friends


print(get_friends_list(social_network, 'Shah Jamal Alam'))
print('Recommended Friends for ' + str(user) + ': ')
get_recommended_friends(social_network, profiles, user)
print('\n')


# Button for getting recommended friends

def button_for_recommended_friends(clicked):
    user=E1.get()
    user=case_sensitivity(user)
    #filename = 'friendships.csv'
    #matrix_of_friendships = readcsv(filename)
    #social_network = constructing_social_network(matrix_of_friendships)
    #profiles = fixing_user_profile(profiles_temp, user, age, country, department, hobbies)
    res=get_recommended_friends(social_network, profiles, user)
    my_listbox = Listbox(F2, width=50)
    my_listbox.pack(pady = 15)
    title = 'Recommended Friends for ' + user + ': '
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for i in range(len(res)):
        ans = str(i+1) + '. ' + res[i][0]
        my_listbox.insert('end', ans)



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

# button for user connection

def button_get_users_connection(clicked):
    user = E1.get()
    user=case_sensitivity(user)
    target_user = E6.get()
    target_user=case_sensitivity(target_user)
    res = get_users_connection(social_network, user, target_user)
    my_listbox = Listbox(F2, width=50)
    my_listbox.pack(pady = 15)
    title = 'Path from ' + user + ' to  ' + target_user
    my_listbox.insert(0, title)
    my_listbox.insert(1, '')
    for i in range(len(res)):
        ans = str(i+1) + '. ' + res[i][0]
        my_listbox.insert('end', ans)
    last = str(i+2) + '. ' + target_user
    my_listbox.insert('end', last)




from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle

# from PIL import ImageTk,Image  


#GUI

root = Tk()
root.title("MINI-FACEBOOK")
root.geometry('1300x1000')
# root.configure(bg='')


#Button for Clearing Window

def ClearInfo():
    for widget in F2.winfo_children():
        widget.destroy()
def clear_text():
   E1.delete(0, END), E2.delete(0, END), E3.delete(0, END), E4.delete(0, END), E5.delete(0, END), E6.delete(0, END)

# Label(root, text="FriendsConnect", font=("Arial bold", 30), fg="black").pack()
b = PhotoImage(file = "socialnetwork1.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 20, height = 20)
  
# Display image
canvas1.create_image( 0, 0, image = b)
Label(root, image=b, width='2000', height='125', bg='#405898').pack()
F1= Frame(root,borderwidth=2, relief='sunken', bg='#405898', bd='10')
F1.pack(side="left", expand=True, fill="both")
F2= Frame(root,borderwidth=2, relief="sunken", bg='#405898', bd='10')
F2.pack(side="right", expand=True, fill="both")

# Label(F1,text="Enter your Name", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=0,column=0)
Label(F1,text="Enter your Name", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=0, sticky=W,padx=10)

E1= Entry(F1,bd=2)
E1.grid(row=0,column=1,padx=5,pady=12)



# Label(F1,text="Enter your Age", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=1,column=0)
Label(F1,text="Enter your Age", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=1,sticky=W, padx=10)

E2= Entry(F1,bd=2)
E2.grid(row=1,column=1,padx=13,pady=12)

# Label(F1,text="Enter your Country", bg=('white'), bd='3', font=('calibri bold', 15), fg='Black').grid(row=2,column=0)
Label(F1,text="Enter your Country", bg=('white'), bd='3', font=('calibri bold', 15), fg='Black').grid(row=2,sticky=W, padx=10)

E3= Entry(F1,bd=2)
E3.grid(row=2,column=1,padx=13,pady=12)

# Label(F1,text="Enter your Department", bg='white', bd='3', font=('calibri bold', 15), fg='Black', anchor='center').grid(row=3,column=0)
Label(F1,text="Enter your Department", bg='white', bd='3', font=('calibri bold', 15), fg='Black', anchor='center').grid(row=3,sticky=W, padx=10)

E4= Entry(F1,bd=2)
E4.grid(row=3,column=1,padx=13,pady=12)

# Label(F1,text="Enter your Hobbies", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=4,column=0)
Label(F1,text="Enter your Hobbies", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=4,sticky=W, padx=10)

E5= Entry(F1,bd=2)
E5.grid(row=4,column=1,padx=13,pady=12)

# Label(F1, text="Enter your friend name's", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=40, column=0)
Label(F1, text="Enter your friend name's", bg='white', bd='3', font=('calibri bold', 15), fg='Black').grid(row=40, sticky=W, padx=10)

E6=Entry(F1,bd=5)
E6.grid(row=40,column=1,padx=13,pady=12)

View_Friends=Button(F1, text='View My Friendlist', command="c", padx=13, pady=10, activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
View_Friends.grid(row=60,column=0,sticky=NSEW,padx=13,pady=10)
View_Friends.bind('<Button-1>', button_get_friends_list)

clearButton = Button(F1,text="Clear Entry Data", command=clear_text, padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
clearButton.grid(row=100,column=1,sticky=NSEW,padx=13,pady=10)

Clear=Button(F1, text='Clear', command=ClearInfo, padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2, height=1, width=1)
Clear.grid(row=100,column=0,sticky=NSEW,padx=13,pady=10)

Save_Profile=Button(F1, text='Save Profile', command="c", padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
Save_Profile.grid(row=60,column=1,sticky=NSEW,padx=13,pady=10)
Save_Profile.bind('<Button-1>', save_user_profile)

View_Profile=Button(F1, text='View Profile', command="c", padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
View_Profile.grid(row=60,column=2,sticky=NSEW,padx=13,pady=10)
View_Profile.bind('<Button-1>', button_get_user_profile)

View_recommended_friends=Button(F1, text='Recommended Friends', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
View_recommended_friends.grid(row=80,column=0,sticky=NSEW,padx=13,pady=10)
View_recommended_friends.bind('<Button-1>', button_for_recommended_friends)

Add_friend=Button(F1, text='Add Friend', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
Add_friend.grid(row=40,column=2,sticky=NSEW,padx=10,pady=10)
Add_friend.bind('<Button-1>', button_addfirend)

Unfriend=Button(F1, text='Unfriend', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='#8B0000', fg='white', font=('calibri bold', 15), bd=2, width=10)
# Unfriend.grid(row=100,column=2,sticky=NSEW,padx=13,pady=10)
Unfriend.grid(row=40,column=3,sticky=NSEW,padx=10,pady=10,)

Unfriend.bind('<Button-1>', button_unfriend)

View_Mutual_Friends=Button(F1, text='Mutual Friends', command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
View_Mutual_Friends.grid(row=80,column=1,sticky=NSEW,padx=13,pady=10)
View_Mutual_Friends.bind('<Button-1>', button_get_mutual_friends)

View_Users_Connection=Button(F1, text="User's Connection", command='c', padx=13, pady=10,  activebackground='light blue', activeforeground='red', bg='green', fg='white', font=('calibri bold', 15), bd=2)
View_Users_Connection.grid(row=80,column=2,sticky=NSEW,padx=13,pady=10)
View_Users_Connection.bind('<Button-1>', button_get_users_connection)
# root.tk.call('tk', 'scaling', 1.0)
root.mainloop()

