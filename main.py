import os
from pytube import YouTube
from sys import argv
from os import path
from moviepy.video.io.VideoFileClip import VideoFileClip

link = argv[1]; #Link to the YouTube video
turn_to_mp3 = argv[2]; # 1 for converting, 0 otherwise
yt = YouTube(link);

print("Title:", yt.title, "| Views: ", yt.views);

yd = yt.streams.get_highest_resolution();

dl_path = "./Downloads/";
if not (path.exists(dl_path)):
	os.mkdir(dl_path);
yd.download(dl_path);

if (turn_to_mp3 == "1"):
	video = VideoFileClip(dl_path + yt.title + ".mp4");
	audio = video.audio;
	audio.write_audiofile(dl_path + yt.title + ".mp3");
elif (turn_to_mp3 == "0"):
	exit();