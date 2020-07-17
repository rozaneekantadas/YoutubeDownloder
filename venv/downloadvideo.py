from pytube import YouTube
from pytube import Playlist

url = input("Enter Youtube Link: ")
print("Stream Loading...\n")

ytd = YouTube(url)
video = ytd.streams

i = 1
print("Available Stream\n")
for stream in video:
    print(str(i)+" "+str(stream))
    i += 1

num = int(input("\nEnter Stream Number: "))

print("Downloading...")
video = video[num - 1]
video.download("D:\Music Video")
print("Download Finish")