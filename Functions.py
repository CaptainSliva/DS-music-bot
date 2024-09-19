
import yt_dlp

# from __future__ import unicode_literals
# import youtube_dl
import moviepy.editor as mp
import os
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time


# def get_audio(link):
#     yt = pytube.YouTube(link)
#     path = 'C:/Users/Дима/Documents/VSCode/Мелкопроекты/DS_music_bot'
#     # try:
#     # yt.streams.filter(only_audio=True)
#     # stream = yt.streams.get_by_itag(22)
#     # name = stream.download(path)
#     name = 'Alan Walker - Faded [60ItHLz5WEA].mp4'
#     ydl_opts = {
#         'format': 'best', 
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([link])
#     print("downloaded", link)
    
#     # print(name)
#     soundpath = path
#     # soundname = name.split('\\')[1].split('.')[0]
#     soundname = 'Alan Walker - Faded [60ItHLz5WEA]'
    
#     if f'{soundpath}/{soundname}.mp3' not in os.listdir():
#         print(soundname)
#         mp.VideoFileClip(name).audio.write_audiofile(f'{soundname}.mp3')
#         os.remove(name)
#     print(f'{soundpath}/{soundname}.mp3')
#     return f'{soundpath}/{soundname}.mp3'
#     # except:
#     #     print('Ещё попытка')
#     #     get_audio(link)

# print(get_audio('https://www.youtube.com/watch?v=60ItHLz5WEA'))

from selenium import webdriver
driver = webdriver.Firefox()
# def get_audio(name, link):
#     # yt = pytube.YouTube(link)
#     path = 'C:/Users/Дима/Documents/VSCode/Мелкопроекты/DS_music_bot'
#     # try:
#     # yt.streams.filter(only_audio=True)
#     # stream = yt.streams.get_by_itag(22)
#     # name = stream.download(path)
#     print('видео начал качать')
    
    
#     ydl_opts = {
#         'format': 'best', 
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([link])
#     print("DOWNLOADED", link)
#     print('видео скачал')

#     name = str([i for i in os.listdir() if name in i.replace('＂', '').replace('？', '?').replace('｜', '|')][0])
#     print(name)
#     soundpath = path

#     # soundname = name.split('\\')[1].split('.')[0]
#     soundname = name.split(' [')[0].replace('＂', '')
#     print('начало конвертации в звук')
#     if f'{soundpath}/{soundname}.mp3' not in os.listdir():
#         print(name)
#         print(soundname)
#         mp.VideoFileClip(name).audio.write_audiofile(f'{soundname}.mp3')
# # "Dr.Dre - Nuthin' but a ＂G＂ Thang [dwWUXZtv2C0].mp4"
# # "Dr.Dre - Nuthin' but a &quot;G&quot; Thang "

# # 'Рей - Мимо Поста ГИБДД [vu60a72YN6Y].mp4'
# # 'Рей - Мимо Поста ГИБДД '
        
#     print('путь')
#     print(f'{soundpath}/{soundname}.mp3')
#     # os.remove(name)
#     return f'{soundpath}/{soundname}.mp3'



def get_audio(name_and_link):
    # yt = pytube.YouTube(link)
    print(name_and_link)
    soundname = name_and_link[0]
    link = name_and_link[1]
    soundpath = 'C:/Users/Дима/Documents/VSCode/Мелкопроекты/DS_music_bot'

    print('видео начал качать')
    #-----------------------------------!
    if os.path.exists(soundname):
        os.remove(soundname)
    # audio_downloader = yt_dlp.YoutubeDL({'format':'mp3/bestaudio', 'outtmpl' : soundname})
    # audio_downloader.extract_info(link) хрень
    #-----------------------------------!
    ydl_opts = {
    # 'format': 'bestaudio/best',
    'format':'mp3/bestaudio',
    'outtmpl': soundname,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


    # name = str([i for i in os.listdir() if name in i.replace('＂', '').replace('？', '?').replace('｜', '|')][0])

    print(soundname)
 


    print('путь')
    # print(f'{soundpath}/{soundname}.mp3')
    # os.remove(name)
    return f'{soundpath}/{soundname}.mp3'

def find_video(v):
    global driver
    dir_name = os.getcwd()
    files = os.listdir(dir_name)
    for item in files:
        if item.endswith(".mp3"):
            os.remove(os.path.join(dir_name, item))
    print(v)
    url = f'https://www.youtube.com/results?search_query={v}'
    
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    # print(html)
    soup = BS(html, "html.parser")
    # print(soup)

    videos = soup.find_all('a', class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
    video_link = str()
    video_name = str()
    # print(videos)

    for video in videos[:1]:
        try:
            video_name = str(video).split('aria-label=')[1][1:-1].split('Автор')[0].replace('"', '')
            video_link = 'https://www.youtube.com'+str(video).split('href="')[1].split('"')[0]
            print(video_name+video_link)
        except:
            print("ERROR!")
    print('спарсил')
    print(video_name+video_link)
    # if (len(video_name) > 0) and (len(video_link) > 0):
    return [video_name, video_link]
    # else:
        # return ['дура', 'https://www.youtube.com/watch?v=WNadEfGnV04&pp=ygUHbGpobGVoZg%3D%3D']

# a = 'vbvjgjcnfub,ll'
# b = 'https://www.youtube.com/watch?v=vu60a72YN6Y&amp;pp=ygUOdmJ2amdqY25mdWIsbGw%3D'
# print(find_video(a))
# import re

# def refactor_song_url(message):
#     '''Обработка ссылки в нужный формат'''
#     if '&' in message:
#         song_url = re.sub(r'&[\w\S]*', '', message)
#         print(song_url, 're')
#     elif 'youtu.be' in message:
#         song_url = re.sub('youtu.be/', 'www.youtube.com/watch?v=', message)
#         print(song_url, 'be')
#     else:
#         song_url = message
#         print(song_url, 'oke')
#     return song_url.split('watch?v=')[-1]
# print(refactor_song_url(b))

# def Song(song_url, song_title):
#     '''Обработка видео из Ютуб в аудио файл'''
#     outtmpl = song_title
#     ydl_opts = {
#         'format': 'm4a/bestaudio/best',
#         'outtmpl': outtmpl,
#         'postprocessors': [
#             {'key': 'FFmpegExtractAudio',
#              'preferredcodec': 'm4a',
#              'preferredquality': '192'},
#             {'key': 'FFmpegMetadata'},
#         ],
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([song_url])  # Скачивание видео в виде m4a файла

# Song('https://www.youtube.com/watch?v=vu60a72YN6Y&amp;pp=ygUOdmJ2amdqY25mdWIsbGw%3D', 'гедее')
# https://www.youtube.com/watch?v=vu60a72YN6Y
# https://www.youtube.com/watch?v=vu60a72YN6Y&pp=ygUOdmJ2amdqY25mdWIsbGw%3D
# https://www.youtube.com/watch?v=WNadEfGnV04&pp=ygUIbGpoZmxlaGY%3D
# print(Song('https://www.youtube.com/watch?v=WNadEfGnV04&pp=ygUIbGpoZmxlaGY%3D', 'dd'))