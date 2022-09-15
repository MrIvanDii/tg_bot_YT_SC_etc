import moviepy.editor as mp
from moviepy.video.fx import resize

video = mp.VideoFileClip("../media_files/MINECRAFT 1ST DAY || MINECRAFT GAMEPLAY || MINECRAFT SURVIVAL SERIES.mp4", target_resolution=(480, 854))

new_video = video.subclip(t_start=0)
#newClip = resize('../MINECRAFT 1ST DAY || MINECRAFT GAMEPLAY || MINECRAFT SURVIVAL SERIES.mp4', width=854, height=480)

new_video.write_videofile("../vid_test.mp4")