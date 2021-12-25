import sys
from os import name
import urllib.request
import pytube
from pytube import Playlist


def install_video_from_yotube(url):
  link = url
  yt = pytube.YouTube(link)
  print("do you want highest resolution or lowest resolution or specified: \n")
  print("1-highest resolution \n")
  print("2-lowest resolution \n")
  print("3-specified \n")
  ask = input("")
  if ask=="1":
      stream = yt.streams.get_highest_resolution()
      stream.download('./')
  elif ask=="2":
      stream = yt.streams.get_lowest_resolution()
      stream.download('./')
  elif ask=="3":
      res = input("Enter resolution you want: \n")
      res = (f"{res}p")
      stream = yt.streams.filter(file_extension='mp4')
      if stream.get_by_resolution(res) == None:
         print("this res is not avilable \n")
      else:
         stream = yt.streams.get_by_resolution(res)
         stream.download('./')
  
  else:
      print("Enter a valid option \n")
  

#Funcation to install outside youtube
def install_outside_youtube(url,name):
    try:
        url = input("Enter your video link \n")
        name = input("Enter your video name \n")
        print("Downloading starts...\n")
        urllib.request.urlretrieve(url, name)
        print("Download completed..!!")
    except Exception as e:
        print(e)

def install_playlist(url):
    p = Playlist('playlist link')
    for video in p.videos:
        video.streams.first().download()


print("##############################################################\n")
print("This Script is created by: Mohamed Alamrawy \n")
print("##############################################################\n")

print("do you want to install video or playlist or video outside youtube: ")
print("1-video ")
print("2-playlist")
print("2-outside youtube ")

mode = input("")

if mode =="1":
    url = input("Enter video url: \n")
    install_video_from_yotube(url)
    
elif mode =="2":
    url = input("Enter playlist url: \n")
    install_playlist(url)

elif mode =="3":
    url = input("Enter video url: \n")
    name = input("Enter video name: \n")
    install_outside_youtube(url,name)

else:
    print("Enter a valid choose. \n")


  
print("task completed!")
