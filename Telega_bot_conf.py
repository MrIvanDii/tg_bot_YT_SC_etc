from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
import os
import time
from tools import bot_messages
from tools.configurations_data import BOT_TOKEN
from get_video_audio_from_YT import GetTheVideoAudio
from sound_cloud_audio import GetAudioFromSoundCloud
from tic_tock import TikTokGet

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

g = GetTheVideoAudio()
sc_audio = GetAudioFromSoundCloud()
ti_to = TikTokGet()

hide_buttons = types.ReplyKeyboardRemove()
time_to_wait = 2


# Answer_after /start button
@dp.message_handler(commands="start")
async def start(message: types.Message):
	await message.answer(f'{bot_messages.welcome_message}')


# Getting and sending an Audio from Sound Cloud
@dp.message_handler(regexp="^(?:(https?):\/\/)?(?:(?:www|m)\.)?(soundcloud\.com|snd\.sc)\/(.*)$")
async def get_audio_sound_cloud(message: types.Message):
	await message.answer(f'{bot_messages.YT_Video_processing_request}')

	cloud_link_from_user = message.text
	sc_audio.get_audio_trek(cloud_link_from_user)
	file_name = sc_audio.get_name_of_file()

	with open(file_name, 'rb') as audio:
		await message.answer_audio(audio)

	sc_audio.remove_audio_trek()


# Getting and sending an Audio from YouTube
@dp.message_handler(regexp="^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")
async def getting_link_from_user(message: types.Message):

	await message.answer(f'{bot_messages.YT_Video_processing_request}')

	global link_from_user

	link_from_user = message.text

	g.get_the_audio_128(link_from_user)
	title = g.get_the_video_title(link_from_user)

	with open(f'media_files/{title}.mp3', 'rb') as audio:
		await message.answer_audio(audio)
		os.remove(f'media_files/{title}.mp3')

	await message.answer(f'{bot_messages.some_more}')


# INSTA
@dp.message_handler(Text(equals="Instagram"))
async def choose_youtube_platform(message: types.Message):
	await message.answer(f'{bot_messages.choose_INST_platform_answer}')


# Getting and sending video from TIKTOK by link
@dp.message_handler(regexp='^(?:(https?):\/\/)?(?:(?:www|m)\.)?(tiktok\.com)?(\/@[a-zA-Z0-9._-]+)?(\/video)?(\/[0-9]{19})')
async def get_audio_from_tik_tok(message: types.Message):
	await message.answer(f'{bot_messages.TT_Video_downloading_answer}')

	os.system(f'python get_video_from_TikTok.py {message.text}')
	file_name = ti_to.get_author_name(message.text)

	time.sleep(time_to_wait)

	try:
		with open(f'tik_tok_videos/{file_name}', 'rb') as audio:
			await message.answer_video(audio)

	except Exception as _FileNotFoundError:
		print('Error: ', _FileNotFoundError)
		time.sleep(time_to_wait)

		try:
			with open(f'tik_tok_videos/{file_name}', 'rb') as audio:
				await message.answer_video(audio)

		except Exception as _FileNotFoundError:
			print('STILL NO FILE', _FileNotFoundError)

	ti_to.remove_file()


def main():
	executor.start_polling(dp)


if __name__ == "__main__":
	main()
