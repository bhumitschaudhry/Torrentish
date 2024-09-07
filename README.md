# Torrentish

This is a simple Python-based Torrent Client built using `tkinter` for the GUI and `libtorrent` for handling torrent downloads.

## Features

- Select a `.torrent` file to start downloading.
- Choose the download location for your files.
- Displays the download progress, including completion percentage, number of peers, and download rate.
- Uses threading to ensure the GUI remains responsive during downloads.

## Requirements

- Python 3.x
- `tkinter` 
- `libtorrent` 

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install python-libtorrent
