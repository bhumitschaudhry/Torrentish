import tkinter as tk
from tkinter import filedialog, messagebox
class TorrentClient:
    def __init__(self, root):
        #Base
        self.root = root
        self.root.title("Python Torrent Client")
        self.root.geometry("640x360")
        self.center_frame = tk.Frame(self.root)
        self.center_frame.pack(expand=True)
        #File Selector
        self.label1 = tk.Label(self.center_frame, text="Torrent Client",font=("Arial",20,"bold"))
        self.label1.pack(pady=15)
        self.label2 = tk.Label(self.center_frame, text="Select a file:",font=("Arial"))
        self.label2.pack(pady=10)
        self.torrent_path = tk.StringVar()
        tk.Entry(self.center_frame, textvariable=self.torrent_path,width=50).pack(pady=10)
        tk.Button(self.center_frame, text="Open Torrent", command=self.open_torrent).pack(pady=5)
        #Start Button
        self.start_button = tk.Button(self.center_frame, text="Start Download", command=self.start_download)
        self.start_button.pack(pady=5)
        #Status
        self.status_label = tk.Label(self.center_frame, text="Status: Not Started")
        self.status_label.pack(pady=10)

    def open_torrent(self):
        file_path = filedialog.askopenfilename(filetypes=[("Torrent files",".torrent")])
        if file_path:
            self.torrent_path.set(file_path)
    
    def start_download(self):
        messagebox.showinfo("Start Download","Download functionality not implemented yet")

def main():
    root = tk.Tk()
    app = TorrentClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()