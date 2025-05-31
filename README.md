# Python Video Renderer Based on Static Images and Audio Files

This project provides Python scripts to generate videos by combining static images with audio tracks. It uses FFmpeg to create high-quality 1080p videos, ideal for visual storytelling, podcasts, or social media content.

## Scripts Overview

### `generate_single_video.py`

Generates a single video from:

* One **image** (JPG or PNG)
* One **audio file** (MP3)

The resulting video (`output.mp4`) displays the static image while playing the audio, encoded using FFmpeg.

### `generate_videos_by_date.py`

Generates multiple videos across a date range. For each date (in `YYYY-MM-DD` format), it:

* Looks for a matching image in `source/imgs/`
* Looks for a matching audio file in `source/audio/`
* Generates a video if both exist
* Skips and logs an error if either is missing

Example:

```
source/
├── imgs/
│   ├── 2025-06-15.jpg
│   └── 2025-06-16.jpg
├── audio/
│   ├── 2025-06-15.mp3
│   └── 2025-06-16.mp3
```

Each output video will be saved in the `output/` directory as `YYYY-MM-DD.mp4`.

## Features

* Outputs **1920x1080 resolution** videos at **24fps**
* Uses `-tune stillimage` for efficient static encoding
* Ensures clean synchronization between image and audio
* Handles multiple days with minimal setup
* Logs missing media files for audit and debugging

## Getting Started

### Prerequisites

* Python 3.7 or later
* FFmpeg installed and accessible in your system PATH

Install FFmpeg:

* Ubuntu:

  ```bash
  sudo apt install ffmpeg
  ```
* macOS:

  ```bash
  brew install ffmpeg
  ```
* Windows:
  Download from [FFmpeg's official site](https://ffmpeg.org/download.html) and add it to PATH.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/biagolini/PythonVideoFromImageAudio.git
   cd PythonVideoFromImageAudio
   ```

2. **Prepare the Source Files**

   For `generate_single_video.py`:

   ```
   source/
   ├── image.jpg
   └── music.mp3
   ```

   For `generate_videos_by_date.py`:

   ```
   source/
   ├── imgs/
   │   ├── YYYY-MM-DD.jpg
   └── audio/
       ├── YYYY-MM-DD.mp3
   ```

3. **Run the Scripts**

   For a single video:

   ```bash
   python generate_single_video.py
   ```

   For batch generation:

   ```bash
   python generate_videos_by_date.py
   ```

4. **Output**

   The generated videos will appear in the `output/` directory.

## File Structure

```
PythonVideoFromImageAudio/
├── generate_single_video.py
├── generate_videos_by_date.py
├── source/
│   ├── image.jpg
│   ├── music.mp3
│   ├── imgs/
│   │   ├── 2025-06-15.jpg
│   │   └── ...
│   └── audio/
│       ├── 2025-06-15.mp3
│       └── ...
└── output/
    ├── output.mp4
    ├── 2025-06-15.mp4
    └── ...
```

## Dependencies

No Python packages required (FFmpeg must be installed and in PATH).

Optionally, you can install `ffmpeg-python` if you prefer a Python wrapper:

```bash
pip install ffmpeg-python
```

## License and Disclaimer

This project is open-source under the MIT License. Use and modify it freely. The author assumes no responsibility for misuse or output content.

---

Happy rendering! 🎥✨
