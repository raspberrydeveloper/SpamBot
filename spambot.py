import keyboard
import customtkinter
import threading
from time import sleep

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

active = False
delaytime = 0.02

def threadstart():
    thread = threading.Thread(target=start)
    thread.daemon = True
    thread.start()

def start():

    global active, entry1, entry2, delaytime
    active = True
    spamword = str(entry1.get())
    times = int(entry2.get())

    print(f"Sleeping 5 seconds and starting with {delaytime} second typing delay...")
    sleep(5)

    for i in range(times):
        if active == True:
            keyboard.write(spamword)
            keyboard.press("enter")
            sleep(delaytime)
        else:
            pass

def stop():
    global active
    active = False

def gui():
    global stop, start, entry1, entry2
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="SpamBot", text_font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="The word to spam.")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Times to spam.")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Start", command=threadstart)
    button.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Stop", command=stop)
    button.pack(pady=12, padx=10)

    root.mainloop()

gui()