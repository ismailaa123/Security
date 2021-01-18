known_users=["Dania","ismail","Mom","Dad"]

print(len(known_users))


name=input("what is your name?: ").strip().capitalize()

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
            
