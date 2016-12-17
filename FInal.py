import tempfile
import random
import urllib
import java.lang
import time

board 
#OS Detection
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
		#Creates a temp holder folder for windows
		tempFilePath = "C:\\Windows\\Temp\\" + fileName + suffix
	else:
		#Creates a temp holder folder for mac
		tempFilePath = tempfile.gettempdir() + fileName + suffix

	url = "https://github.com/alphabin/CSUMB-ABSTRACTFACTORY/raw/master/Resources/"+ fileName + suffix
	data = urllib.urlretrieve(url, tempFilePath)

	if mediaType == "img":
		myMedia = makePicture(tempFilePath)
	else:
		myMedia = makeSound(tempFilePath)
	return myMedia
 
 

def playGame():

  global board
  global guess
  global guess_x
  global guess_y
  global xCoordinate
  global yCoordinate
  global hint
  global gamePlay
  
  
  
  soungStart = getMedia("wav","movearound")
  file1 = getMedia("img","NEWboard")
  file2 = getMedia("img","NEWguess")
  file3 = getMedia("img","win")
  file4 = getMedia("img","loose")
  
  
  boardorig = file1
  guess = file2
  win = file3
  lose = file4
  
  style = makeStyle(sansSerif, bold, 25)
  
  xCoordinate = random.randint(1,10)
  yCoordinate = random.randint(1,10)
  
  introSong=getMedia("wav","intro1")
  board=getMedia("img","menu")
  show(board)
  play(introSong)
  x=true
  while(x !=false):
    fileX = getMedia("img","menu")
    copy(board,fileX)
    repaint(board)
    name=intro()
    userDecison=introChoice()         
    repaint(board)
    if (userDecison=="Z" or userDecison=="Y"):    
      repaint(board)
      time.sleep(5)
      x=true
    elif (userDecison=="X"):
      x=false 
  stopPlaying(introSong)
  
  
  guess_x = 0
  guess_y = 0
  count = 0
  gamePlay = 0
  
  hint = ""
  
  board = copy(board,file1)
  repaint(board)
 
  while count < 8:
    
    showInformation(str(yCoordinate) + " " + str(xCoordinate))
 
    guess_y = int(requestString("Guess Row:"))
    guess_x = int(requestString("Guess Col:"))
    play(soungStart)
    count = count + 1
    
    mapx = xcordinate(guess_x)
    mapy = ycordinate(guess_y)
    
    userGuess()
    
    board = greenScreen(guess, board, mapx, mapy)
    addTextWithStyle(board, 215, 115, hint, style, white)
    addTextWithStyle(board, 441, 120, "try: " + str(count), style, white)
    repaint(board)
    board = copy(board, boardorig)
    
    if "loading" in hint:
      break
    
    
  if guess_y == yCoordinate and guess_x == xCoordinate:
    winSound = getMedia("wav","win1")
    play(winSound)
    board = copy(board, win)
    repaint(board)
  else:
    looseSound = getMedia("wav","loose1")
    play(looseSound)
    board = copy(board, lose)
    repaint(board)
  
def userGuess():

  global guess_x
  global guess_y
  global xCoordinate
  global yCoordinate
  global hint
  global gamePlay

  # create lihrt clues

  if guess_x == xCoordinate and guess_y == yCoordinate:
    hint = " loading... "

  elif guess_x == xCoordinate:
    if guess_y > yCoordinate:
      hint = "   Go South  "
  
    elif guess_y < yCoordinate:
      hint = "   Go North  " 
    
  elif guess_y == yCoordinate:
    if  guess_x < xCoordinate:
      hint = "   Go East  "

    elif  guess_x > xCoordinate:
      hint = "   Go West  "
        
  elif guess_y < yCoordinate:
    if guess_x < xCoordinate:
        hint = "Go northeast"
    elif guess_x > xCoordinate:
        hint = " Go northwest"
      
  elif guess_y > yCoordinate:
    if guess_x < xCoordinate:
        hint = "Go southeast"
       
    elif guess_x > xCoordinate:
        hint = " Go southwest"
        
def greenScreen(source, target, tx, ty):
  width = getWidth(source)
  height = getHeight(source)
  backgreen = makeColor(67, 216, 0)
  for x in range(0, width):
    for y in range(0, height):
      oldPixel = getPixel(source, x, y)
      newPixel = getPixel(target, tx + x, ty + y)     
      color = getColor(oldPixel)
      color2 = getColor(newPixel)
      if (distance(color, backgreen) > 50.00):
        setColor(newPixel, color)
      
  return target
  
def copy(source, target):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      newPixel = getPixel(target, x, y)     
      color = getColor(newPixel)
      setColor(getPixel(source, x, y) , color)
      
  return source
  
def xcordinate(x):
  startx = 57

  if x > 1:
    for i in range(0, (x - 1)):
      startx = startx + 50

  return startx

def ycordinate(y):
  starty = 590
  
  if y > 1:
    for i in range(0, (y - 1)):
      starty = starty - 50

  return starty


def intro():
    global firstvisit
    userName = requestString("Hello, What do you call yourself?")      
    if (userName == " "  ):
      userName = "Lonely"
    return userName

def introChoice():
    global board
    fistState = true  
    i =""
    while(fistState == true):
      choice = requestString("What is your choice?")       
      if (choice == "p" or choice == "P"):     
         fistState = false  
         i="X"
         board=copy(board,getMedia("img","NEWboard"))   
      elif (choice == "i" or choice == "I"):         
         fistState = false 
         i="Y"
         board=copy(board,getMedia("img","NEWinfo"))
      else :
         fistState = true  
         i="Z"
         board=copy(board,getMedia("img","menu"))    
    return i  


                                                                    