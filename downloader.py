# Helper functions to download content from youtube 

import youtube_dl

from pathlib import Path
home = str(Path.home())

import json 

songList = []; 

def getData():
	with open("data.json") as f:
		data = f.read(); 

	return json.loads(data); 

def pushData(arr):
	with open("data.json", mode='w', encoding='utf-8') as f:
		json.dump(arr,f); 
 	

def isUnique(arr, name):
	for song in arr: 
		if song["title"] == name:
			return False 
	return True 

def downloadURL(url, preferredCodec=None, preferredQuality=None):
    """ Downloads song using youtube_dl and the song's youtube
    url.
    """

    ydl_opts = {
    	'outtmpl': home+'/Music/Songs/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': "mp3",
            'preferredquality': "192",
        },
            {'key': 'FFmpegMetadata'},
        ],
    }



    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    	data = ydl.extract_info(url, download=False) 
    	songTitle = data['title']; 
    	songLoc = home+"/Music/Songs/"+songTitle+".mp3"; 
    	songList = getData()


    	if isUnique(songList, songTitle):
    		print("Downloading song, please wait..."); 
    		ydl.extract_info(url, download=True) 
    		print("Done...");
    		songList.append({"title": songTitle, "loc": songLoc});     		
    		pushData(songList)
    	else:
    		print("song already exists")

