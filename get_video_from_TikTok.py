import argparse
from tic_tock import TikTokGet

bot = TikTokGet()

parser = argparse.ArgumentParser()
parser.add_argument("url", type=str)
args = parser.parse_args()

bot.get_tik_video(args.url)