from moviepy.editor import *

audio = AudioFileClip("../media_files/audioalyona alyona x Jerry Heil x Monika Liu - Dai Boh.mp3")
video = VideoFileClip("../media_files/alyona alyona x Jerry Heil x Monika Liu - Dai Boh.mp4")

new_video = video.subclip(t_start=0)
new_audio = audio.subclip(t_start=0)

new_video.audio = new_audio
new_video.write_videofile("vid_test.mp4")
