from downloader import *
import subprocess 
import vlc 

songList = getData(); 


media = None 
def playSong(location):
	# subprocess.Popen(['mpg123', '-q', location.replace("\"","'")]).wait(); 
	global media; 
	if media == None:
		media=vlc.MediaPlayer(location.replace("\"", "'")); 
	else:
		media.stop() 
		media=vlc.MediaPlayer(location.replace("\"", "'")); 
	
	media.play()
	
def addSong(url):
	downloadURL(url); 
	songList = getData(); 


def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def showsongs(mne):
	mne.show() 



def addnewsong():
	url = getClipboardData();
	choice = input(">>>Download {} (y/n)?".format(url)); 
	if choice in ["y","Y"]:
		addSong(str(url).split("\'")[1]);
		refresh_menu(songmenu);


def refresh_menu(mnu):
	mnu.append_item(FunctionItem(songList[-1]["title"], playSong, [songList[-1]["loc"]]))



def load_song_menu(mnu):
	for song in songList:
		mnu.append_item(FunctionItem(song["title"], playSong, [song["loc"]]))
	
# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

# Create the menu
global media; 


songmenu = CursesMenu("Soul-Music", "Song List")
mainmenu = CursesMenu("Soul-Music","Options");
load_song_menu(songmenu);

ft_newsong = FunctionItem("Add New Song", addnewsong); 
ft_showsongs = FunctionItem("Song List", showsongs, [songmenu]);  


subsongs = SubmenuItem("Songs list", songmenu, mainmenu)

mainmenu.append_item(ft_newsong); 
mainmenu.append_item(subsongs); 

mainmenu.show(); 





