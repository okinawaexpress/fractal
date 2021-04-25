import math
import numpy
import PIL
from PIL import Image

im = Image.new('RGB', (500, 500), (255, 255, 255))
grid = numpy.linspace(-2.0, 2.0, 500)

def juliabrot(z, c):
    ic = 0
    for i in range(999):
        if abs (math.sqrt (z[0]**2 + z[1]**2)) > 2 or abs (math.sqrt (z[0]**2 + z[1]**2)) < -2: #check if above/lower than 2/-2
            return ic #unbounded
        else:   
            z = [(z[1]**2*-1 + z[0]**2) + c[0], (z[0]*z[1] + z[0]*z[1]) + c[1]] #update z
            ic = ic + 1 #update iteration count
    return 0 #part of set

def colorpixel(ic):
    #cleaner, succinct way of check ic, plus user given colors
    if ic == 0:
        im.putpixel((xline, yline), (0, 0, 0))
    elif ic == 1:
        im.putpixel((xline, yline), (255, 200, 200))
    elif ic == 2:
        im.putpixel((xline, yline), (255, 180, 180))
    elif ic == 3:
        im.putpixel((xline, yline), (255, 160, 160))
    elif ic == 4:
        im.putpixel((xline, yline), (255, 140, 140))
    elif ic == 5: 
        im.putpixel((xline, yline), (255, 120, 120))
    elif ic == 6:
        im.putpixel((xline, yline), (255, 100, 100))
    else:
        im.putpixel((xline, yline), (255, 80, 80))

def generatefractal():
    #take z/c constant (mandelbrot/julia), name of file, colors, iterations, grid size,
    pass
        
yline = 0
for y in grid:
    xline = 0
    for x in grid:
        c = [round(x, 2), round(y, 2)]
        z = [0, 0]
        colorpixel(juliabrot(z, c))
        xline+=1
    yline+=1
        
im.save("mandelbrot.png")
