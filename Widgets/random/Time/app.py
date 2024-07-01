
import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube


def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        video = yt.streams.get_highest_resolution()
        video.download()
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
        return False

def progress_function(stream, chunk, bytes_remaining):
    progress = (1 - bytes_remaining / stream.filesize) * 100
    progress_var.set(progress)
    root.update_idletasks()

def start_download():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a valid URL.")
        return

    dialog = tk.Toplevel(root)
    dialog.title("Downloading...")
    dialog.geometry("300x100")
    
    progress_bar_dialog = ttk.Progressbar(dialog, orient='horizontal', length=250, mode='determinate', variable=progress_var)
    progress_bar_dialog.pack(pady=20)
    
    download_complete = download_video(url)
    if download_complete:
        for i in range(101):
            progress_var.set(i)
            dialog.update_idletasks()
            dialog.after(50)
        messagebox.showinfo("Success", "Download complete!")
    dialog.destroy()

root = tk.Tk()
root.title("YouTube Video Downloader")

progress_var = tk.DoubleVar()

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=10)

btn_download = tk.Button(root, text="Download", command=start_download)
btn_download.pack(pady=10)

root.mainloop()
