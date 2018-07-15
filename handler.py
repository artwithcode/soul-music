import json 

class Handler(object):
 	"""Handles song data"""
	def __init__(self):
		self.songList = None; 
 		
	def getData(self):
		# open data.json file 
		with open("data.json") as f:
			data = f.read();

		self.songList = json.loads(data); 

	def putData(self, song): 
		songEntry = {'name':song.name, 'location':song.location}; 
		self.songList.append(songEntry); 


	def flushData(self):
		with open("data.json", "W", encoding="utf-8") as f:
			json.dumps(self.songList, f); 


class Song(object):
	def __init__(self,name,location):
		self.name = name; 
		self.location = location; 

 		 

