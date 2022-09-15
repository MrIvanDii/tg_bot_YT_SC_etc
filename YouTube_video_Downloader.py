from pytube import YouTube

#yt = YouTube('https://www.youtube.com/watch?v=p13GxoKvs_0&list=RDp13GxoKvs_0&index=2')
yt = YouTube('https://www.youtube.com/watch?v=sPzqaVqEPPw')

# title = yt.title
# thumbnail_url = yt.thumbnail_url
# info = yt.vid_info
video_quality_info = yt.streams

#print(f'Title: {title}\n Thumbl: {thumbnail_url}\n Info about video: {info}')
#print(f'Quality info: {video_quality_info}')
for i in video_quality_info:
    print(i)

#---------------------------------------------VHS------------------------------------------------

video_hd_144_progressive = yt.streams.filter(resolution="144p", mime_type="video/mp4", progressive="True")
if video_hd_144_progressive:
    print('This is not HD-video, it available in resolution: 144p')

video_hd_360_progressive = yt.streams.filter(resolution="360p", mime_type="video/mp4", progressive="True")
if video_hd_360_progressive:
    print('This is not HD-video, it available in resolution: 360p')

# video without audio
video_hd_480_progressive = yt.streams.filter(resolution="480p", mime_type="video/mp4", progressive="False")
if video_hd_480_progressive:
    print('This is not HD-video, it available in resolution: 360p')

# audio for the video
audio_for_the_video = yt.streams.filter(mime_type="audio/mp4", abr="128kbps")
if audio_for_the_video:
    print('This is not HD-video have separeted audio file')

#--------------------------------------------HD------------------------------------------------

# HD 720
video_hd_720_progressive = yt.streams.filter(resolution="720p", mime_type="video/mp4", progressive="True")
if video_hd_720_progressive:
    print('Video available in resolution HD 720p')

# HD 1080
video_hd_1080p = yt.streams.filter(resolution="1080p", mime_type="video/mp4")
if video_hd_1080p:
    print('Video available in resolution HD 1080p')

# HD 1440
video_hd_1440p = yt.streams.filter(resolution="1440p", mime_type="video/webm")
if video_hd_1440p:
    print('Video available in resolution HD 1440p')

# HD 2160
video_hd_2160p = yt.streams.filter(resolution="2160p", mime_type="video/webm")
if video_hd_2160p:
    print('Video available in resolution HD 2160p')

# audio for HD videos


# downloadProcessor = yt.streams.filter(resolution="1080p", mime_type="video/mp4")
# downloadProcessor.first().download()
#
# audiodownloadprocessor = yt.streams.filter().get_audio_only()
# audiodownloadprocessor.download(filename=f'audio{title}')

download_video = yt.streams.filter(resolution="360p", mime_type="video/mp4", progressive="True")
download_video.first().download('testtestestestestestest.mp4')

# <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="22" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="313" mime_type="video/webm" res="2160p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="271" mime_type="video/webm" res="1440p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="25fps" vcodec="avc1.640028" progressive="False" type="video">
# <Stream: itag="248" mime_type="video/webm" res="1080p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.64001f" progressive="False" type="video">
# <Stream: itag="247" mime_type="video/webm" res="720p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">
# <Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">
# <Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">
# <Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400c" progressive="False" type="video">
# <Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">
# <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
# <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
# <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">
# <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">


# video_hd_720_progressiv = yt.streams.filter(resolution="720p", mime_type="video/mp4", progressive="True")
	# if video_hd_720_progressiv:
	# 	start_buttons.append('HD 720p')
	# else:
	# 	video_hd_360_progressiv = yt.streams.filter(resolution="360p", mime_type="video/mp4", progressive="True")
	# 	if video_hd_360_progressiv:
	# 		start_buttons.append('HD 360p')
	#
	# video_hd_1080p = yt.streams.filter(resolution="1080p", mime_type="video/mp4")
	# if video_hd_1080p:
	# 	start_buttons.append('HD 1080p')
	# else:
	# 	video_hd_144_progressiv = yt.streams.filter(resolution="144p", mime_type="video/mp4", progressive="True")
	# 	if video_hd_144_progressiv:
	# 		start_buttons.append('HD 144p')
	#
	# video_hd_1440p = yt.streams.filter(resolution="1440p", mime_type="video/webm")
	# if video_hd_1440p:
	# 	start_buttons.append('HD 1440p')
	#
	# video_hd_2160p = yt.streams.filter(resolution="2160p", mime_type="video/webm")
	# if video_hd_2160p:
	# 	start_buttons.append('HD 2160p')

	# keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	# keyboard.add(*start_buttons)
	#
	# print(start_buttons)
	# print(link_from_user)




# @dp.message_handler(Text(equals='HD 360p'))
# async def get_the_360p_video(message: types.Message):
#
# 	g.get_the_video_360(link_from_user)
# 	title = g.get_the_video_title(link_from_user)
# 	# yt = YouTube(link_from_user)
# 	# video_hd_360_progressiv = yt.streams.filter(resolution="360p", mime_type="video/mp4", progressive="True")
# 	# video_hd_360_progressiv.first().download(filename='testVIDEOtest.mp4')
#
# 	await message.answer(f'{bot_messages.YT_Video_downloading_144p}')
#
# 	with open(f'{title}.mp4', 'rb') as video:
# 		await message.answer_video(video)
#
# 	os.remove(f'{title}.mp4')
#
# # @dp.message_handler(Text(equals="HD 144p"))
# @dp.message_handler(Text(equals="HD 720p"))
# async def get_the_720p_video(message: types.Message):
# 	g.get_the_video_720(link_from_user)
# 	title = g.get_the_video_title(link_from_user)
#
# 	await message.answer(f'{bot_messages.YT_Video_downloading_144p}')
#
# 	with open(f'{title}.mp4', 'rb') as video:
# 		await message.answer_video(video)
#
# 	os.remove(f'{title}.mp4')
# @dp.message_handler(Text(equals="HD 1080p"))
# @dp.message_handler(Text(equals="HD 1440p"))
# @dp.message_handler(Text(equals="HD 2160p"))