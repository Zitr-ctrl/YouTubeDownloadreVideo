import yt_dlp

def download_video(link):
    # Opciones para descargar video (137) y audio (140) y fusionarlos
    ydl_opts = {
        'format': '137+140/best',  # Video 1080p (137) + Audio M4A (140)
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
        'merge_output_format': 'mp4',  # Forzar salida en MP4
        'postprocessors': [
            {  
                'key': 'FFmpegVideoConvertor',  
                'preferedformat': 'mp4'  # Asegura que la conversión se haga en MP4
            },
            {  
                'key': 'FFmpegMetadata'  # Mantiene metadatos originales
            }
        ],
        'ffmpeg_location': r"C:\ffmpeg\bin\ffmpeg.exe"  # Ruta de FFmpeg (ajústala si es necesario)
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("✅ Descarga completa con audio 🎵")
    except Exception as e:
        print(f'❌ Hubo un problema al descargar el video: {e}')

# Solicitar la URL del video
link = input("Pega la URL del video a descargar: ").strip()
download_video(link)
