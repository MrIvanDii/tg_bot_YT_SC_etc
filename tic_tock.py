from TikTokAPI import TikTokAPI
import glob
import re
import os

class TikTokGet:

    def get_tik_video(self, video_url):

        path_for_videos = '/Users/martinanikola/PycharmProjects/You_Tube_Download_TGbot_DB_Analitic/tik_tok_videos'
        api = TikTokAPI()
        video_id = self.get_id_video_from_url(video_url)
        author_name = self.get_author_name(video_url)
        api.downloadVideoById(video_id, save_path=f'{path_for_videos}/{author_name}')

    def get_id_video_from_url(self, url):
        url_id = re.findall('[0-9]{19}', url)
        return url_id[0]

    def get_author_name(self, url):
        name = re.findall('@[a-zA-Z0-9._-]+', url)
        return f'video_by:_({name[0]}).mp4'


    def remove_file(self):
        path_for_videos = '/Users/martinanikola/PycharmProjects/You_Tube_Download_TGbot_DB_Analitic/tik_tok_videos'
        file = glob.glob(f'{path_for_videos}/*.mp4')
        os.remove(file[0])