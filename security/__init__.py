from tkinter import messagebox
from typing import *
import os

class EatzGoSecurityChecker(object):
    def __init__(self) -> Any:
        super().__init__()

        self.LICENSE = "./LICENSE"
        self.CopyRight = "./CopyRight.txt"
        self.AUTHORS = "./AUTHORS.md"
        self.ThirdPartyNotice = "./ThirdPartyNotices.md"

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