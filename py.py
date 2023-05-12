import time
import os
import vlc
from pathlib import Path
adminpassword = "pancak"
def beep():
    beep = vlc.MediaPlayer("file:///beep.mp3")
    beep.play()
def main():
    beep()
    print("")
    print("")
    print("welcome to pandu v1.4!")
    print("")
    beep()
    if os.path.exists(r"D:\IansCode\pandu\user1") and not os.path.exists(r"D:\IansCode\pandu\user2"):
        print("current user amount: 1")
    elif os.path.exists(r"D:\IansCode\pandu\user1") and os.path.exists(r"D:\IansCode\pandu\user2"):
        print("current user amount: 2")
    elif not os.path.exists(r"D:\IansCode\pandu\user1") and not os.path.exists(r"D:\IansCode\pandu\user2"):
        print("current user amount: 0")
    print("")
    yn = input("command: [input 'cmds' to see all commands]: ")
    if yn == "signin":
        print("")
        beep()
        enteruser = input("username: ")
        correctpass = Path("user1/user1pass.txt").read_text()
        correctuser = Path("user1/user1.txt").read_text()
        beep()
        enter = input("password: ")
        if enter == correctpass and enteruser == correctuser:
            print("")
            beep()
            print(f"signed in as {correctuser}!")
        else:
            print("")
            beep()
            print("wrong username or password!")
            pass
    if yn == "signup":
        print("")
        beep()
        print("sign up:")
        username = input("username: ")
        beep()
        password = input("password: ")
        beep()
        yasure = input("are you sure? [y/n]: ")
        if yasure == "y":
            beep()
            print("making dir...")
            newpath = r"D:\IansCode\pandu\user1"
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                beep()
                print("creating files (this may take a minute)...")
                with open("user1/user1.txt", "w") as text_file:
                    text_file.write(f"{username}")
                with open("user1/user1pass.txt", "w") as text_file:
                    text_file.write(f"{password}")
                beep()
                print("complete! restarting pandu...")
            elif os.path.exists(newpath):
                newpath = "user2"
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    beep()
                    print("creating files (this may take a minute)...")
                    with open("user2/user2.txt", "w") as text_file:
                        text_file.write(f"{username}")
                    with open("user2/user2pass.txt", "w") as text_file:
                        text_file.write(f"{password}")
                    beep()
                    print("complete! restarting pandu...")
                elif os.path.exists(newpath):
                    print("sorry! pandu is full of users! contact an admin for help.")
    elif yn == "cmds":
        beep()
        cmds = '''
        pandu (1.4) commands:

        signin - sign into your pandu account.
        signup - make an account for pandu.
        cmds - show this list.
        userdata - show the username and password of a user. (ADMIN)
        version - check the version of pandu.
        del - delete a user. (ADMIN)

        if you see "(ADMIN)" next to a command, that means you'll have to enter a password to continue.
        '''
        print(cmds)
        time.sleep(2)
    elif yn == "version":
        vers = '''
        the current version of pandu is:

        v1.4 - added more commands and polished user creation and deletion!

        enjoy pandu!
        '''
        beep()
        print(vers)
        print("")
        beep()
        print("pandu will now restart.")
    elif yn == "userdata":
        beep()
        print("this command is an admin function.")
        beep()
        areuadmin = input("enter admin passcode!: ")
        if areuadmin == adminpassword:
            beep()
            print("")
            print("correct passcode entered!")
            if os.path.exists(r"D:\IansCode\pandu\user1") and not os.path.exists(r"D:\IansCode\pandu\user2"):
                beep()
                print("gathering data of user 1...")
                scanuser1 = Path(f"user1/user1.txt").read_text()
                scanuserpass1 = Path(f"user1/user1pass.txt").read_text()
                beep()
                print(f"name of user 1: {scanuser1}")
                beep()
                print(f"password of user 1: {scanuserpass1}")
                print("")
                beep()
                input("press enter to restart pandu.")
            elif not os.path.exists(r"D:\IansCode\pandu\user1") and not os.path.exists(r"D:\IansCode\pandu\user2"):
                beep()
                print("there are currently no users on pandu!")
            elif os.path.exists(r"D:\IansCode\pandu\user1") and os.path.exists(r"D:\IansCode\pandu\user2"):
                beep()
                which = input("show the data of which user [1/2]: ")
                beep()
                print(f"gathering data of user {which}...")
                scanuser = Path(f"user{which}/user{which}.txt").read_text()
                scanuserpass = Path(f"user{which}/user{which}pass.txt").read_text()
                beep()
                print(f"name of user {which}: {scanuser}")
                beep()
                print(f"password of user {which}: {scanuserpass}")
                print("")
                beep()
                input("press enter to restart pandu.")
        else:
            beep()
            beep()
            beep()
            print("incorrect password!")
            beep()
            input("press enter to restart pandu.")
    elif yn == "del":
        beep()
        print("this command is an admin function.")
        beep()
        areuadmin = input("enter admin passcode!: ")
        if areuadmin == adminpassword:
            beep()
            print("")
            print("correct passcode entered!")
            beep()
            deluser = input("are you sure? [y/n]: ")
            if deluser == "y":
                beep()
                usertodel = input("delete which user? enter anything else to cancel. [1/2]: ")
                if usertodel != "1" and not "2":
                    beep()
                    print("deletion cancelled. restarting pandu...")
                elif usertodel == "1":
                    beep()
                    print("deleting...")
                    os.remove('user1/user1.txt')
                    os.remove('user1/user1pass.txt')
                    os.removedirs('user1')
                    beep()
                    print("deleted. restarting pandu to apply changes...")
                elif usertodel == "2":
                    beep()
                    print("deleting...")
                    os.remove('user2/user2.txt')
                    os.remove('user2/user2pass.txt')
                    os.removedirs('user2')
                    beep()
                    print("deleted. restarting pandu to apply changes...") 
            elif deluser == "n" or deluser != "y" or "n":
                beep()
                print("deletion cancelled.")
            
        
while True:
    main()
    
