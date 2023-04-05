from pytube import YouTube as YT
import os
from dotenv import load_dotenv

load_dotenv()

downloadPath = os.environ.get("downloadPath")


link = input("Enter Link\n")

video = YT(link)

print(video.title, "is being downloaded")

HRvideo = video.streams.get_highest_resolution()

HRvideo.download(f"{downloadPath}")

print("All Done")