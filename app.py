import sys
import yt_dlp


def download_video(url, outdir="YoutubeDownloads"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{outdir}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_download.py <YouTube_URL>")
        sys.exit(1)

    url = sys.argv[1]
    download_video(url)
