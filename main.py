"""run the program then enter cube and enter the information recommended: 
5
5
5
2,2,2"""

height = 30
base = 50
import pong
import cube
import math
import time
import setup
import matricies


class Command:
    def __init__(command, name, help):
        command.name = name
        command.help = help


Exit = Command("exit", "This closes the window")
Pong = Command(
    "pong",
    "This starts a game of pong. Use W and S for left and I and K for right")
CUBE = Command("cube", "This does the cube animation")
Help = Command("help", "This prints this message")
commands = [Exit, Pong, CUBE, Help]

flag = True
while flag:
    userinput = input(
        "What would you like to do(Type 'help' for help)?:").lower()
    if userinput == "pong":
        pong.Pong(base, height)
    if userinput == "cube":
        cube_base = int(input("Base: "))
        cube_height = int(input("Height: "))
        cube_thickness = int(input("Thickness: "))
        cube_origin_list = input("Origin<x,y,z>:").split(",")
        cube_origin = (int(cube_origin_list[0]), int(cube_origin_list[1]),
                       int(cube_origin_list[2]))
        print("creating cube")
        CubeObject = cube.Cube(cube_origin, cube_base, cube_height,
                               cube_thickness)
        print("cube created")
        Zeye = 0
        Zdisplay = Zeye + 1
        H = 0
        phi = 0
        theta = 0
        yaw = 0

        frame = setup.CreateFrame(base, height)
        edge = setup.CreateEdge(base, height)

        theta = math.pi / 6

        print("starting rotation")
        for i in range(0, 40):
            THdmatricies = matricies.ThreeDPointsToMatrices(CubeObject.points)
            CubeObject.TWdpoints = matricies.Turn3dMatriciesTo2DPoints(
                THdmatricies, Zdisplay, Zeye, H)
            CubeObject.CreateLines()

            for line in CubeObject.lines:
                CubeObject.AddCubeValues(frame, line.points)
            setup.PrintFrame(frame)
            for line in CubeObject.lines:
                CubeObject.RemoveCubeValues(frame, line.points)
            center = CubeObject.FindCenter()
            CubeObject.rotateZ(center, theta)
            time.sleep(0.5)

    if userinput == "exit":
        flag = False
    if userinput == "help":
        for command in commands:
            print(command.name + ":\n" + command.help + "\n")
    time.sleep(0.5)
