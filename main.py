import os
import random
import datetime
from typing import *
from tkinter import *
from tkinter import messagebox

dttime = datetime.datetime.now()
print(dttime.strftime("%Y-%m-%d %H:%M:%S"))

if os.path.exists(".meals/meals.txt"):
    with open(".meals/meals.txt", "r") as f:
        meal_data_list = f.readlines()
        f.close()
    __meal__ = random.choice(meal_data_list)
    print(__meal__)
else:
    messagebox.showerror("EatzGo:", "Couldn't find file \"meals.txt\"")

class EatzGo:
    def __init__(self) -> Any:
        self.screen_size = "700x500"
        self.main_theme_color = "green"
        self.root_title = "EatzGo!"
        self.favicon_path = "assets/icon/favicon.ico"

        self.root = Tk()
        self.root.title(self.root_title)
        self.root.geometry(self.screen_size)
        self.root.config(bg=self.main_theme_color)
        self.root.iconbitmap(self.favicon_path)

        def switch_dark_mod():
            self.root.config(bg="#000")

        def switch_light_mod():
            self.root.config(bg="#fff")

        def switch_main_theme():
            self.root.config(bg=self.main_theme_color)

        self.dark_mod_btn = Button(self.root, text="Main Theme", font=('Arial', 13), bg=self.main_theme_color, fg="#fff", command=switch_main_theme)
        self.dark_mod_btn.place(x=0, y=408)

        self.dark_mod_btn = Button(self.root, text="Dark Mod(beta)", font=('Arial', 13), bg="#000", fg="#fff", command=switch_dark_mod)
        self.dark_mod_btn.place(x=0, y=437)

        self.light_mod_btn = Button(self.root, text="Light Mod(beta)", font=('Arial', 13), bg="#fff", fg="#000", command=switch_light_mod)
        self.light_mod_btn.place(x=0, y=470)

        self.meal_label = Label(self.root, text=f"Today I prupose to you the meal: {__meal__}", font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.meal_label.pack()

        self.r = Label(self.root, text="https://youtu.be/dQw4w9WgXcQ", font=('Arial', 13), bg=self.main_theme_color, fg="#000")

        self.root.mainloop()
class EatzGoServiceLoger:
    def __init__(self) -> None:
        self.dttime = datetime.datetime.now()
        self.res_date = dttime.strftime("%Y-%m-%d %H:%M:%S")
        with open("log/cookie.log", "a+") as self.f:
            self.f.write(f"pruposed_meal : {__meal__}\n")
            self.f.write(self.res_date + "\n")
            self.f.close()
        with open(f"cache/EatzGoServices.log", "a+") as f:
            f.write("[INFO]: No errors detected.")
            f.close()

if __name__ == '__main__':
    EatzGo()
    EatzGoServiceLoger()