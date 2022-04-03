# EatzGo Copyright (c) Boubajoker 2021. All right reserved.
# Project under MIT License.
import os
import random
import datetime
from typing import *
from tkinter import *
from tkinter import messagebox
from security import EatzGoSecurityChecker
from updater import Updater

dttime = datetime.datetime.now()
print(dttime.strftime("%Y-%m-%d %H:%M:%S"))

langs_locales = {
    'en::prupose_text' : 'Today I prupose to you the meal:',
    'en::main_theme_btn_text' : 'Main Theme',
    'en::dark_mod_btn_text' : 'Dark Mod',
    'en::light_mod_btn_text' : 'Light Mod',
    'en::clean_btn_text' : 'Clean EatzGo !',
    'en::good_mo' : 'Good morning !',
    'en::hello' : 'Hello !',
    'en::acces_updater' : 'Up to date',

    'fr::prupose_text' : 'Aujourd\'hui je vous propose le repas:',
    'fr::main_theme_btn_text' : 'Theme Principal',
    'fr::dark_mod_btn_text' : 'Mode Sombre',
    'fr::light_mod_btn_text' : 'Mode Claire',
    'fr::clean_btn_text' : 'Nettoyez EatzGo !',
    'fr::hello' : 'Bonjour !',
    'fr::acces_updater' : 'Mettre à jour'
}

#class `EatzGoCore`
class EatzGoCore(object):
    if os.path.exists(".meals/meals.txt"):
        with open(".meals/meals.txt", "r") as f:
            meal_data_list = f.readlines()
            f.close()
        __meal__ = random.choice(meal_data_list)
        print(__meal__)
    else:
        messagebox.showerror("EatzGo:", "Couldn't find file \"meals.txt\"")
        quit()
#class `EatzGo`
class EatzGo(Tk):
    def __init__(self, root_title: str, height: Any, width: Any, root_bg=None, root_favicon=None, *args) -> Tk:
        super(EatzGo, self).__init__()
        self.main_theme_color = "green"

        self.title(root_title)
        self.geometry(f"{height}x{width}")
        self.config(bg=root_bg)
        self.iconbitmap(f"{root_favicon}.ico")

        self.main_theme_mod_btn = Button(self, text=f"{langs_locales.get('en::main_theme_btn_text')}", font=('Arial', 13), bg=self.main_theme_color, fg="#fff", command=self.switch_main_theme)
        self.main_theme_mod_btn.place(x=0, y=408)

        self.dark_mod_btn = Button(self, text=f"{langs_locales.get('en::dark_mod_btn_text')}", font=('Arial', 13), bg="#000", fg="#fff", command=self.switch_dark_mod)
        self.dark_mod_btn.place(x=0, y=437)

        self.light_mod_btn = Button(self, text=f"{langs_locales.get('en::light_mod_btn_text')}", font=('Arial', 13), bg="#fff", fg="#000", command=self.switch_light_mod)
        self.light_mod_btn.place(x=0, y=470)

        self.meal_label = Label(self, text=f"{langs_locales.get('en::prupose_text')} {EatzGoCore.__meal__}!", font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.meal_label.place(x=70, y=50)

        self.switch_french = Button(self, text="Switch to french (passer en français) [beta, en test]", font=('Arial', 10), bg=self.main_theme_color, fg="#000", command=self.switch_to_french)
        self.switch_french.place(x=0, y=380)

        self.switch_english = Button(self, text="Switch to english", font=('Arial', 10), bg=self.main_theme_color, fg="#000", command=self.switch_to_english)
        self.switch_english.place(x=0, y=352)

        self.clean_btn_acces = Button(self, text=langs_locales.get('en::clean_btn_text'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.clean)
        self.clean_btn_acces.place(x=0, y=320)

        self.updater_btn = Button(self, text=langs_locales.get('en::acces_updater'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.open_updater)
        self.updater_btn.place(x=0, y=290)

        self.set_welcome_msg()
        self.set_clock()

        self.mainloop()
    
    #function `switch_dark_mod`
    def switch_dark_mod(self) -> Any:
        self.config(bg="#000")
        self.meal_label = Label(self, text=f"{langs_locales.get('en::prupose_text')} {EatzGoCore.__meal__}!", font=('Arial', 20), bg="#000", fg="#fff")
        self.meal_label.place(x=70, y=50)
        self.welcome_label = Label(self, text=langs_locales.get('en::hello'), font=('Arial', 20), bg="#000", fg="#fff")
        self.welcome_label.place(x=self.wlcm_pos, y=self.wlcm_pos)
        self.clock_label = Label(self, text=self.clock, font=('Arial', 13), bg="#000", fg="#fff")
        self.clock_label.place(x=self.clock_pos_x, y=self.clock_pos_y)


    #function `switch_light_mod`
    def switch_light_mod(self) -> Any:
        self.config(bg="#fff")
        self.meal_label = Label(self, text=f"{langs_locales.get('en::prupose_text')} {EatzGoCore.__meal__}!", font=('Arial', 20), bg="#fff", fg="#000")
        self.meal_label.place(x=70, y=50)
        self.welcome_label = Label(self, text=langs_locales.get('en::hello'), font=('Arial', 20), bg="#fff", fg="#000")
        self.welcome_label.place(x=self.wlcm_pos, y=self.wlcm_pos)
        self.clock_label = Label(self, text=self.clock, font=('Arial', 13), bg="#fff", fg="#000")
        self.clock_label.place(x=self.clock_pos_x, y=self.clock_pos_y)

    #function `switch_main_theme`
    def switch_main_theme(self) -> Any:
        self.config(bg=self.main_theme_color)
        self.meal_label = Label(self, text=f"{langs_locales.get('en::prupose_text')} {EatzGoCore.__meal__}!", font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.meal_label.place(x=70, y=50)
        self.welcome_label = Label(self, text=langs_locales.get('en::hello'), font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.welcome_label.place(x=self.wlcm_pos, y=self.wlcm_pos)
        self.clock_label = Label(self, text=self.clock, font=('Arial', 13), bg=self.main_theme_color, fg="#000")
        self.clock_label.place(x=self.clock_pos_x, y=self.clock_pos_y)


    #function `switch_to_french`
    def switch_to_french(self) -> Any:
        self.main_theme_mod_btn = Button(self, text=f"{langs_locales.get('fr::main_theme_btn_text')}", font=('Arial', 13), bg=self.main_theme_color, fg="#fff", command=self.switch_main_theme)
        self.main_theme_mod_btn.place(x=0, y=408)

        self.dark_mod_btn = Button(self, text=f"{langs_locales.get('fr::dark_mod_btn_text')}", font=('Arial', 13), bg="#000", fg="#fff", command=self.switch_dark_mod)
        self.dark_mod_btn.place(x=0, y=437)

        self.light_mod_btn = Button(self, text=f"{langs_locales.get('fr::light_mod_btn_text')}", font=('Arial', 13), bg="#fff", fg="#000", command=self.switch_light_mod)
        self.light_mod_btn.place(x=0, y=470)

        self.meal_label = Label(self, text=f"{langs_locales.get('fr::prupose_text')} {EatzGoCore.__meal__} !", font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.meal_label.place(x=70, y=50)

        self.clean_btn_acces = Button(self, text=langs_locales.get('fr::clean_btn_text'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.clean)
        self.clean_btn_acces.place(x=0, y=320)

        self.updater_btn = Button(self, text=langs_locales.get('fr::acces_updater'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.open_updater)
        self.updater_btn.place(x=0, y=290)

    #function `switch_to_english`
    def switch_to_english(self) -> Any:
        self.main_theme_mod_btn = Button(self, text=f"{langs_locales.get('en::main_theme_btn_text')}", font=('Arial', 13), bg=self.main_theme_color, fg="#fff", command=self.switch_main_theme)
        self.main_theme_mod_btn.place(x=0, y=408)

        self.dark_mod_btn = Button(self, text=f"{langs_locales.get('en::dark_mod_btn_text')}", font=('Arial', 13), bg="#000", fg="#fff", command=self.switch_dark_mod)
        self.dark_mod_btn.place(x=0, y=437)

        self.light_mod_btn = Button(self, text=f"{langs_locales.get('en::light_mod_btn_text')}", font=('Arial', 13), bg="#fff", fg="#000", command=self.switch_light_mod)
        self.light_mod_btn.place(x=0, y=470)

        self.meal_label = Label(self, text=f"{langs_locales.get('en::prupose_text')} {EatzGoCore.__meal__}", font=('Arial', 20), bg=self.main_theme_color, fg="#000")
        self.meal_label.place(x=70, y=50)

        self.clean_btn_acces = Button(self, text=langs_locales.get('en::clean_btn_text'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.clean)
        self.clean_btn_acces.place(x=0, y=320)

        self.updater_btn = Button(self, text=langs_locales.get('en::acces_updater'), font=('Arial', 13), bg=self.main_theme_color, fg="#000", command=self.open_updater)
        self.updater_btn.place(x=0, y=290)

    #function `set_welcome_msg`
    def set_welcome_msg(self) -> Any:
        self.wlcm_msg = datetime.datetime.now()
        self.wlcm_msg_result = int(self.wlcm_msg.strftime("%H"))
        self.wlcm_pos = 0

        if self.wlcm_msg_result <= 7:
            self.welcome_label = Label(self, text=langs_locales.get('en::good_mo'), font=('Arial', 20), bg=self.main_theme_color)
            self.welcome_label.place(x=self.wlcm_pos, y=self.wlcm_pos)
        else:
            self.welcome_label = Label(self, text=langs_locales.get('en::hello'), font=('Arial', 20), bg=self.main_theme_color)
            self.welcome_label.place(x=self.wlcm_pos, y=self.wlcm_pos)

    #function `set_clock`    
    def set_clock(self) -> Any:
        self.clock = datetime.datetime.now()
        self.clock_str = self.clock.strftime("%Y-%m-%d %H:%M:%S")
        self.clock_pos_x = 0
        self.clock_pos_y = 100

        self.clock_label = Label(self, text=self.clock, font=('Arial', 13), bg=self.main_theme_color)
        self.clock_label.place(x=self.clock_pos_x, y=self.clock_pos_y)        

    #function `clean`
    def clean(self) -> Any:
        try:
            with open("log/cookie.log", "w+") as self.flog:
                self.flog.write("")
                self.flog.close()
        except Exception as e:  
            print(f"[cleaner][UnknowExepetion: {e}]")
    
    #function `open_updater`
    def open_updater(self):
        Updater("EatzGo: Updater", height=500, width=200, root_bg="green", root_favicon="./assets/icon/favicon")

#class `EatzGoServiceLoger`
class EatzGoServiceLoger(object):
    def __init__(self) -> Any:
        super().__init__()

        self.dttime = datetime.datetime.now()
        self.res_date = dttime.strftime("%Y-%m-%d %H:%M:%S")
        with open("log/cookie.log", "a+") as self.f:
            self.f.write(f"pruposed_meal : {EatzGoCore.__meal__}\n")
            self.f.write(self.res_date + "\n")
            self.f.close()

__version__ = "0.0.1 Alpha C-3"
__all__ = [
    "Eatz",
    "Go !",
    "EatzG",
    "Meals",
    "Customize"
]

if __name__ == '__main__':
    EatzGoSecurityChecker()
    EatzGoServiceLoger()
    print("<!--EatzGo Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License.-->")
    EatzGo("EatzGo!", height=700, width=500, root_bg="green", root_favicon="./assets/icon/favicon")