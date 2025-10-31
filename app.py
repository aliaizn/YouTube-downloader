import argparse
import yt_dlp


def download_video(url, outdir="YoutubeDownloads"):
    """"
    Downloads a video from a given URL using yt-dlp
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{outdir}/%(title)s.%(ext)s",
    }
    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Successfuly downloaded video from {url}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error failed to download video. Please check the URL and you connection")
        print(f"Details: {e}")
    except Exception as e:
        print(f"An unexpexted error ocurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A professional YouTube video downloader.")
    parser.add_argument("url", help="The URL of the YouTube video to download.")
    parser.add_argument("-o", "--output", default="YoutubeDownloads", help="The directory to save the download file.")
    args = parser.parse_args()
    download_video(args.url, outdir=args.output)
