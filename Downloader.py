from pytube import YouTube as YT
import os

path = os.environ.get("path")

link = input("Enter Link\n")

video = YT(link)

print(video.title, "is being downloaded")

HRvideo = video.streams.get_highest_resolution()

HRvideo.download(f"{path}")

print("All Done")