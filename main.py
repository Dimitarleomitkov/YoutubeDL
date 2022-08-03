import os
from pytube import YouTube
from sys import argv
from os import path

link = argv[1];
yt = YouTube(link);

print("Title:", yt.title, "| Views: ", yt.views);

yd = yt.streams.get_highest_resolution();

dl_path = "./Downloads/";
if not (path.exists(dl_path)):
	os.mkdir(dl_path);
yd.download(dl_path);