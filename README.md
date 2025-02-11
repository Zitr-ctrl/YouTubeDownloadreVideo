# Código para descargar videos de YouTube

## Pasos a seguir para el uso correcto del código

### Consideraciones
Este código usa Python 3.12.1 
y necesita tener instara FFMPEG para poder tener el video en un formato correcto

#### Pasos para instalar ffmpeg
1. ve al sitio web y descarga los documentos [Enlace de FFMPEG](https://ffmpeg.org/download.html)

2. Extrae el archivo zip que descargaste del repositorio de github, Copia el contenido extraído (generalmente una carpeta llamada ffmpegcon subcarpetas bin, doc, etc.) a una ubicación conveniente, como C:\ffmpeg.

3. Agrega la ruta de la carpeta a las variables de entorno

    Abre el Panel de Control y ve a "Sistema y seguridad" > "Sistema" > "Configuración avanzada del sistema".

    Haz clic en "Variables de entorno".oEn "Variables del sistema", selecciona la variable Pathy haz clic en "Editar".
    
    Agrega la ruta completa a la carpeta binde FFmpeg (por ejemplo, C:\ffmpeg\bin).oHaz clic en "Aceptar" para cerrar todas las ventanas

4. Verifica la instlación - Abre una ventana de línea de comandos y escribe ffmpeg -version. Si ves información sobre la versión de FFmpeg, la instalación ha sido exitosa.

#### Instalación y Configuración del Entorno Virtual

Una vez que se haya instalado correctamente ffmpeg podemos seguir con la reación del entorno virtual

Dentro de la carpeta en la que tienes descargado el código del proyecto crea un entorno virtual con el comando: python -m venv env, luego activa el entorno con el comando: env\Scripts\activate, luego instala las dependencias necesarias en el enotrno virtual con el comando: pip install -r requirementes.txt, una vez hecho eso ya peudes ejecutar el código

### Uso del Código

Una vez lo ejecutes en la consola te pedirá que pegues el link del video que deseas descargar, este video se descargará en la mejor calidad promedio en formato MP4 en la carpeta acutal en la que ejecutes el programa

### Nota
Estaré mejorando este código con más opciones y funciones en un futuro