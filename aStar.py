import math

class Point:
    xX = 0
    yY = 0
    valueXY = 0
    costValue = 0.0
    fatherX = None
    motherY = None

    def __init__(self, x, y):
        self.xX = x
        self.yY = y

    def __str__(self):
        return (' (' + str(self.xX) + ' | ' + str(self.yY) + ' )'+'\n')



beginXY = Point(0, 0)
endXY = Point(3, 18)
opened = []
closed = []
mapXY = []
pointMAP = [[Point(x, y) for y in range(20)] for x in range(20)]



def loadMap(fileName):
    try:
        plik = open(fileName, 'r')
        for line in plik:
            mapXY.append(line.split())
        plik.close()
    except FileNotFoundError as e:
        print(" There's no existance of such file ")
        print(e)



def loadPointMap():
    for i in range(20):
        for j in range(20):
            pointMAP[i][j].valueXY = mapXY[i][j]


# Algorithm that counts exact cost value from parents position to their descendants
# It chooses the shortest path based on value.
def heuristic(x, y):
    return math.sqrt(pow(x - endXY.xX, 2) + pow(y - endXY.yY, 2))



# Here's the opened list with sections about moving in each direction, we can switch the directions so
# if there are basically 2 paths leading to the destination both of the same cost, the chosen one
# may be selected differently if we switch "if's" between each other, but it'd require very specific
# situation to appear, the chances for our grid generated in exe are nearly impossible.
def addOpened(point):
    descendant = Point
    print("\n Beginning of the function AddOpened, number of elements in opened:" + str(len(opened)))

    # Move to the bottom
    if point.xX + 1 < 20 and pointMAP[point.xX + 1][point.yY].valueXY != '5' and ifExist(
            pointMAP[point.xX + 1][point.yY]) is False and pointMAP[point.xX + 1][point.yY].fatherX is None:
        descendant = pointMAP[point.xX + 1][point.yY]

        descendant.fatherX = point.xX
        descendant.motherY = point.yY
        pointMAP[point.xX + 1][point.yY] = descendant
        costCounter(descendant)
        opened.append(descendant)
        print(" both X and Y parents " + str(point.xX) + "," + str(point.yY) + "\t bottom descendant " + str(
            descendant.xX) + "," + str(descendant.yY) + "\t cost value : " + str(descendant.costValue))
        descendant = Point

    # Move up
    if point.xX - 1 >= 0 and pointMAP[point.xX - 1][point.yY].valueXY != '5' and ifExist(
            pointMAP[point.xX - 1][point.yY]) is False and pointMAP[point.xX - 1][point.yY].fatherX is None:
        descendant = pointMAP[point.xX - 1][point.yY]
        descendant.fatherX = point.xX
        descendant.motherY = point.yY
        pointMAP[point.xX - 1][point.yY] = descendant
        costCounter(descendant)
        opened.append(descendant)
        print(" both X and Y parents " + str(point.xX) + "," + str(point.yY) + "\t up descendant " + str(
            descendant.xX) + "," + str(descendant.yY) + "\t cost value : " + str(descendant.costValue))
        descendant = Point

    # Move to the left
    if point.yY - 1 >= 0 and pointMAP[point.xX][point.yY - 1].valueXY != '5' and ifExist(
            pointMAP[point.xX][point.yY - 1]) is False and pointMAP[point.xX][point.yY - 1].fatherX is None:
        descendant = pointMAP[point.xX][point.yY - 1]
        descendant.fatherX = point.xX
        descendant.motherY = point.yY
        pointMAP[point.xX][point.yY - 1] = descendant
        costCounter(descendant)
        opened.append(descendant)
        print(" both X and Y parents " + str(point.xX) + "," + str(point.yY) + "\t left descendant " + str(
            descendant.xX) + "," + str(descendant.yY) + "\t cost value: " + str(descendant.costValue))
        descendant = Point

    # Move to the right
    if point.yY + 1 < 20 and pointMAP[point.xX][point.yY + 1].valueXY != '5' and ifExist(
            pointMAP[point.xX][point.yY + 1]) is False and pointMAP[point.xX][point.yY + 1].fatherX is None:
        descendant = pointMAP[point.xX][point.yY + 1]
        descendant.fatherX = point.xX
        descendant.motherY = point.yY
        pointMAP[point.xX][point.yY + 1] = descendant
        costCounter(descendant)
        opened.append(descendant)
        print(" both X and Y parents " + str(point.xX) + "," + str(point.yY) + "\t right descendant " + str(
            descendant.xX) + "," + str(descendant.yY) + "\t cost value: " + str(descendant.costValue))
        descendant = Point


    for i in opened:
        print(" Points of X and Y in opened " + str(i.xX) + " " + str(i.yY))
    print("\n The end of the function addOpened \n")



def costCounter(point):
    heur = heuristic(point.xX, point.yY)
    print("Heuristic: " + str(heur))
    costValue = 0
    temp = point
    valueXY = True
    while valueXY:
        temp = pointMAP[temp.fatherX][temp.motherY]
        costValue += 1
        if beginXY.xX == temp.xX and beginXY.yY == temp.yY:
            valueXY = False

    point.costValue = costValue + heur



def ifExist(point):
    for i in closed:
        if i.xX == point.xX and i.yY == point.yY:
            return True
    return False



def costLOW():
    try:
        max = opened[len(opened) - 1]
        for i in opened:
            if max.costValue > i.costValue:
                max = i
        return max
    except IndexError as e:
        print(" It's out of the range, error ")



def closedAdd():
    optimalP = costLOW()
    print("\n Return of the closedAdd ")
    for i in range(opened.__len__() - 1, -1, -1):
        if opened[i].xX == optimalP.xX and opened[i].yY == optimalP.yY:
            del opened[i]
    # show the closed list(opened)
    closed.append(optimalP)
    for i in closed:
        print(" Points in the closedAdd " + str(i.xX) + " " + str(i.yY))
    print(" The end of the function closedAdd ")



def endMap():
    point = pointMAP[endXY.xX][endXY.yY]
    print("Pure map with the final score")
    valueXY = True
    while valueXY:
        mapXY[point.xX][point.yY] = '3'
        point = pointMAP[point.fatherX][point.motherY]
        if beginXY.xX == point.xX and beginXY.yY == point.yY:
            valueXY = False



def mapSHOW():
    for i in mapXY:
        print(i)



def showXY():
    for i in closed:
        print(" Element of the closed list " + str(i.xX) + " | " + str(i.yY))



def aSTAR():
    loadMap('grid.txt')
    loadPointMap()
    # loadMap()
    closed.append(beginXY)
    addOpened(closed[0])
    print(" First element")
    for i in opened:
        print(" Element of the opened list " + str(i.xX) + " | " + str(i.yY))
    showXY()
    mapXY[beginXY.xX][beginXY.yY] = '3'
    mapXY[endXY.xX][endXY.yY] = '3'
    # Iteration's indexes in the closed list
    temp = 1

    while True:
        if opened.__len__() == 0:
            print(" There's no path leading to destination ")
        print("\n\n Iteration : " + str(temp))

        closedAdd()

        addOpened(closed[temp])

        for i in opened:
            print(" Element of the opened list " + str(i.xX) + " | " + str(i.yY))

        temp += 1
        if ifExist(endXY):
            break
    endMap()
    mapSHOW()


aSTAR()
