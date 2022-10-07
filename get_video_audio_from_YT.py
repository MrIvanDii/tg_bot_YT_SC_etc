from pytube import YouTube

class GetTheVideoAudio:

    def get_the_video_360(self, url):

        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="360p", mime_type="video/mp4", progressive="True")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')


    def get_the_video_144(self, url):
        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="144p", mime_type="video/mp4", progressive="True")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')


    def get_the_video_720(self, url):
        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="720p", mime_type="video/mp4", progressive="True")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')


    def get_the_video_1080(self, url):
        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="1080p", mime_type="video/mp4")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')


    def get_the_video_1440(self, url):
        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="1440p", mime_type="video/mp4")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')


    def get_the_video_2160(self, url):
        yt = YouTube(url)

        video_title = yt.title
        download_video = yt.streams.filter(resolution="2160p", mime_type="video/mp4")
        download_video.first().download(filename=f'{video_title}.mp4', output_path='media_files')

    def get_the_video_title(self, url):
        yt = YouTube(url)
        video_title = yt.title

        return video_title

    def get_the_audio_title(self, url):
        yt = YouTube(url)
        audio_title = yt.title

        return audio_title

    def get_the_audio_128(self, url):
        yt = YouTube(url)

        audio_title = yt.title
        download_audio = yt.streams.filter(abr="128kbps", mime_type="audio/mp4").first()
        download_audio.download(filename=f'{audio_title}.mp3', output_path='media_files')

    def get_the_audio_256(self, url):
        yt = YouTube(url)

        audio_title = yt.title
        download_audio = yt.streams.filter(abr="256kbps", mime_type="audio/mp4")
        download_audio.download(filename=f'{audio_title}.mp3', output_path='media_files')