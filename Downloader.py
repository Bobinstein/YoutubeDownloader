from pytube import YouTube as YT

link = input("Enter Link\n")

video = YT(link)

print(video.title, "is being downloaded")

HRvideo = video.streams.get_highest_resolution()

HRvideo.download(f"C:\\Users\\cavan\\Videos\\YouTube-Downloads/{video.title}")

print("All Done")