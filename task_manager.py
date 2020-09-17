# Everything works but I accidentally deleted everything in the tasks.txt file though :( 
# Import datetime for when the admin adds a task and needs to input a start & due date
import datetime

# Open both files (opened both as read only for now, will be opened as append or write when need be)
user_file = open('user.txt','r')
tasks_file = open('tasks.txt','r')

# This menu is only available to the admin. It allows the admin to register a user and display statistics
# Defined it as a function that will be called on later (two seperate menus were made so the user doesn't have all the options)
def adminMenu():
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("ds - display statistics")
    print("e - exit")
    print("\n")

# Depending on what the admin chooses to do it will call on a function that has been defined below. Also display a message when action completed
    ans=input("What would you like to do? ")
            
    if ans=="r":
        print("\n")
        register()
        print("\n")
        print("Thank you, you have successfully registered a user")
                                      
    elif ans=="a":
        print("\n")
        add_task()
        print("\n")
        print("Thank you, you have successfully added a task")
                
    elif ans=="va":
        print("\n")
        view_all_tasks()
        print("\n")
        print("These are all the tasks in the file")
                                     
    elif ans=="vm":
        print("\n")
        view_my_tasks()
        print("\n")
        print("These are all of the tasks assigned to you")

    elif ans=="ds":
        print("\n")
        display_statistics()
        print("\n")
        print("Statistic display complete")
                                     
    elif ans == "e":
        print("\n")
        print("Goodbye!")
        quit()


# Only a registered user can access this menu. It does not allow them to register a user or see task/ user statistics 
def userMenu():
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    print("\n")
    
    ans=input("What would you like to do? ")

    if ans=="a":
        print("\n")
        add_task()
        print("\n")
        print("Thank you, you have successfully added a task")
        
    elif ans=="va":
        print("\n")
        view_all_tasks()
        print("\n")
        print("These are all the tasks in the file")
        
                
    elif ans=="vm":
        print("\n")
        view_my_tasks()
        print("\n")
        print("These are all of the tasks assigned to you")              
                      
    elif ans == "e":
        print("\n")
        print("Goodbye!")
        quit()
        

# This function allows the admin to register a user. Open file using 'a' for append so it does not write over any users already in the file
# Asks admin for the usermane and password. Will only register a user if the password and password confirmation match
# using write() to put this information into the txt file (always close fie after) and .format so it printes neatly
def register():
    user_file = open('user.txt','a')
    username = input("Please enter a new username: ")
    password = input("Please enter your new password: ")
    confirm_password = input("Please confirm your new password: ")
    if password == confirm_password:
        user_file.write("\n{}, {}".format(username, password))
        user_file.close()
    else:
        print("Could not register - passwords do not match!")


# This function allows the admin or user to add a task. Open file using 'a' for append so it does not write over any users already in the file
# Asks for all information about the task then writes them to the txt file using write()
def add_task():
    task_file = open('tasks.txt','a')
    username = input("Please enter the username the task is assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please eneter a description of the task: ")
    task_start = input("Please enter the date that this task was assigned: ")
    task_due = input("Please enter the due date of this task: ")
    task_completed = input("Please specifiy if the task has been completed by putting either 'Yes' or 'No': ")
    task_file.write("\n{}, {}, {}, {}, {}, {}" .format(username, task_title, task_description, task_start, task_due, task_completed))                              
    task_file.close()
                          
# This function allows all the contents of the task file to be printed out. Use 'r' as it is only being read 
def view_all_tasks():
    task_file = open('tasks.txt','r')
    content = task_file.read()
    print(content)
    task_file.close()
    
# This function searches for the username in everyline and only prints the lines that the username is found in
def view_my_tasks():
    task_file = open('tasks.txt','r')
    for line in task_file.readlines(): 
        if username in line:
            print(line)
    task_file.close()
    
# this funcion lets the admin see how many tasks and users there are. It does this by opening both files as read only
# then by splittiing the lines by the new line operator and adding one to the specified counter number everytime a new line is read
def display_statistics():
    task_file = open('tasks.txt','r')
    user_file = open('user.txt','r')
    task_counter = 0
    user_counter = 0
    data = line.split('\n')

    for data in task_file:
        task_counter += 1

    for data in user_file:
        user_counter += 1

    print("The total number of tasks is: {} and the total number of users assigned to these tasks is: {}" .format(task_counter, user_counter))

    task_file.close()
    user_file.close()   

# userNames and userPass are the usernames and passwords already in the txt file. Define them as open strings
userNames = ""
userPass = ""

# they are saved in the file in the form 'username, password' so by removing the space and splitting by the comma
# allows us to say that the usermane will be found in index 0 and the password in index -1 (last position) 
for line in user_file:
    data = line.strip(' ')
    data = line.split(',')
    userNames += data[0]
    userPass += data[-1]

# ask the user to enter their username (If it does not match one in the txt file give an error message)
# without a valid username the user can't move on to the next step 
print("Welcome to your task manager, please login below")
username = input("Please enter your username: ")
if username not in userNames:
    print("This user does not exist!")

# once the username has been accepted ask them to enter their password. If it does not match give an error message
else:
    password = input("Please enter your password: ")    
    if password not in userPass: 
        print("Invalid password")

# when they have successfully loggen in print the menu by calling on the menu functions
# adminMenu() if the admins credentials were entered and userMenu() if not 
    else:
        print("You are now logged in")
        print("\n")
        print("Please select one of the following options: ")
        print("\n")
        if username == "admin":
            adminMenu()
        else:
            userMenu()

# close both files
user_file.close()
tasks_file.close()
