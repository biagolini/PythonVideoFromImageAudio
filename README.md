# Python Video Renderer Based on Static Images and Audio Files

This project provides a simple Python script that generates a video from a static image and an audio file. It leverages the power of FFmpeg to render a 1080p, 24fps video with synchronized image and audio.

## Script: `main.py`

This script takes:

* One **image** (JPG or PNG)
* One **music file** (MP3)
* Produces a video file (`output.mp4`) using FFmpeg

## Features

* Outputs a **1920x1080 resolution** video
* Static image is displayed for the full duration of the audio
* Audio and video are synced perfectly
* Uses **FFmpeg** for performance and quality
* Runs entirely via standard Python libraries (no pip dependencies)

## Getting Started

### Prerequisites

* Python 3.7 or later
* FFmpeg installed and available in your system PATH

Install FFmpeg using your system's package manager:

* On Ubuntu:

  ```bash
  sudo apt install ffmpeg
  ```
* On macOS:

  ```bash
  brew install ffmpeg
  ```
* On Windows:
  Download from [FFmpeg's official website](https://ffmpeg.org/download.html) and add it to your PATH.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/biagolini/PythonVideoFromImageAudio.git
   cd PythonVideoFromImageAudio
   ```

2. **Prepare the Source Files**
   Inside the project directory, create a `source/` folder and place the following:

   ```
   source/
   ├── image.jpg
   └── music.mp3
   ```

3. **Run the Script**

   ```bash
   python main.py
   ```

4. **Output**
   The resulting video will be saved as:

   ```
   output.mp4
   ```

## File Structure

```
PythonVideoFromImageAudio/
├── main.py
├── source/
│   ├── image.jpg
│   └── music.mp3
└── output/
    └── output.mp4
```

## Dependencies

None (aside from FFmpeg being available on your system).

If you prefer a Pythonic wrapper, you can optionally install `ffmpeg-python`:

```bash
pip install ffmpeg-python
```

## License and Disclaimer

This project is open-source under the MIT License. You are free to use and modify it at your discretion. The author is not responsible for how this code is used.

---

Happy rendering! 🎥✨
