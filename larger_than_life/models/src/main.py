#TEST ONLY PYTHON SCRIPT
import board
import pygame
import time
import json

constMul = 2
constSize = 400
sleepTime = 0.02
random1constant0 = 1
percentOfAlive = 300

Moore = 0
Neumann = 1
Circular = 2

game = board.Board(constSize, constSize)

game.SetConstBoard()
if random1constant0 == 1:
    game.SetRandomBoard(percentOfAlive)

nameOfFile = input("Enter name of file:")

try:
    with open("./rules/{}.json".format(nameOfFile), "r") as jsonFileRules:
        data = json.load(jsonFileRules)
        game.SetRules(data["range"], data["numberOfStates"], data["middleCell"], data["survivalMin"], data["survivalMax"], data["birthMin"], data["birthMax"], data["neighbourhoodType"])
except:
    print("Cannot open file, setting default rules\n")
    game.SetRules(1,0,0,2,3,3,3,0)


game.SetRules(1,48,0,1,4,3,4,0)

pygame.init()
gameDisplay = pygame.display.set_mode((constMul*constSize,constMul*constSize))

white = (255,255,255)
black  = (0,0,0)

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    
    gameDisplay.fill(black)


    for heightArg in range(0,game.Height()):
        for widthArg in range(0,game.Width()):

            if game.GetPixelState(heightArg,widthArg) >0:
                pygame.draw.rect(gameDisplay, (255, game.GEtPixelState(heightArg, widthArg), 0)) , [heightArg * constMul ,widthArg * constMul,constMul,constMul])
    
    pygame.display.update()
    game.Update()
    time.sleep(sleepTime) #delays the loop

