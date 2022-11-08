from youtube_search import YoutubeSearch
import webbrowser
import speech_recognition
from pyttsx3 import *
from tkinter import *

window=Tk()
txt_timkiem = Entry(window,width=25,bd=15)
def robot_say(txt):
    a = init()
    a.say(txt)
    a.runAndWait()
def init_robot_ear():
    robot_ear = speech_recognition.Recognizer()
    return robot_ear
def robot_listening():
    robot_ear=init_robot_ear()
    with speech_recognition.Microphone() as mic:
        robot_say("I'm Listening")
        audio = robot_ear.record(mic, duration=5)
        robot_say("Done Listening")
    try:
        mysong = robot_ear.recognize_google(audio,language="vi-VN")
    except:
        mysong = ""
    return mysong
def list_info():
    mysong = robot_listening()
    if mysong=="":
        result=""
    else:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
    return result
def open_youtube():
    result = list_info()
    if result == "":
        url = 'https://www.youtube.com'
    else:
        url = 'https://www.youtube.com'+ result[0]['url_suffix']
    webbrowser.open(url)
    robot_say("Have fun watching the video")
def list_info_hand():
    mysong=txt_timkiem.get()
    if mysong == "":
        result = ""
    else:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
    return result
def open_youtube_hand():
    result = list_info_hand()
    if result == "":
        url = 'https://www.youtube.com'
    else:
        url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    robot_say("Have fun watching the video")
def out():
    exit()
def GUI():
    window.title("Open video on youtube")
    window.geometry("450x250")
    window.iconbitmap('icon.ico')
    lbl_timkiem=Label(window,text="Nhập từ khóa:",bg="blue",fg="white",font=("Arial,15"),height=2)
    lbl_timkiem.grid(column=1,row=1)
    txt_timkiem.grid(column=2,row=1)
    btn_timkiem = Button(window, text="Tìm Kiếm", command=open_youtube_hand,height=2,bg="red",font=("Arial,1"))
    btn_timkiem.grid(column=3, row=1)
    btn_timkiem=Button(window,text="Nhấn để nói",command=open_youtube,height=2,bg="red",bd=12,font=("Arial,15"))
    btn_timkiem.grid(column=2,row=2)
    btn_thoat = Button(window, text="   Thoát   ", command=out,height=2,bg="red",bd=12,font=("Arial,15"))
    btn_thoat.grid(column=2, row=6)
    window.mainloop()
GUI()