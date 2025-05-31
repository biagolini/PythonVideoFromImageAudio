import subprocess
import shutil
import os

# Input files
image_path = "source/image.jpg"
audio_path = "source/music.mp3"

# Output directory and file
output_dir = "output"
output_filename = "output.mp4"
output_path = os.path.join(output_dir, output_filename)

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Ensure ffmpeg is available
if not shutil.which("ffmpeg"):
    raise EnvironmentError("ffmpeg not found. Make sure it is installed and in your system PATH.")

# FFmpeg command
cmd = [
    "ffmpeg",
    "-y",                   # Overwrite output if it exists
    "-loop", "1",           # Loop the image
    "-i", image_path,       # Input image
    "-i", audio_path,       # Input audio
    "-c:v", "libx264",      # Use H.264 codec
    "-tune", "stillimage",  # Optimize for static image
    "-c:a", "aac",          # Use AAC audio
    "-b:a", "192k",         # Set audio bitrate
    "-pix_fmt", "yuv420p",  # Compatible pixel format
    "-shortest",            # Stop when the shortest input ends
    "-r", "24",             # Frame rate
    "-s", "1920x1080",      # Resolution
    output_path
]

# Run the command
try:
    subprocess.run(cmd, check=True)
    print(f"Video generated successfully: {output_path}")
except subprocess.CalledProcessError as e:
    print("FFmpeg failed:", e)
