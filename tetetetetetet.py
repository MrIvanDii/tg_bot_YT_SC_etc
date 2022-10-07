# import re
#
url = 'https://www.tiktok.com/@sound_rt/video/7129927689800011013?_t=8VrmpUbRnuw&_r=1'
url2 = 'https://www.tiktok.com/@crzwy/video/7140461393312025862?_t=8VwuTsu0c5u&_r=1'
url3 = 'https://www.tiktok.com/@quixxxwtf/video/7146693876588367150?_t=8VwuV6p9OiL&_r=1'
url4 = 'https://www.tiktok.com/@mr.benz/video/7129606392515661062?_t=8VwucRimQwn&_r=1'
#
# urls = [url, url2, url3, url4]
#
# for ur in urls:
#     ur_id = re.findall('[0-9]{19}', ur)
#     name = re.findall('/@([a-zA-Z0-9._-]+)/', ur)
#     print(ur)
#     print('name:', name, 'id:', ur_id)

from tic_tock import TikTokGet

bot = TikTokGet()

bot.get_tik_video(url2)
#bot.get_tik_video_no_watermark(url)

# import requests
#
# headers = {
#             'Host': 't.tiktok.com',
#             'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
#             'Referer': 'https://www.tiktok.com/',
#             'Cookie': 'tt_webid_v2={}; tt_webid={}'.format('6913027209393473025', '6913027209393473025')
#         }
#
# def get_req_content(url, params=None, headers=None):
#     headers["Host"] = url.split("/")[2]
#     print(headers)
#     r = requests.get(url, params=params, headers=headers)
#
#     with open('videooooo.mp4', 'wb') as f:
#         f.write(r.content)
#
#
# get_req_content(url, headers=headers)