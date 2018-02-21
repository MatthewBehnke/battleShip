class Matrix():
  def __init__(self):
    self.grid =   ['00','1','2','3','4','5',
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

def placeShip(player, x1, y1, x2, y2):
  isHorizontal = False
  isVertical = False
  if x1 == x2 and y1 == y2:
    print 'Ship can not be placed on it self'
  elif x1 == x2:
    isHorizontal = False
    isVertical = True
    distance = y2 - y1 +1
  elif y1 == y2:
    isVertical = False
    isHorizontal = True
    distance = x2 - x1 + 1
  else:
    print 'Ship cannot be placed diagonally'
  for i in range(abs(distance)):
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
    if i == 0:
      print 'Place ship #1 (length of 3)'
    elif i == 1:
      print 'Place ship #2 (length of 2)'
    elif i == 2:
      print 'Place ship #3 (length of 2)'
    x1 = int(raw_input('x1 '))
    y1 = int(raw_input('y1 '))
    x2 = int(raw_input('x2 '))
    y2 = int(raw_input('y2 '))
    placeShip(player, abs(x1), abs(y1), abs(x2), abs(y2)) 
    if player == playerOne:
      printMatrix(playerOne)
    elif player == playerTwo:
      printMatrix(playerTwo)

def main():
  print 'Welcome to battleship'
  print 'The aim of the game is to sink your opponent\'s ships.'
  print 'Each player gets 3 ships: 2 ships that are 3 units long and 1 ship that is 2 units long'
  playerName(playerOne)
  playerName(playerTwo)
  print 'The players are', playerOne.name, 'and' ,playerTwo.name
  playerShip(playerOne)
  playerShip(playerTwo)
  
main()
