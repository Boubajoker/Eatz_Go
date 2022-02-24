import os
import sys
from tkinter import *
from tkinter import messagebox
import requests
from typing import Any

class Updater(object):
    def __init__(self, root_title: str, height: Any, width: Any, root_bg=None, root_favicon=None) -> Any:
        super().__init__()

        self.root = Tk()
        self.root.title(root_title)
        self.root.geometry(f"{height}x{width}")
        self.root.config(bg=root_bg)
        self.root.iconbitmap(f"{root_favicon}.ico")
        
        self.downlaod_btn = Button(self.root, text="Downlaod the latest realese of EatzGo !", font=('Arial', 20), bg="green", fg="#000", command=self.download_realeses)
        self.downlaod_btn.place(x=0, y=70)

        self.open_src_file_btn = Button(self.root, text="Open the zip file.", font=('Arial', 20), bg="green", fg="black", command=self.open_src_file)
        self.open_src_file_btn.pack()

        self.root.mainloop()

    def download_realeses(self) -> Any:
        downloadUrl = 'https://boubajoker.github.io/Eatz_Go/assets/others/Eatz_Go.zip'
        req = requests.get(downloadUrl)
        filename = req.url[downloadUrl.rfind('/')+1:]
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        def download_file(url, filename='') -> Any:
            try:
                if filename:
                    pass            
                else:
                    filename = req.url[downloadUrl.rfind('/')+1:]
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
    
    def open_src_file(self) -> Any:
        if os.path.exists("Eatz_Go.zip"):
            os.system("start %cd%/Eatz_Go.zip")
        else:
            os.system("start %cd%")

if __name__ == "__main__":
    pass