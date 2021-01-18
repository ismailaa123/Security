#known users are the user which the system recognizes

known_users=["Ana","Brian","Cletus","Debbie"]

#This will print the legnth of the list
print(len(known_users))

#input method is used to let the user enter the information when the program is executed. 
#*** Important thing here to take note is when you use input method always remember that the type is always in string even if you enter numberical values.
#strip() eliminates any extra spaces and Capitalize() bring only the first alphabet in upper case mode

name=input("what is your name?: ").strip().capitalize()

#remove() is an inbuilt function in Python that removes a given object from the list.

if name in known_users:
    print("Hello {}!".format(name))
    remove=input("would you like to be removed from the system (y/n)?: ").lower()

    if remove =="y":
        known_users.remove(name)
    elif remove=="n":
        print("i didnt wanted to you to leave anyway")
else:
        print("Hmm i dont think i have met you yet".format(name))
        add_me=input("woudld yu like to be added to the system (y/n)").strip().lower()
        if add_me=="y":
            known_users.append(name)
            
#The append() method in python adds a single item to the existing list. It doesn't return a new list of items but will modify the original list by adding the item to the end of the list
