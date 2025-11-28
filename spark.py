from helpers import ai, logo, salutation, shutdown, cpu_temp, battery_status, time_now
import os
import time

os.system("clear")
logo()

while True:
    try:
        question = input("Input> ")
        words = question.split()
    except KeyboardInterrupt:
        break
    try:
        if words[0] == "open":
            print(f"opening {words[1]}, sir.")
            try:
                os.system(words[1])
            except TypeError:
                print("This app isn't installed in your system, sir.")

        elif words[0] == "mode":
            mode = words[1]
            if mode == "code":
                print("Good job, sir. Opening your apps.")
                time.sleep(1)
                os.system("spotify && code")
            elif mode == "chat" or mode == "chill":
                print("Just chillax, sir.")
                time.sleep(1)
                os.system("spotify && discord&")
            else:
                print("I didn't understood your mood, sir")

        elif words[0] == "/":
            command = words[1]
            if command == "bye":
                break

            elif command == "help":
                print("I'm a sophisticated AI for helping you with your problems. Text me if you need help, sir.")

            elif command == "shutdown":
                shutdown()

        elif words[0] == "temp":
            print(cpu_temp())

        elif words[0] == "battery":
            print(battery_status())

        elif words[0] == "time":
            print(time_now())

        else:  
            answer = ai(question)
            print(answer)
            
    except KeyboardInterrupt:
        break
    
salutation()