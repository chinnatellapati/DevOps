# Design a python program for car engine start / stop /quit
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car engine started ....")
    elif command == "stop":
        print("Car engine stopped ....")
    elif command == "help":
         print(""" 
start - To start the car engine started
stop - To stop the car engine stopped
quit - To quit
         """)
    elif command == "quit":
        break
    else:
        print("sorry - i don't understand that")



