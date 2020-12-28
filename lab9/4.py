users_text = open("users.txt","r")
lines = users_text.readline()
data_info = []
temp_list = []
list_ = []
x = 0

for lines in users_text :
    if x < 3 :
        x += 1
        i = lines[:-1]
        i = i.split(";")
        data_info.append(i)
    elif x == 3:
        a = lines.split(";")
        data_info.append(a)

for i in data_info:
    names = i[2]
    names = names.split(",")

print(data_info)
def option1(data_info):
    global username
    global password
    username = input("Please enter a username:\n")
    password = input("Please enter password:\n")
    for i in data_info:
        if i[0]==username and i[1]==password:
            print("Logged in")
            return username, password
        else:
            print("Wrong password or username\n")
            username = ""
            password = ""


def option2(data_info):
    new_username = input("Please enter a username:\n")
    for i in data_info:
        if i[0] == new_username:
            print("Username is invalid")
    if new_username.isalnum()==True:
        temp_list.append(new_username)

    new_password = input("Enter a new password:\n")
    for i in data_info:
        if i[1] == new_password:
            print("Password is invalid")
        elif (new_password.isalpha()==True) or (new_password.isdigit==True) or (len(new_password)>=8 or len(new_password)<=4):
            print("Invalid password.")
        else:
            temp_list.append(new_password)
    list_.append(temp_list)
    data_info.extend(list_)
    main_menu()
def option3(data_info,username):
        listq = []
        if username != "":
            new_friend = input("Please enter your new friend:\n")
            for i in data_info:
                if new_friend in i:
                    for a in data_info:
                        if username in i[0] :
                            listq = a
                    for i in data_info:
                        if i[0] == new_friend:
                            a.append(new_friend)
                            a = tuple(a)
                            a = list(a)
                            print(a)
                else:
                    print("Friend not found\n")
                    break
        else:
            print("You need to log in first\n")
def option4(data_info,username):
    if username != "":
        for i in data_info:
            if username in i :
                print(i[2])
    else:
        print("You need to log in first\n")

def main_menu():
    menu_text = "1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"
    while True:
        print(menu_text)
        option = int(input("\n"))
        if option == 1:
            option1(data_info)
        elif option == 2:
            option2(data_info)
        elif option == 3:
            option3(data_info,username)
        elif option == 4:
            option4(data_info,username)
        elif option == 5:
            break
main_menu()



users_text.close()
