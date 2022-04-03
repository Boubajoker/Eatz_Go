import os
from tkinter import *
from tkinter import messagebox
import requests
from typing import Any

#class `Updater`
class Updater(Tk):
    def __init__(self, root_title: str, height: Any, width: Any, root_bg=None, root_favicon=None) -> Any:
        super(Updater, self).__init__()

        self.title(root_title)
        self.geometry(f"{height}x{width}")
        self.config(bg=root_bg)
        self.iconbitmap(f"{root_favicon}.ico")
        
        self.baseUrl = 'https://boubajoker.github.io/Eatz_Go/'
        self.file_path = "assets/others/Eatz_Go.zip"
        self.downloadUrl = self.baseUrl + self.file_path

        self.downlaod_btn = Button(self, text="Downlaod the latest realese of EatzGo !", font=('Arial', 20), bg="green", fg="#000", command=self.download_realeses)
        self.downlaod_btn.pack()

        self.open_src_file_btn = Button(self, text="Open the zip file.", font=('Arial', 20), bg="green", fg="black", command=self.open_src_file)
        self.open_src_file_btn.pack()

        self.download_label = Label(self, text=f"Realeses file will be downlaoded on the URL:\n{self.baseUrl}", font=('Arial', 13), bg="green", fg="black")
        self.download_label.pack()

        self.mainloop()
    
    #function `downlaod_realeses`
    def download_realeses(self) -> Any:
        print("Downloading realeses from", self.downloadUrl + ".")
        req = requests.get(self.downloadUrl)
        filename = req.url[self.downloadUrl.rfind('/')+1:]
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        #function `downlaod_file`
        def download_file(url, filename='') -> Any:
            try:
                if filename:
                    pass            
                else:
                    filename = req.url[self.downloadUrl.rfind('/')+1:]
                with requests.get(url) as req:
                    with open(filename, 'wb') as f:
                        for chunk in req.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                    return filename
            except Exception as e:
                messagebox.showerror("EatzGo: Updater", f"[ERROR]:{e}")
                print("[ERROR]:", e)
                return None
    
    #function `open_src_file`
    def open_src_file(self) -> Any:
        if os.path.exists("Eatz_Go.zip"):
            os.system("start %cd%/Eatz_Go.zip")
        else:
            os.system("start %cd%")

if __name__ == "__main__":
    pass