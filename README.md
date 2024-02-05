# YouTube Video and Audio Downloader

This simple Python application allows users to download videos and audio from YouTube. It provides a basic graphical user interface (GUI) to paste the YouTube URL and download the content in either video or audio format.

## Features

- Download videos in the highest available resolution.
- Download audio in MP3 format.
- Display download progress.
- Simple and user-friendly interface.

## Requirements

- Python 3
- `pytube` Python library
- `tkinter` for the GUI (usually comes with Python)

## Installation

Before running the application, you need to install the `pytube` library. You can install it using pip:

```bash
pip install pytube
```

## Usage
To use the downloader, follow these steps:

Run the script with Python:

```bash
python youtube_downloader.py
```
The application window will appear. Copy and paste the YouTube URL into the provided text field.

To download a video, click the DESCARGAR VIDEO button. For audio, click the DESCARGAR AUDIO button.

A file dialog will appear, prompting you to choose the save location. Navigate to your desired directory and confirm.

The progress bar within the application will show the download progress.

Once the download is complete, the application will display a message with the file's location, and the URL field will be cleared.

## Notes
-Ensure you have the legal rights to download content from YouTube.
-This script is intended for educational purposes and personal use only.
-Filename sanitization is essential to prevent errors due to invalid characters in file names on different operating systems
