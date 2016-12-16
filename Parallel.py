import tempfile
import urllib
import java.lang
import time

firstvisit = 0
introcanvas = ""
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
    global firstvisit
    userName = requestString("Hello, What do you call yourself?")      
    if (userName == " "  ):
      userName = "Lonely"
    return userName

def introChoice():
    fistState = true
    while(fistState == true):
      choice = requestString("What is your choice?")       
      if (choice == "p" or choice == "P"):     
         fistState = false      
      elif (choice == "i" or choice == "I"):
         introCanvas=getMedia("img","info5") 
         fistState = false 
      else :
         fistState = true 
    return introCanvas          

def gameEngine(): 
    introSong=getMedia("wav","intro1")
    introCanvas=getMedia("img","menu")
    show(introCanvas)
    play(introSong)
    name=intro()
    introCanvas=introChoice()        
    repaint(introCanvas)
    introCanvas=getMedia("img","menu")
    repaint(introCanvas)
         