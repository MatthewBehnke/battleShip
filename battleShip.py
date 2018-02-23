import replit
class Matrix():
  def __init__(self):  #init for Matrix class 
    self.grid =['00','1','2','3','4','5',
                '01','0','0','0','0','0',
                '02','0','0','0','0','0',
                '03','0','0','0','0','0',
                '04','0','0','0','0','0',
                '05','0','0','0','0','0',
                '06','N','N','N','N','N',
                '07','0','0','0','0','0',
                '08','0','0','0','0','0',
                '09','0','0','0','0','0',
                '10','0','0','0','0','0',
                '11','0','0','0','0','0']
    self.score = 0
    self.distance = 0

playerOne = Matrix()
playerTwo = Matrix()

def lookUp(iVal, bVal):
  if iVal == 0 and bVal == 0:
    return 0 
  else:
    return (iVal*6)  + bVal

def printMatrix(player):
  for i in range(12):
    print [player.grid[lookUp(i,b)] for b in range(6)]

def updateMatrix(value, xVal, yVal, player):
  place = lookUp(yVal,xVal)  
  player.grid[place] = value
  
def checkMarix(x, y, player, value):
  if player.grid[lookUp(y, x)] == str(value):
    return True
  else:
    return False

def distance(player, x1,y1,x2,y2):
  player.distance = 0
  isHorizontal = False
  isVertical = False
  if x1 == x2:
    isHorizontal = False
    isVertical = True
    if y2 > y1:
      isBackwards = False
      distance = y2 - y1 + 1
    else:
      isBackwards = True
      distance = y1 - y2 + 1
  elif y1 == y2:
    isVertical = False
    isHorizontal = True
    if x2 > x1:
      isBackwards = False
      distance = x2 - x1 + 1
    else:
      isBackwards = True
      distance = x1 - x2 + 1
  if x1 != x2 and y1 != y2:
    print 'provid valid coordinate points'
  else:
    player.distance = distance
  

def placeShip(player, x1, y1, x2, y2):
  isHorizontal = False
  isVertical = False
  if x1 == x2 and y1 == y2:
    print 'Ship can not be placed on it self'
  elif x1 == x2:
    isHorizontal = False
    isVertical = True
    if y2 > y1:
      isBackwards = False
      distance = y2 - y1 + 1
    else:
      isBackwards = True
      distance = y1 - y2 + 1
  elif y1 == y2:
    isVertical = False
    isHorizontal = True
    if x2 > x1:
      isBackwards = False
      distance = x2 - x1 + 1
    else:
      isBackwards = True
      distance = x1 - x2 + 1
  else:
    print 'Ship cannot be placed diagonally'
  for i in range(abs(distance)):
    if isBackwards:
      i = -i
    if isHorizontal:
      updateMatrix('1',(x1+i),y1, player)
    elif isVertical:
      updateMatrix('1',x1,(y1+i), player)

def playerName(player):
  if player == playerOne: 
    x = 'player One'
  elif player == playerTwo:
    x = 'player Two'
  player.name = raw_input('Who will be ' + x+'?')
  return player.name

def playerShip(player):
  print player.name + ' you are up'
  print 'place your ship by providing coordinates'
  for i  in range(3):
    if player == playerOne:
      printMatrix(playerOne)
    elif player == playerTwo:
      printMatrix(playerTwo)
    if i == 0:
      print 'Place ship #1 (length of 2)'
      while player.distance != 2:
        validate(player, 2)
    elif i == 1:
      print 'Place ship #2 (length of 3)'
      while player.distance != 3:
        validate(player, 3)
    elif i == 2:
      print 'Place ship #3 (length of 2)'
      while player.distance != 2:
        validate(player, 2)
    
def validate(player, value):
  x1 = raw_input('x1 ')
  while type(x1) == str:
    try:
      x1 = int(x1)
    except ValueError:
      print 'Use a valid coordinate'
      x1 = raw_input('x1 ')
  while int(x1)>5 or int(x1)<1:
    print 'not a valid spot'
    x1 = int(raw_input('x1 '))
  y1 = raw_input('y1 ')
  while type(y1) == str:
    try:
      y1 = int(y1)
    except ValueError:
      print 'Use a valid coordinate'
      y1 = raw_input('y1 ')
  while int(y1)> 11 or int(y1)<7:
    print 'not a valid spot'
    y1 = int(raw_input('y1 '))
  x2 = raw_input('x2 ')
  while type(x2) == str:
    try:
      x2 = int(x2)
    except ValueError:
      print 'Use a valid coordinate'
      x2 = raw_input('x2 ')
  while int(x2)> 5 or int(x2)<1:
    print 'not a valid spot'
    x2 = int(raw_input('x2 '))
  y2 = raw_input('y2 ')
  while type(y2) == str:
    try:
      y2 = int(y2)
    except ValueError:
      print 'Use a valid coordinate'
      y2 = raw_input('y2 ')
  while int(y2)> 11 or int(y2)<7:
    print 'not a valid spot'
    y2 = int(raw_input('y2 '))
  distance(player,x1,y1,x2,y2)
  if player.distance == value:
    placeShip(player, abs(x1), abs(y1), abs(x2), abs(y2))
  else:
    print 'Put in a distance of ', value

def won(player):
  print player.name, 'has won'
  main()

def shoot(player):
  print 'Where would', player.name  ,'like to shoot'
  x = raw_input('X ')
  while type(x) == str:
    try:
      x = int(x)
      while int(x)>5 or int(x)<1:
        print 'not valid spot'
        x = raw_input('X ')
    except ValueError:
      print 'not valid spot'
      x = raw_input('X ')
      
  y = raw_input('Y ')
  while type(y) == str:
    try:
      y = int(y)
      while int(y)>5 or int(y)<1:
        print 'not valid spot'
        y = raw_input('Y ')
    except ValueError:
      print 'not valid spot'
      y = raw_input('Y ')   
    
  while player.grid[lookUp(y,x)] != '0':
    print 'you have already shot there' 
    x = raw_input('X ')
    while type(x) == str:
      try:
        x = int(x)
        while int(x)>5 or int(x)<1:
          print 'not valid spot'
          x = raw_input('X ')
      except ValueError:
        print 'not valid spot'
        x = raw_input('X ')
    y = raw_input('Y ')
    while type(y) == str:
      try:
        y = int(y)
        while int(y)>5 or int(y)<1:
          print 'not valid spot'
          y = raw_input('Y ')
      except ValueError:
        print 'not valid spot'
        y = raw_input('Y ') 
    
  y = int(y)+6
  if player == playerOne:
    if checkMarix(x,y,playerTwo, '1'):
      print 'Hit'
      updateMatrix('H',x,(y - 6),playerOne)
      printMatrix(player)
      playerOne.score = playerOne.score + 1
      if playerOne.score < 7:
        shoot(playerOne)
      else:
        won(playerOne)
    else:
      print 'Miss'
      updateMatrix('X',x,(y - 6),playerOne)
      printMatrix(player)
      
  elif player == playerTwo:
    if checkMarix(x,y,playerOne, '1'):
      print 'Hit'
      updateMatrix('H',x, (y - 6),playerTwo)
      printMatrix(player)
      playerTwo.score = playerTwo.score + 1
      if playerTwo.score < 7:
        shoot(playerTwo)
      else:
        won(playerTwo)
    else:
      print 'Miss'
      updateMatrix('X',x,(y - 6),playerTwo)
      printMatrix(player)

def main():
  playerOne.distance = 0
  playerTwo.distance = 0
  print 'Welcome to battleship'
  print 'The aim of the game is to sink your opponent\'s ships.'
  print 'Each player gets 3 ships: 2 ships that are 3 units long and 1 ship that is 2 units long'
  playerName(playerOne)
  replit.clear()
  playerName(playerTwo)
  replit.clear()
  print 'The players are', playerOne.name, 'and' ,playerTwo.name
  playerShip(playerOne)
  replit.clear()
  playerShip(playerTwo)
  replit.clear()
  while True:
    shoot(playerOne)
    replit.clear()
    shoot(playerTwo)
    replit.clear()
    
main()
