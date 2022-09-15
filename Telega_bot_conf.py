from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
import os
import glob
from pytube import YouTube
from tools import bot_messages
from tools.configurations_data import BOT_TOKEN
from get_video_audio_file import GetTheVideoAudio
from sound_cloud_audio import GetAudioFromSoundCloud

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
g = GetTheVideoAudio()
sc_audio = GetAudioFromSoundCloud()

hide_buttons = types.ReplyKeyboardRemove()

# Audio_or_Video?->
@dp.message_handler(commands="start")
async def start(message: types.Message):

	start_buttons = ["Download Audio", "Download Video"]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer(f'{bot_messages.welcome_message}', reply_markup=keyboard)

# Video-> Instagram_or_Tik-Tok ?
@dp.message_handler(Text(equals="Download Video"))
async def start(message: types.Message):

	start_buttons = ["Instagram", "Tic-Tock"]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer(f'{bot_messages.video}', reply_markup=keyboard)

# Audio-> YouTube_or_SoundCloud ?
@dp.message_handler(Text(equals="Download Audio"))
async def start(message: types.Message):

	start_buttons = ["From YouTube", "From SoundCloud"]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer(f'{bot_messages.audio}', reply_markup=keyboard)

# -------------------------------------------------------------------------------------------------

# Audio-> Youtube-> Link?
@dp.message_handler(Text(equals="From YouTube"))
async def choose_youtube_platform(message: types.Message):
	await message.answer(f'{bot_messages.YT_Video_button}', reply_markup=hide_buttons)

# Audio-> SoundCloud-> Link?
@dp.message_handler(Text(equals="From SoundCloud"))
async def choose_youtube_platform(message: types.Message):
	await message.answer(f'{bot_messages.SoundCloud_Audio_button}', reply_markup=hide_buttons)

# Audio-> SoundCloud-> Link-> ok?
@dp.message_handler(regexp="^(?:(https?):\/\/)?(?:(?:www|m)\.)?(soundcloud\.com|snd\.sc)\/(.*)$")
async def get_audio_sound_cloud(message: types.Message):

	cloud_link_from_user = message.text
	sc_audio.get_audio_trek(cloud_link_from_user)
	file_name = sc_audio.get_name_of_file()

	with open(file_name, 'rb') as audio:
		await message.answer_audio(audio)

	sc_audio.remove_audio_trek()


# Audio-> Youtube-> Link-> Choose_the_quality?
@dp.message_handler(regexp="^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")
async def getting_link_from_user(message: types.Message):

	await message.answer(f'{bot_messages.YT_Video_processing_request}')

	global link_from_user

	link_from_user = message.text
	yt = YouTube(link_from_user)
	start_buttons = []

	audio_128 = yt.streams.filter(abr="128kbps", mime_type="audio/mp4")
	if audio_128:
		start_buttons.append('Download in Quality: 128kbps')

	audio_256 = yt.streams.filter(abr="256kbps", mime_type="audio/mp4")
	if audio_256:
		start_buttons.append('Download in Quality: 256kbps')

	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer(f'{bot_messages.YT_Audio_quality_question}', reply_markup=keyboard)


# Audio-> Youtube-> Link-> Choose_the_quality-> Get_the_file -> Some more tasks?
@dp.message_handler(Text(equals='Download in Quality: 128kbps'))
async def get_the_360p_video(message: types.Message):

	await message.answer(f'{bot_messages.YT_Audio_downloading_}', reply_markup=hide_buttons)

	g.get_the_audio_128(link_from_user)
	title = g.get_the_video_title(link_from_user)

	with open(f'{title}.mp3', 'rb') as audio:
		await message.answer_audio(audio)
		os.remove(f'media_files/{title}.mp3')

	await message.answer(f'{bot_messages.some_more}')


# Audio-> Youtube-> Link-> Choose_the_quality-> Get_the_file -> Some more tasks-> Yes
# @dp.message_handler(Text(equals='Yes'))
# @dp.message_handler(Text(equals="From YouTube"))



# @dp.message_handler(Text(equals="HD 144p"))
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


# -------------------------------------------------------------------------------------------------

# INSTA
@dp.message_handler(Text(equals="Instagram"))
async def choose_youtube_platform(message: types.Message):
	await message.answer(f'{bot_messages.choose_INST_platform_answer}')


# TICTOK
@dp.message_handler(Text(equals="Tic-Tock"))
async def choose_youtube_platform(message: types.Message):
	await message.answer(f'{bot_messages.choose_TT_platform_answer}')


def main():
	executor.start_polling(dp)


if __name__ == "__main__":
	main()
