import tempfile
import urllib
import java.lang
import time



def getOS():
	os = ""
	ver = sys.platform.lower()
	ver = java.lang.System.getProperty("os.name").lower()
	if ver.startswith('mac'):
		os = "mac"
	if ver.startswith('win'):
		os = "win"
	return os


def getMedia(mediaType, fileName):
	suffix = ""
	if mediaType == "img":
		suffix = ".png"
	else:
		suffix = ".wav"

	if getOS() == "win":
		#windows
		tempFilePath = "C:\\Windows\\Temp\\" + fileName + suffix
	else:
		#mac/linux
		tempFilePath = tempfile.gettempdir() + fileName + suffix

	url = "https://github.com/alphabin/CSUMB-ABSTRACTFACTORY/raw/master/Resources/"+ fileName + suffix
	data = urllib.urlretrieve(url, tempFilePath)

	if mediaType == "img":
		myMedia = makePicture(tempFilePath)
	else:
		myMedia = makeSound(tempFilePath)
	return myMedia
 
def intro():
    introSong=getMedia("wav","intro1")
    introCanvas=getMedia("img","menu")
    select = false
    while (select == false):
      play(introSong)
      show(introCanvas)
    



def gameEngine():
    intro() 
         
         
         