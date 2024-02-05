import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import threading
import re


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = int((bytes_downloaded / total_size) * 100)
    progress_bar['value'] = percentage
    root.update_idletasks()


def sanitize_filename(filename):
    # Remove invalid file name characters
    return re.sub(r'[\\/*?:"<>|]', "", filename)
 

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Revise la URL")
        return

    try:
        youtube = YouTube(url, on_progress_callback=on_progress)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        download_path = filedialog.askdirectory()
        if download_path:
            safe_title = sanitize_filename(youtube.title)
            audio_stream.download(output_path=download_path, filename=f"{safe_title}.mp3")
            messagebox.showinfo("Exito", f"Audio Descargado: {youtube.title}\nAt: {download_path}")
            url_entry.delete(0, tk.END)
        progress_bar['value'] = 0
    except Exception as e:
        messagebox.showerror("Error", str(e))
        progress_bar['value'] = 0

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Revise la URL")
        return

    try:
        youtube = YouTube(url, on_progress_callback=on_progress)
        video_stream = youtube.streams.get_highest_resolution()
        download_path = filedialog.askdirectory()
        if download_path:
            video_stream.download(download_path)
            safe_title = sanitize_filename(youtube.title)

            messagebox.showinfo("Exito", f"Video Descargado: {safe_title}\nAt: {download_path}")
            url_entry.delete(0, tk.END)  # Clear the URL entry field

        progress_bar['value'] = 0
    except Exception as e:
        messagebox.showerror("Error", str(e))
        progress_bar['value'] = 0

def start_download_thread():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()

# Create the main window
root = tk.Tk()

root.title("Para Descargar Videos de Youtube")
window_width = 500  # or any other width you prefer
window_height = 200  # adjust the height as needed
root.geometry(f"{window_width}x{window_height}")

# Create and place widgets
url_label = tk.Label(root, text="Primero Copie la URL del Video y luego lo Pega abajo:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="DESCARGAR VIDEO", command=start_download_thread)
download_button.pack()

download_audio_button = tk.Button(root, text="DESCARGAR AUDIO", command=lambda: threading.Thread(target=download_audio).start())
download_audio_button.pack()

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack()

# Run the application
root.mainloop()
