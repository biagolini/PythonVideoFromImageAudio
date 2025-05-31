import subprocess
import shutil
import os
import time
from datetime import datetime, timedelta

# Define input and output folders
source_img_path = "source/img"
source_audio_path = "source/audio"
output_dir = "output"

# Define the date range to process (videos will be generated for each date)
start_date = datetime.strptime("2025-06-15", "%Y-%m-%d")
end_date = datetime.strptime("2025-06-17", "%Y-%m-%d")

# Check if ffmpeg is available in the system PATH
if not shutil.which("ffmpeg"):
    raise EnvironmentError("ffmpeg not found. Make sure it is installed and in your system PATH.")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through the date range
current_date = start_date
while current_date <= end_date:
    output_file_name = current_date.strftime("%Y-%m-%d")
    image_file = os.path.join(source_img_path, f"{output_file_name}.jpg")
    audio_file = os.path.join(source_audio_path, f"{output_file_name}.mp3")
    output_path = os.path.join(output_dir, f"{output_file_name}.mp4")
    current_time = time.strftime("[%Y-%m-%d %H:%M]", time.localtime())

    print("-" * 70)
    print(f"{current_time} Processing {output_file_name}...")

    # Check if input files exist
    if not os.path.isfile(image_file):
        print(f"{current_time} ERROR: Image not found -> {image_file}")
        current_date += timedelta(days=1)
        continue

    if not os.path.isfile(audio_file):
        print(f"{current_time} ERROR: Audio not found -> {audio_file}")
        current_date += timedelta(days=1)
        continue

    # --------------------------------------------
    # Choose between CPU or GPU encoding:
    # Uncomment the one you want to use
    # --------------------------------------------

    # CPU-based encoding using libx264
    # This is widely compatible and works even without a dedicated GPU
    """
    cmd = [
        "ffmpeg",
        "-y",                     # Overwrite output without asking
        "-loop", "1",             # Loop the image to match audio length
        "-i", image_file,         # Input image
        "-i", audio_file,         # Input audio
        "-c:v", "libx264",        # CPU-based H.264 encoder
        "-tune", "stillimage",    # Optimize for static images (less motion analysis)
        "-c:a", "aac",            # Audio codec: AAC
        "-b:a", "192k",           # Audio bitrate
        "-pix_fmt", "yuv420p",    # Pixel format for wide compatibility
        "-shortest",              # Stop encoding when the shortest stream ends
        "-r", "24",               # Frames per second
        "-s", "1920x1080",        # Output resolution
        output_path
    ]
    """

    # GPU-based encoding using NVIDIA NVENC (requires compatible NVIDIA GPU)
    # Much faster than CPU encoding, but may be slightly less efficient at low bitrates
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_file,
        "-i", audio_file,
        "-c:v", "h264_nvenc",     # GPU-based encoder (NVIDIA)
        "-preset", "p4",          # Speed/quality trade-off: p1 (slowest) to p7 (fastest)
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-r", "24",
        "-s", "1920x1080",
        output_path
    ]

    # Run the FFmpeg command
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(f"{current_time} SUCCESS: Video generated -> {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"{current_time} ERROR: FFmpeg failed for {output_file_name}\n{e}")

    # Move to the next day
    current_date += timedelta(days=1)
