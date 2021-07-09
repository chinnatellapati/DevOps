
#Design car game using python

started = False
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Start - Start the car engine .....")
    elif command == "stop":
        if not started:
            print("car already stopped .....")
        else:
            started = False
            print("Stop - Stopping the car engine  ......")
    elif command == "help":
        print("""
    start - For starting the car engine
    stop  - For stopping the car engine 
    quit  - quit the program 
        """)
    elif command == "quit":
        break
    else:
        print("Sorry - I don't understand the command")





