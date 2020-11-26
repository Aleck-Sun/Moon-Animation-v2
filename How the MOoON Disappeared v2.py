from tkinter import *
from random import *
from time import *
from math import *

width = 800
height = 500

myInterface = Tk()
s = Canvas(myInterface, width = width, height = height, background = "black")
s.pack()
#Images
frame1 = PhotoImage(file = "frame1.gif")
frame2 = PhotoImage(file = "frame2.gif")
frame3 = PhotoImage(file = "frame3.gif")
frame4 = PhotoImage(file = "frame4.gif")
frame5 = PhotoImage(file = "frame5.gif")
frame6 = PhotoImage(file = "frame6.gif")
fight1 = PhotoImage(file = "fight1.gif")
fight2 = PhotoImage(file = "fight2.gif")
frameslist = [frame3, frame4, frame5, frame6]

#Functions
#Fade in function(black to white)
def fade():
    s.delete("all")
    i = 1
    for f in range (100):
        fade = s.create_rectangle(0, 0, width, height, fill = "grey" + str(i))
        s.update()
        sleep(0.01)
        s.delete(fade)
        i+=1

#Fade out function(white to black)
def fadeOut():
    s.delete("all")
    i = 100
    for f in range (100):
        fade = s.create_rectangle(0, 0, width, height, fill = "grey" + str(i))
        s.update()
        sleep(0.01)
        s.delete(fade)
        i-=1

#Clouds
def cloud(x2, x3, y2, y3):
    for clouds in range(50):
        x = randint(x2, x3)
        y = randint(y2, y3)
        s.create_oval(x, y, x + 50, y + 50, fill = "grey84", outline = '')

#Stars
def createStars():
    for stars in range (1, 20):
        starX = randint(10, 790)
        starY = randint(10, 490)
        starX2 = starX - 5
        starX3 = starX + 5
        starY2 = starY + 7.5
        starDownY = starY + 10
        starDownY2 = starDownY - 7.5
        s.create_polygon(starX, starY, starX2, starY2, starX3, starY2, fill = "white")
        s.create_polygon(starX, starDownY, starX2, starDownY2, starX3, starDownY2, fill = "white")

    #Little Stars
    for Litstrs in range (1, 200):
        sizeIncrease = randint(1, 3)
        LitStarX = randint(0, 800)
        LitStarY = randint(0, 500)
        s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white")

#Fireworks
def firework(ExCx, ExCy):
    #Variables
    x = []
    y = []
    numExplosion = 1000
    particles = []
    r = []
    rSpeed = []
    angle = []
    sizes= []
    exColours = ["cyan2", "white", "red", "yellow"]
    fadeColours = ["black", "white", "black", "black"]

    #Creating arrays
    for i in range(numExplosion):                                       
        sizes.append(randint(1, 3))

        x.append(ExCx)
        y.append(ExCy)
        
        r.append(0)
        angle.append(uniform(0,2*pi))
        rSpeed.append(uniform(0, 10))
        particles.append(0)
        
    #Animation
    for f in range(20):                                                        
        for i in range(numExplosion):
            if f < 10:
                colour = choice(exColours)
            else:
                colour = choice(fadeColours)
            particles[i] = s.create_rectangle( x[i], y[i], x[i] + sizes[i], y[i] + sizes[i], fill = colour)

            x[i] = ExCx + r[i] * cos( angle[i] )
            y[i] = ExCy - r[i] * sin( angle[i] )
            r[i] += rSpeed[i]

        s.update()
        sleep(0.03)
        for i in range(numExplosion):
            s.delete(particles[i])    
    

#Scene 1: Intro
#Stars
createStars()

#Text array intro
textY = 100
text = ["Around 1 year ago", "The legendary coder Bowen", "Uncovered the secrets of the", "Dissappearance of the moon..."]
for f in range (len(text)):
    text[f] = s.create_text(width/2, textY, text = text[f], font = "Arial 20", fill = "white")
    textY += 100
    s.update()
    sleep(2)


for delete in range (len(text)):
    s.delete(text[delete])

#Scene 2: Recall
#Stars
createStars()

#Earth
s.create_oval(-300, 200, 300, 800, fill = "#2b2b2b")
s.create_polygon(42, 253, 16, 273, 15, 305, 23, 334, 30, 351, 46, 358, 89, 367, 114, 365, 128, 349, 127, 324, 112, 311, 102, 277, 77, 256, fill = "gray", smooth = True)
s.create_polygon(44, 495, 57, 466, 86, 444, 119, 425, 155, 420, 184, 420, 207, 410, 225, 403, 243, 413, 267, 447, 284, 481, 285, 500, 200, 550, 100, 550, fill = "gray", smooth = True) 

#Meteor
meteor = 0
meteorX = 800
meteorY = -100
flameColors = ["#3a3a3a", "#939393", "#d8d8d8"]
for meteorfly in range (25):
    s.delete(meteor)
    ranFlame = randint(0,2)
    flameX = meteorX + 50
    flameY = meteorY
    flame = s.create_polygon(flameX, flameY, flameX + 13.3, flameY + 26.6, flameX + 50, flameY - 15, fill = flameColors[ranFlame])
    flame2 = s.create_polygon(flameX + 13.3, flameY + 26.6, flameX + 13.3*2, flameY + 26.6*2, flameX + 50*1.5, (flameY + 26.6) -15, fill = flameColors[ranFlame])
    flame3 = s.create_polygon(flameX + 13.3*2, flameY + 26.6*2, flameX + 13.3*3, flameY + 26.6*3, flameX + 50*2, (flameY + 26.6*2) - 15, fill = flameColors[ranFlame])
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)
    s.delete(flame, flame2, flame3)

    meteorX -= 12
    meteorY += 8

s.delete(meteor)

#Meteor veers away from Earth
#Cordinates change at different speed, causing parabola motion
ySpeed = 3
xSpeed = -7
for meteorfly in range (40):
    #draw meteor
    s.delete(meteor)
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)

    #update postition
    meteorX += xSpeed
    meteorY += ySpeed

    #change ySpeed
    ySpeed += -1

s.delete("all")

#Stars
createStars()

#Moon
cY = 250
cX = 400
moon = s.create_oval(cX + 100, cY + 100, cX - 100, cY - 100, fill = "#2b2b2b")
meteorX = cX
meteorY = 550
while meteorY > 400:
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    if meteorY > 450:
        meteorY -= 5
    else:
        meteorY -= 1
    s.update()
    sleep(0.03)
    s.delete(meteor)
s.delete(moon)
s.update()

#Scene 3: The Truth
s.create_text(width/2, height/3, text = "But little did people know...", font = "Arial 20", fill = "white")
s.update()
sleep(3)
s.create_text(width/2, height/1.5, text = "How the MOoON Really DISAPPEARED", font = "Arial 20", fill = "white")
s.update()
sleep(3)

#Scene 4: My perspective
#Stars
s.create_rectangle(0, 0, width, height, fill = "black")
createStars()

#Earth
s.create_oval(-300, 200, 300, 800, fill = "blue")
s.create_polygon(42, 253, 16, 273, 15, 305, 23, 334, 30, 351, 46, 358, 89, 367, 114, 365, 128, 349, 127, 324, 112, 311, 102, 277, 77, 256, fill = "green", smooth = True)
s.create_polygon(44, 495, 57, 466, 86, 444, 119, 425, 155, 420, 184, 420, 207, 410, 225, 403, 243, 413, 267, 447, 284, 481, 285, 500, 200, 550, 100, 550, fill = "green", smooth = True)

#Meteor
meteor = 0
meteorX = 800
meteorY = -100
flameColors = ["red", "orange", "yellow"]
for meteorfly in range (200):
    ranFlame = randint(0,2)
    flameX = meteorX + 50
    flameY = meteorY
    flame = s.create_polygon(flameX, flameY, flameX + 13.3, flameY + 26.6, flameX + 50, flameY - 15, fill = flameColors[ranFlame])
    flame2 = s.create_polygon(flameX + 13.3, flameY + 26.6, flameX + 13.3*2, flameY + 26.6*2, flameX + 50*1.5, (flameY + 26.6) -15, fill = flameColors[ranFlame])
    flame3 = s.create_polygon(flameX + 13.3*2, flameY + 26.6*2, flameX + 13.3*3, flameY + 26.6*3, flameX + 50*2, (flameY + 26.6*2) - 15, fill = flameColors[ranFlame])
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)
    s.delete(flame, flame2, flame3, meteor)

    meteorX -= 3
    meteorY += 2

#Variables
meteorX = width - 150
meteorY = height - (height+1000)
armDirection = 100
meteor = 0

#Background
sky = s.create_rectangle(0, 0, width, height - 150, fill = "steel blue", outline = "steel blue")
land = s.create_rectangle(0, height - 150, width, height, fill = "dark green", outline = "dark green")
human = s.create_image(200, 325, image = frame1)
cloud(100, 300, 100, 175)
cloud(500, 700, 150, 250)


#Meteor coming in
for i in range (50):
    s.delete(meteor)
    meteor = s.create_oval(meteorX, meteorY, meteorX + 1000, meteorY + 1000, fill = "gray") 
    meteorX -= 6
    meteorY += 5
    s.update()
    sleep(0.03)

#Fighter getting ready
s.delete(human)
human = s.create_image(200, 325,image = frame2)
text = s.create_text(width/2, height/2-100, text = "YAAAAAAAAAAAA!", font = "impact 60")
s.update()
sleep(1)

#Powering up
for i in range (20):
    s.delete(human)
    human = s.create_image(200, 325, image = frameslist[i%4])
    s.update()
    sleep(0.1)

#Scene 5: Battle
#VS           
fadeOut()
vs = s.create_text(width/2, height/2, text = "V.S.", font = "impact 100", fill = "red")
s.update()
sleep(2)
s.delete(vs)

#Background
#Variables
x = []
y = []
line = []
color = []
humanX = -50
humanY = height+50
size = 0
increase = 0
x2 = 305
y2 = 340
clash = 0
col = ["black", "white"]

#Creating arrays
for random in range (500):
    x.append(randint(-150, width))
    y.append(randint(0, height+150))
    color.append(choice(["gold", "white", "yellow"]))
    line.append(0)
    
for times in range (100):
    #Battle line streaks
    for i in range (500):
        line[i] = s.create_line(x[i], y[i], x[i] + 600, y[i] - 600, fill = color[i], width = 60)
        x[i] += 10
        y[i] -= 10
        if x[i] > width or y[i] < 0:
            x[i] = randint(-400, width)
            y[i] = randint(0, height+400)

    #Human and meteor colliding
    if meteorX <= humanX-100:
        meteor = s.create_oval(meteorX, meteorY, meteorX + 1000, meteorY + 1000, fill = "gray") 
        human = s.create_image(humanX, humanY, image = fight1)

        #Clash
        clash = s.create_oval(x2+size, y2+size, x2-size, y2-size, fill = col[times%2], outline = col[times%2])
        increase +=0.1
        size+=(1 + increase**2)

    #Human and meteor charging at each other    
    else:
        meteor = s.create_oval(meteorX, meteorY, meteorX + 1000, meteorY + 1000, fill = "gray") 
        meteorX -= 6
        meteorY += 5
        
        human = s.create_image(humanX, humanY, image = fight2)
        humanY -= 5
        humanX += 7

    s.update()
    sleep(0.03)
    s.delete(human, meteor, clash)
    for i in range(500):
        s.delete(line[i])

#Scene 6: Moon explosion
#Stars
createStars()

#Earth
s.create_oval(-300, 200, 300, 800, fill = "#007ef4")
s.create_polygon(42, 253, 16, 273, 15, 305, 23, 334, 30, 351, 46, 358, 89, 367, 114, 365, 128, 349, 127, 324, 112, 311, 102, 277, 77, 256, fill = "green", smooth = True)
s.create_polygon(44, 495, 57, 466, 86, 444, 119, 425, 155, 420, 184, 420, 207, 410, 225, 403, 243, 413, 267, 447, 284, 481, 285, 500, 200, 550, 100, 550, fill = "green", smooth = True)

#Meteor knocked away from Earth
ySpeed = 10
xSpeed = -3
meteorX = 200
meteorY = 200
for meteorfly in range (60):
    #draw meteor
    s.delete(meteor)
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)

    #update postition
    meteorX -= xSpeed
    meteorY -= ySpeed

    #change ySpeed
    ySpeed += -0.1

s.delete("all")

#Stars
createStars()

#Moon
cY = 250
cX = 400
moon = s.create_oval(cX + 100, cY + 100, cX - 100, cY - 100, fill = "yellow")
meteorX = cX
meteorY = 550
while meteorY > 325:
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    meteorY -= 10
    s.update()
    sleep(0.03)
    s.delete(meteor)
s.delete(moon)

#Explosion
#Variables
ExCx = width/2
ExCy = height/2
x = []
y = []
numExplosion = 1000
particles = []
r = []
rSpeed = []
angle = []
sizes= []
exColours = ["white", "yellow", "yellow", "gray"]

#Creating arrays
for i in range(numExplosion):                                       
    sizes.append(randint(1, 5))

    x.append(ExCx)
    y.append(ExCy)
    
    r.append(0)
    angle.append(uniform(0,2*pi))
    rSpeed.append(uniform(0, 50))
    particles.append(0)
    
#Animation
for f in range(75):                                                        
    for i in range(numExplosion):
        particles[i] = s.create_rectangle( x[i], y[i], x[i] + sizes[i], y[i] + sizes[i], fill = choice(exColours))

        x[i] = ExCx + r[i] * cos( angle[i] )
        y[i] = ExCy - r[i] * sin( angle[i] )
        r[i] += rSpeed[i]*5

    s.update()
    sleep(0.03)
    for i in range(numExplosion):
        s.delete(particles[i])
        
fadeOut()

#Scene 7: "Dad the moon exploded"
#Speech(Ignore the fact that this could've been done a much easier way (slicing), my brain is too dead to think at the moment)
son1 = ["D", "a", "d", " ", "I", " ", "t", "h", "i", "n", "k", " ", "I", " ",
        "j", "u", "s", "t", " ", "s", "a", "w", " ", "t", "h", "e", " ",
        "m", "o", "o", "n", " ", "e", "x", "p", "l", "o", "d", "e", "!"]

dad1 = ["D", "o", "n", "'", "t", " ", "b", "e", " ", "s", "i", "l", "l",
        "y", "!", " ", "I", "t", "'", "s", " ", "j" "u", "s", "t", " ",
        "f", "i", "r", "e", "w", "o", "r", "k", "s", "!" ]

#Typing speech
x = 50
x2 = x
for i in range (len(son1)):
    text = s.create_text(x, 100, text = son1[i], font = "Arial 15", fill = "white")
    x+=15
    s.update()
    sleep(0.06)
    
sleep(0.5)
for i in range (len(dad1)):
    text = s.create_text(x2, 200, text = dad1[i], font = "Arial 15", fill = "white")
    x2+=10
    s.update()
    sleep(0.06)

sleep(2)
s.delete("all")

#Scene 8: The Big REVEAL
#Sky
skyShade = ["#f2f9ff", "#deedf9", "#c8e1f4", "#afd1ea", "#9ecbed", "#8cbde2",
            "#85b7dd", "#7aaed6", "#6fa5ce", "#659cc6", "#5993bf", "#4d89b7",
            "#417ead", "#35709e", "#2b6796", "#215d8c", "#164e7a", "#11456d",
            "#0c3e66", "#073459", "#032b4c", "#001d35"]
y = height-10
size = 10

for sky in range (len(skyShade)):
    s.create_rectangle(0, y, width, y+size, fill = skyShade[sky], outline = '')
    if sky < 10:
        y-=10
    elif sky < 15:
        y-=20
        size = 20
    else:
        y-=35
        size = 35

#Stars
for Litstrs in range (1, 100):
    sizeIncrease = uniform(0, 3)
    LitStarX = randint(0, 800)
    LitStarY = randint(0, 500)
    s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white", outline = '')
s.create_polygon(0, height, 0, 380, 150, 260, 230, 400, 300, 350, 400, 440, 650, 220, width, 350, width, height, fill = "#001b33")
s.update()
sleep(1)

#Mountain + stars
s.delete("all")
i = 100
fade = 0
for f in range (101):
    s.delete(fade)
    fade = s.create_rectangle(0, 0, width, height, fill = "grey" + str(i))
    for Litstrs in range (50):
        sizeIncrease = uniform(0, 3)
        LitStarX = randint(0, 800)
        LitStarY = randint(0, 500)
        s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white", outline = '')
    s.create_polygon(0, height, 0, 380, 150, 260, 230, 400, 300, 350, 400, 440, 650, 220, width, 350, width, height, fill = "#001b33")
    s.update()
    sleep(0.01)
    i-=1   

#Fireworks
for i in range (10):
    x = randint(0, width)
    y = randint(0, 400)
    firework(x, y)

fadeOut()

#Scene9: Conlusion
#Text
text = s.create_text(width/2, height/3, text = "That day, the hero saved the day and created an amazing show for everyone", font = "Arial 15", fill = "white")
s.update()
sleep(5)

text2 = s.create_text(width/2, height/1.5, text = "This was the story of...", font = "Arial 25", fill = "white")

s.update()
sleep(2)
s.delete("all")

#The BIG MOMENT
sentence = ["H", "o", "w", " ", "t", "h", "e", " ", "M", "O", "o", "O", "N", " ",
            "D", "i", "s", "s", "a", "p", "p", "e", "a", "r", "e", "d"]
x = 25
for i in range (len(sentence)):
    s.create_text(x, height/2, text = sentence[i], font = "Arial 25", fill = "white")
    s.update()
    sleep(0.2)
    x += 30





