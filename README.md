# Terminal Renderer

Terminal Renderer is a Python-based tool that allows you to render images and videos in the terminal using ASCII art or colored blocks. This project leverages libraries such as OpenCV, PIL (Pillow), and Rich to process and display media files directly in the terminal.

## Features

- Convert images to ASCII art.
- Convert images to colored blocks.
- Convert videos to ASCII art.
- Convert videos to colored frames using colored blocks.
- Adjustable output width for terminal display.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies

Install the required Python packages using pip:

```bash
pip install opencv-python numpy pillow rich
```

### Usage
Command-line Interface
```bash
python3 terminal_renderer.py <file_path> [--ascii] [--color]
```

- <file_path>: Path to the image or video file you want to render.
- --ascii: Render the file as ASCII art.
- --color: Render the file using colored blocks

### Examples
Render an Image as ASCII Art
```bash
python3 terminal_renderer.py example/demo.jpg --ascii
```
Render an Image with Colored Blocks


```bash
python3 terminal_renderer.py example/demo.jpg --color
```
Render a Video as ASCII Art
```bash
python3 terminal_renderer.py example/demo.mp4 --ascii
```

Render a Video with Colored Frames
```bash
python3 terminal_renderer.py example/demo.mp4 --color
```
