# YouTube Downloader CLI

A professional, robust command-line tool to download video or audio from YouTube.

## Features

-   **Professional CLI:** Uses `argparse` for clean, user-friendly command-line arguments.
-   **Robust Error Handling:** Gracefully handles bad URLs and network issues.
-   **Custom Output:** Specify a custom output directory for your downloads.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd youtube-downloader
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To download a video, provide the URL as the main argument.

```bash
python app.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

By default, files are saved to the `YoutubeDownloads/` directory. You can specify a different directory using the `-o` or `--output` flag:

```bash
python app.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o ~/Music/
```
