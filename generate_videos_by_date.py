import subprocess
import shutil
import os
import time
from datetime import datetime, timedelta

# Paths
source_img_path = "source/img"
source_audio_path = "source/audio"
output_dir = "output"

# Date range for processing
start_date = datetime.strptime("2025-06-15", "%Y-%m-%d")
end_date = datetime.strptime("2025-06-17", "%Y-%m-%d")

# Ensure ffmpeg is available
if not shutil.which("ffmpeg"):
    raise EnvironmentError("ffmpeg not found. Make sure it is installed and in your system PATH.")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Loop through each date to generate daily compilations
current_date = start_date
while current_date <= end_date:
    output_file_name = current_date.strftime("%Y-%m-%d")
    image_file = os.path.join(source_img_path, f"{output_file_name}.jpg")
    audio_file = os.path.join(source_audio_path, f"{output_file_name}.mp3")
    output_path = os.path.join(output_dir, f"{output_file_name}.mp4")
    current_time = time.strftime("[%Y-%m-%d %H:%M]", time.localtime())

    print("-" * 70)
    print(f"{current_time} Processing {output_file_name}...")

    if not os.path.isfile(image_file):
        print(f"{current_time} ERROR: Image not found -> {image_file}")
        current_date += timedelta(days=1)
        continue

    if not os.path.isfile(audio_file):
        print(f"{current_time} ERROR: Audio not found -> {audio_file}")
        current_date += timedelta(days=1)
        continue

    # FFmpeg command
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_file,
        "-i", audio_file,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-r", "24",
        "-s", "1920x1080",
        output_path
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(f"{current_time} SUCCESS: Video generated -> {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"{current_time} ERROR: FFmpeg failed for {output_file_name}\n{e}")

    current_date += timedelta(days=1)
