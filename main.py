import os
from pytube import YouTube
from pytube import Playlist
from sys import argv
from os import path
from moviepy.video.io.VideoFileClip import VideoFileClip

def Download (video, dl_path):
	print("Downloading | Title:", video.title);
	
	stream = video.streams.get_highest_resolution();
	stream.download(dl_path, stream.default_filename, None, False, 3, 3);

	return stream;

def MP4_to_MP3 (video, dl_path):
	stream = Download(video, dl_path);
	
	video = VideoFileClip(dl_path + stream.default_filename);
	mp3_name = stream.default_filename[:-1] + '3';

	video.audio.write_audiofile(dl_path + mp3_name);
	video.close();
	os.remove(dl_path + stream.default_filename);

if __name__ == "__main__":
	link = argv[1]; #Link to the YouTube video
	turn_to_mp3 = argv[2]; # 1 for converting, 0 otherwise
	dl_path = os.path.join("Downloads/");

	if not (path.exists(dl_path)):
			os.mkdir(dl_path);

	if ("list=" in link):
		video_list = Playlist(link);

		for video in video_list.videos:

			if (turn_to_mp3 == "1"):
				MP4_to_MP3(video, dl_path);
			else:
				Download(video, dl_path);
	else:	
		video = YouTube(link);

		if (turn_to_mp3 == "1"):
			MP4_to_MP3(video, dl_path);
		else:
			Download(video, dl_path);
