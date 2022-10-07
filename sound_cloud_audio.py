import os
import glob

class GetAudioFromSoundCloud:

    def get_audio_trek(self, url):
        url = url
        comm = f'scdl -l {url} --path saund_cloud_audio_files'
        os.system(comm)

    def get_name_of_file(self):

        file_name = glob.glob('/Users/martinanikola/PycharmProjects/You_Tube_Download_TGbot_DB_Analitic/saund_cloud_audio_files/*.mp3')
        print(file_name)
        return file_name[0]

    def remove_audio_trek(self):
        file = glob.glob('/Users/martinanikola/PycharmProjects/You_Tube_Download_TGbot_DB_Analitic/saund_cloud_audio_files/*.mp3')
        os.remove(file[0])