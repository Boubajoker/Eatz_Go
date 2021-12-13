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
    def __init__(self, root_title, root_size, root_bg, root_favicon) -> Any:
        self.main_theme_color = "green"

        self.root = Tk()
        self.root.title(root_title)
        self.root.geometry(root_size)
        self.root.config(bg=root_bg)
        self.root.iconbitmap(root_favicon)

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
    def __init__(self) -> Any:
        self.dttime = datetime.datetime.now()
        self.res_date = dttime.strftime("%Y-%m-%d %H:%M:%S")
        with open("log/cookie.log", "a+") as self.f:
            self.f.write(f"pruposed_meal : {__meal__}\n")
            self.f.write(self.res_date + "\n")
            self.f.close()
        with open(f"cache/EatzGoServices.log", "a+") as f:
            f.write(f"[Script_Path]: 'main.py' saved:{None}\n")
            f.close()

class EatzGoSecurityChecker:
    def __init__(self) -> Any:
        self.LICENSE = "LICENSE"
        self.CopyRight = "CopyRight.txt"
        self.AUTHORS = "AUTHORS.md"
        self.ThirdPartyNotice = "ThirdPartyNotice.txt"

        if os.path.exists(self.LICENSE):
            print(self.LICENSE, "file found.")
        else:
            messagebox.showerror("EatzGo:", f"{self.LICENSE} file not found, if you are using an illegal copy of this project quit it NOW !")
            quit()

        if os.path.exists(self.AUTHORS):
            print(self.AUTHORS, "file found.")
        else:
            messagebox.showerror("EatzGo:", f"{self.AUTHORS} file not found, if you are using an illegal copy of this project quit it NOW !")
            quit()

        if os.path.exists(self.CopyRight):
            print(self.CopyRight, "file found.")
        else:
            messagebox.showerror("EatzGo:", f"{self.CopyRight} file not found, if you are using an illegal copy of this project quit it NOW !")
            quit()

        if os.path.exists(self.ThirdPartyNotice):
            print(self.ThirdPartyNotice, "file found.")
        else:
            messagebox.showerror("EatzGo:", f"{self.ThirdPartyNotice} file not found, if you are using an illegal copy of this project quit it NOW !")
            quit()

if __name__ == '__main__':
    EatzGoSecurityChecker()
    EatzGo("EatzGo!", root_size="700x500", root_bg="green", root_favicon="assets/icon/favicon.ico")
    EatzGoServiceLoger()