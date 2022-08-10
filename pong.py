import random
import time
import keyboard
import setup
import box
def UpdateSprite(player):
    for i in range(0, len(player.points)):
        player.points[i] = (player.points[i][0]+player.xvelocity, player.points[i][1]+player.yvelocity)

def BallCollision(sprites):
    ball = sprites[2]
    player1 = sprites[0]
    player2 = sprites[1]

    lefttopx = ball.points[0][0]
    lefttopy = ball.points[0][1]

    righttopx = ball.points[0][0]+ball.base
    #chekcs if it hits the player1 on left
    if lefttopx == player1.points[0][0]+player1.base:
        if lefttopy+ball.height >= player1.points[0][1] and lefttopy <= player1.points[0][1]+player1.height:
            ball.xvelocity = 1
            ball.yvelocity = random.randint(-1, 1)
        return 0
    if lefttopx+ball.base < player1.points[0][0]-2:
        sprites[2] = box.Box(2, 2, 50, 14)
        return -1

    #checks if hits player2 on right
    if righttopx == player2.points[0][0]+player2.base:
        if lefttopy+ball.height >= player2.points[0][1] and lefttopy <= player2.points[0][1]+player1.height:
            ball.xvelocity = -1
            ball.yvelocity = random.randint(-1, 1)
        return 0
    if righttopx-ball.base > player2.points[0][0]+2:
        sprites[2] = box.Box(2, 2, 50, 14)
        return 1
    return 0

def CheckBallBounds(sprites, frameheight):
    ball = sprites[2]
    if ball.points[0][1] <= 1:
        sprites[2].yvelocity = ball.yvelocity*-1
    if ball.points[0][1]+ball.height >= frameheight-1:
        sprites[2].yvelocity = ball.yvelocity*-1

def Game(base, height):
    frame = setup.CreateFrame(base, height)
    draw_lines = setup.CreateEdge(base, height)

    score = 0
    flag = True
    player1 = box.Box(3, 5, 10, 14)
    player2 = box.Box(3, 5, 80, 14)
    ball = box.Box(2, 2, 50, 14)
    gamestart = False
    sprites = [player1, player2, ball]
    while flag:

        if keyboard.is_pressed("space"):
            flag = False
            return 0

        if score != 0:
            flag = False
            return score
            break

        if keyboard.is_pressed("a") and gamestart != True:
            ball.xvelocity = -1
            gamestart = True

        player1.yvelocity = 0
        #player1.xvelocity = 0
        player2.yvelocity = 0
        #player2.xvelocity = 0

        if keyboard.is_pressed("w") and player1.points[0][1] > 1:
            player1.yvelocity = -1
        elif keyboard.is_pressed("s") and player1.points[0][1]+player1.height < height:
            player1.yvelocity = 1

        if keyboard.is_pressed("i") and player2.points[0][1] > 1:
            player2.yvelocity = -1
        elif keyboard.is_pressed("k") and player2.points[0][1]+player2.height < height:
            player2.yvelocity = 1



        UpdateSprite(player1)
        UpdateSprite(player2)
        UpdateSprite(ball)
        for sprite in sprites:
            sprite.AddBoxValues(frame)
        setup.Straight(frame, draw_lines)
        setup.PrintFrame(frame)
        for sprite in sprites:
            sprite.RemoveBoxValues(frame)
        score += BallCollision(sprites)
        CheckBallBounds(sprites, height)
        time.sleep(0.03)

def Pong(base, height):
    bigflag = True
    score = 0
    while bigflag:
        score += Game(base, height)
        if keyboard.is_pressed("space"):
            print(str(score) + ":  neg means left player won and pos means left player won" "\n" +"type again to play again and enter to go back to menu" )
            if input().split(" ")[1] == "again":
                bigflag = True
            else:
                bigflag = False
