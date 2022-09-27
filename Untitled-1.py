
from cProfile import label
from cgitb import text
from pytube import YouTube
from tkinter import ttk
from tkinter import *
root=Tk()
root.geometry("500x500")








def download720p():
    def get_stream_for_res(streams, res):
        stream = list(filter(lambda x: x.resolution == res, streams))
        return stream
    video_url = url.get()
    youtube_obj = YouTube(video_url)
    video_res = "144p"
    req_stream_obj = get_stream_for_res(youtube_obj.streams, video_res)[1]
    req_stream_obj.download("C:\\Users\\admin\\Desktop\\proge\\youtube")
    label(root,text="download finich").pack()
    


Label(root,text="Download YouTube").pack()
url = Entry(root).pack()







Button(root, text="Download 144p",command=download720p).pack()
root.mainloop()
