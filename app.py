import tkinter as tk
from tkinter import ttk, messagebox
import threading
import yt_dlp

# Ruta de FFmpeg
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

def download_video(link, progress_label):
    # Opciones para descargar video (137) y audio (140) y fusionarlos
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
            {'key': 'FFmpegMetadata'}
        ],
        'ffmpeg_location': FFMPEG_PATH
    }

    try:
        progress_label.config(text="⏳ Descargando...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        progress_label.config(text="✅ Descarga completa")
        messagebox.showinfo("Éxito", "El video se descargó correctamente.")
    except Exception as e:
        progress_label.config(text="❌ Error en la descarga")
        messagebox.showerror("Error", f"No se pudo descargar el video:\n{e}")

def start_download():
    link = entry_link.get().strip()
    if not link:
        messagebox.showwarning("Advertencia", "Por favor ingresa un enlace.")
        return
    threading.Thread(target=download_video, args=(link, progress_label), daemon=True).start()

# Crear ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")
root.geometry("500x200")
root.resizable(False, False)

# Etiqueta de instrucciones
label = tk.Label(root, text="Pega el enlace del video de YouTube:", font=("Arial", 12))
label.pack(pady=10)

# Campo de entrada
entry_link = tk.Entry(root, width=50, font=("Arial", 10))
entry_link.pack(pady=5)

# Botón de descarga
btn_download = tk.Button(root, text="Descargar", font=("Arial", 12), command=start_download)
btn_download.pack(pady=10)

# Etiqueta de progreso
progress_label = tk.Label(root, text="", font=("Arial", 10))
progress_label.pack(pady=5)

root.mainloop()
