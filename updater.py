from tkinter import *
from tkinter import messagebox
import requests
from typing import Any

class Updater(object):
    def __init__(self, root_title: str, height: int, width: int, root_bg=None, root_favicon=None) -> Any:
        super().__init__()

        self.root = Tk()
        self.root.title(root_title)
        self.root.geometry(f"{height}x{width}")
        self.root.config(bg=root_bg)
        self.root.iconbitmap(f"{root_favicon}.ico")
        
        self.downlaod_btn = Button(self.root, text="Downlaod the latest realese of EatzGo !", font=('Arial', 13), bg="green", fg="#000", command=self.download_realeses)
        self.downlaod_btn.pack()

        self.root.mainloop()

    def download_realeses(self):
        downloadUrl = 'https://boubajoker.github.io/Eatz_Go/assets/others/Eatz_Go.zip'
        req = requests.get(downloadUrl)
        filename = req.url[downloadUrl.rfind('/')+1:]
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        def download_file(url, filename=''):
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

if __name__ == "__main__":
    pass