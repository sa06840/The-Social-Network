# The Social Network

![Project Image](https://fanart.tv/fanart/movies/37799/hdmovielogo/the-social-network-503d2d7f8e7c1.png)

> This is a ReadMe file to help save you time and effort.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How to save the program](#How-to-save-the-program)
- [How To Use](#how-to-use)
- [How to run the file](#how-to-run-the-file)
- [References](#references)
- [Author Info](#author-info)

---

## Description

This program allows the user to discover new people from all across the globe and make new virtual friends. It uses multiple features of data structures ranging from dictionaries and adjacency lists to djikstra’s algorithm in order to ensure efficient storage of data and the smooth operation of all the features. 

We have added two csv files in the repository which act as the basic input for the program. They are named ‘friendships.csv’ and ‘profiles.csv’. The ‘friendships.csv’ file consists of the connections between 15 users. The weight of these friendships is rated from 1 to10 where 1 is the strongest friendship possible. If the weight between two users is 0 then they are not friends. This file is then used to create a social network in the form of an adjacency list. Moreover, the ‘profiles.csv’ consists of the information of the profile of every user in the social network. A profile includes information such as the user’s age, country of origin, department of work and hobbies. This file is then used to create a dictionary in which the keys are the users’ names and the values are lists of tuples that store the respective user’s information. 

Now that our social network is made and every user’s profile is saved, we come to the functions which allow the user to alter their friendships and get advice from the program while doing so. The user will first view their default profile and if they wish to change it, they can do so by adding their information and saving. Then they can view their friends list in order to get an idea of whom they are associated with. The program allows the user to view the profiles of their friends and if they find someone whom they want to unfriend, it can be done easily. This will also remove the user from that specific friend’s friends list. The user can also check their mutual friends with another person in the group. Moreover, if the user wants to add more friends, they can do so directly or if they want to make an informed decision, they can ask the program for a list of recommended people to befriend. This list is sorted where the person at position 1 is the most recommended. The recommendation takes place on the basis of mutual friends and how similar the features of the profiles (age, country, department, hobbies). The person with a profile that is the most similar to the user’s profile will be at the top of the recommended list. In order to make an even more informed decision, the user can view the profiles of the people in the list and can also get to know the path of friends which connects them to that person. Once satisfied with their choice, the user can add that person to their friend list. By doing so, the user will also be added to that person’s friend list.

In order to make this program more accessible and global, we ensured that even random user who is not present in the input csv files can be a part of this social network. However, just like any other social network, they must first create and save their profile which will add them to the network. Then they can start off by asking the program to recommend some users to befriend. The same process will be applied as described earlier. Since the user is now a part of the social network, they can use all of its features.
Just to clarify, all the features can be used at any time. There is no specific, fixed order for their use. If an invalid action is performed, the program will give an informative output e.g. unfriending a person who is not in the user’s friend list will result in an output saying “(user’s name) is not in your friend list.”.

The inputs from the user are taken in the GUI, they are then used in the backend code and the output is displayed on the right side of the GUI. If it gets too cluttered, you can use the ‘Clear’ button to clear space.

#### Technologies Used:

- Data Structures 
- Python 3
- Tkinter
- Visual Code Studio
- Djikstra's Algorithm 



[Back To The Top](#The-Social-Network)


---

## How to save the program

While saving the files from the repository, make sure that the following files are saved in the same folder:
-	friendships.csv
-	profiles.csv
-	main code file.py
-	tsn.png

[Back To The Top](#The-Social-Network)

---

## How To Use
You must also have tkinter installed in your device in order to display the GUI.

#### Installation

Import Tkinter to use the GUI.

#### API Reference

```python
    from Tkinter import *
```
[Back To The Top](#The-Social-Network)

---
## How to run the file

After saving the files mentioned above in one folder, open this folder in your python editor e.g. VScode, pycharm, sublime text etc. Then open the ‘main code file.py’, and run it. A new window will pop up which acts as the interface for the program. You can type in your inputs in the textboxes and press the required button for the desired output.

#### Functionality of the buttons:
-	Save Profile: Takes the user’s information as an input and updates their profile. If the user is not in the social network then it will create a new profile for them.
-	View Profile: Displays the profile of the user.
-	View My Friendlist: Displays the user’s friend list.
-	Add Friend: Takes the user’s name and the person’s name as inputs and adds that person to the user’s friend list.
-	Unfriend: Takes the user’s name and the person’s name as inputs and removes that person from the user’s friend list.
-	Recommended Friends: Displays the list of users that are recommended to the user to befriend.
-	Mutual Friends: Takes the user’s name and the person’s name as inputs and displays the mutual friends of the user with that person. 
-	User’s Connection: Takes the user’s name and the person’s name as inputs and displays the shortest path of friends from the user to that person. 
-	Clear: Clears the output window.
-	Clear Entry Data: Clears all the text boxes which take the inputs.


In order to get any information related to another person in the social network or in order to add/delete a person from the user’s friend list, the user must first type out their own name in the ‘Enter your name’ input box and then type out the person’s name in the ‘Enter your friend’s name’ text box before pressing the desired button.

[Back To The Top](#The-Social-Network)

---

## References
We implemented the GUI by watching the following Tutorial:

Tkinter Tutorial -  https://youtu.be/YXPyB4XeYLA

[Back To The Top](#The-Social-Network)

---

## Conrtributors 

- Sajeel Alam - [sa06840](https://github.com/sa06840)
- Zaviar Khan - [Zav06838](https://github.com/Zav06838)
- Oqba Jawed - [oqba06878](https://github.com/oqba06878)
- Musab Sattar - [musabsattar70](https://github.com/musabsattar70)

[Back To The Top](#The-Social-Network)

