from PIL import Image

cubeText = ""
with open('digitalcube.txt','r') as f :
    cubeText = f.read()

width = 50
height = 50
image = Image.new("RGB",(width,height))
putPixel = image.putpixel
imgx , imgy = image.size
p = 0
for i in range(50):
    for j in range(50):
        if cubeText[p] == "1" :
            putPixel((i,j),(0,0,0))
        else:
            putPixel((i,j),(255,255,255))
        p += 1
image.save("t.png")
image.show()
