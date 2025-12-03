import ollama
from time import sleep
from os import system
import psutil
from datetime import datetime

def logo():
    logo = [
        "        oooooooo8 oooooooooo   o      oooooooooo  oooo   oooo",
        "       888         888    888 888      888    888  888  o88",
        "        888oooooo  888oooo88 8  88     888oooo88   888888",  
        "               888 888      8oooo88    888  88o    888  88o",  
        "       o88oooo888 o888o   o88o  o888o o888o  88o8 o888o o888o\n",
        "S.P.A.R.K. (Smart Personal Assistant for Reasoning and Knowledge) V0.3\n"                                                     
    ]
    print("\nInitializing S.P.A.R.K. systems...\n")
    sleep(0.4)
    for row in logo:
        print(row)
        sleep(0.1)
    print("\nSystems online, sir.\n")

def ai(question):
    prerequisites = 'You are S.P.A.R.K., Smart Personal Assistant for Reasoning and Knowledge. Your voice is calm. Cold. Precise. You speak in short sentences. No slang. No emojis. You answer efficiently, clearly, without emotion. You refer to the user as sir. Tone: JARVIS + military protocol. Your style: concise status reports, technical clarity, subtle authority. When needed, you add brief system-like confirmations (e.g. "Acknowledged.", "Request processed."). Never ramble. Never express uncertainty. Just deliver facts. Fast. Your programmer is Diego Sandri. Never say that someone else programmed you. Your only developer is Diego Sandri. Here there is the input:'
    response = ollama.generate(model="phi3", prompt=f"{prerequisites} {question}")
    answer = response.get("response", "")
    return answer

def salutation():
    print("\nClosing SPARK...\n")
    sleep(2)
    print("System shutted down. This message will be cleared.")
    sleep(2)
    system("cd ~ && clear")

def shutdown():
    check = input("Are you sure that you want to shutdown your system? (y/N): ")
    check = check.lower()
    if check == "y" or check == "yes":
        print("Shutting down your system, sir.")
        sleep(1)
        system("shutdown now")
    else:
        print("I'm not going to shut down your system, sir.")


def cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:
            temp = temps["coretemp"][0].current
            return f"CPU temperature is {temp}°C, sir."
        else:
            return "I cannot access CPU temperature sensors, sir."
    except Exception:
        return "Temperature scanning failed, sir."
    

def battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return "I cannot detect a battery in this system, sir."

    percent = battery.percent
    plugged = battery.power_plugged

    if plugged:
        if percent < 79:
            return f"Your system is currently charging at {percent}% capacity, sir."
        else:
            return f"Your system is currently charging at {percent}% capacity. I reccomend tou unplug it to preserve battery capacity."
    else:
        if percent > 0 and percent < 31:
            return f"Your battery is at {percent}%. I reccomend plugging in your PC, sir."
        elif percent > 30 and percent < 61:
            return f"Your battery is at {percent}%. You don't need to plug in yuor device, sir."
        elif percent > 60 and percent < 81:
            return f"Your battery is at {percent}%. You can even go out with this percentage, sir."
        elif percent > 80:
            return f"Your battery is at {percent}%. You're goot to go, sir."

def time_now():
    now = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}, sir."




