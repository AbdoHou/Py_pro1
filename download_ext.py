from os import path
from pytube import *
from pytube.cli import on_progress
from pathlib import Path
from os.path import join

#def on_progress(stream,chunk,file_handle,bytes_remaining):
   # print(round((1-bytes_remaining/video.filesize)*100,3),'% done...')
video_url = input("get url :")
youtube_obj = YouTube(video_url,on_progress_callback= on_progress)

for stream in youtube_obj.streams.order_by('resolution'):
    print(stream.resolution +" : "+ stream.subtype + " - "+stream.type)
    
resolu = input("Resolution :")
type_vid =input("Type of video :")
strea=youtube_obj.streams.filter(resolution=resolu,subtype=type_vid).last()
strea.download("C:\\Users\\admin\\Desktop\\proge\\youtube")
print("ok")

#youtube_obj.streams.filter(res=resolu,file_extension=type_vid).first().download(path)
#video = youtube_obj.streams.filter(res=resolu,file_extension=type_vid).first()

#print("okk")


