from PIL import Image
import os
import math
from enum import Enum

#global constants
userInput = {"rows":0,"columns":0,"paperSize":'',"imgPath":''}
paperDimenDict = {"a0":(841,1189),"a1":(594,841),"a2":(420,594),"a3":(297,420),"a4":(210,297)}

class paperSizeEnum(Enum):
    # a0 = 0
    # a1 = 1
    # a2 = 2
    # a3 = 3
    a4 = 4


def driver():
    getInputFromUser(userInput)
    print(userInput)
    nRows = userInput['rows']
    nColumns = userInput['columns']
    paperDimen = paperDimenDict[userInput['paperSize']]

    # calculate the image resize dimensions in MilliMeters
    lengthResizeDimenInMM = getLengthResizeDimen(nColumns, paperDimen)
    breadthResizeDimenInMM = getBreadthResizeDimen(nRows,paperDimen)

    lengthInPixels = math.floor(getMMtoPixels(lengthResizeDimenInMM)) - 10
    breadthInPixels = math.floor(getMMtoPixels(breadthResizeDimenInMM)) -10
    imageHandler = loadImage()
    resizeImage(imageHandler,(int(lengthInPixels),int(breadthInPixels)))


    print(lengthInPixels,breadthInPixels)

def getInputFromUser(userInput):
    userInput["rows"] = input("Enter rows : ")
    userInput["columns"] = input("Enter columns : ")
    userInput["paperSize"] = input("Enter paper size Eg: a4,a3 etc: ").lower()
    userInput["imgPath"] = './sampleImages/sample_image2.png'
    validateUserInput(userInput)
    return (userInput)

def validateUserInput(userInput):
    if not hasattr(paperSizeEnum,userInput["paperSize"]):
        print("User input invalid .Please re-enter")
        getInputFromUser(userInput)

def printData(dataToPrint):
    print(dataToPrint)

def getLengthResizeDimen(nCol,paperDimensionTuple):
# calculate the length resize of the image
# obtained by dividing the length of paper by number of columns required
    print('length resize -')
    print(nCol,paperDimensionTuple[0])
    lengthResize = int(paperDimensionTuple[0]) / int(nCol)
    return lengthResize


def getBreadthResizeDimen(nRow,paperDimensionTuple):
# calculate the breadth resize of the image
# obtained by dividing the breadth of paper by number of rows required
    print('breadth resize -')
    print(nRow,paperDimensionTuple[1])
    breadthResize = int(paperDimensionTuple[1]) / int(nRow)
    return breadthResize

def getMMtoPixels(inputInMM):
    return inputInMM * 3.7795275591;

def loadImage():
   imgHandler = Image.open(userInput['imgPath'])
   return imgHandler


def resizeImage(imgHandler,resizeDimensions):
    imgHandler.thumbnail(resizeDimensions)
    imgHandler.save('./sampleImages/sampleImage_resized_{}_{}.png'.format(resizeDimensions[0],resizeDimensions[1]))

# input from user -> nXm and size of paper to be printed

# take the (n,m ) dimensions of the image impressions on paper to be printed on (l,b) mm paper
# n = number of rows m = number of columns
# l = length of the sheet
# b = breadth of sheet

if __name__=='__main__':
    driver()