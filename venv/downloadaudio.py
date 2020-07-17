from pytube import YouTube
from pytube import Playlist

url = input("Enter Youtube Link: ")

print("Downloading...")
ytd = YouTube(url)
ytd.streams.filter(only_audio=True).first().download("D:\Music")
print("Finish")
