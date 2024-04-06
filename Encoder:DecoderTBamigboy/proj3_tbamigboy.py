#Toluwalase Bamigboye
#Oct 24th 2022
#Programming Assigment 3
#This assigment is a Caesar cipher code which is shifitng each letter of a plaintext mssg on a fixed number of positions in the alphabet
#this then allows the user to input a plaintext and a key value to either encode or decode
from time import *
from graphics import*
from random import randrange
def animationwindow():#animation window function for the beginning animation
    win = GraphWin("Fun",1000,1000)#sets the background/window
    win.setBackground("dark slate gray")#sets the background color
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    explanationtxt = Text(Point(500,300),"A Caesar Cipher is a type of substitutuion cipher in which each letter in the plaintext is replaced by a fixed position on the alphabet.")
    explanationtxt.setFace('arial')
    explanationtxt.setSize(15)
    explanationtxt.setStyle('bold')
    explanationtxt.setTextColor(color_rgb(r,g,b))
    explanationtxt.draw(win)
    introtxt = Text(Point(450,800),"Welcome to the Program. It is a Caesar Cipher.")
    introtxt.setFace('arial')
    introtxt.setSize(15)
    introtxt.setStyle('bold')
    introtxt.setTextColor(color_rgb(r,g,b))
    introtxt.draw(win)
    
    
    for i in range(75):#for loop for the animation and the random colors 
        r = randrange(0,255)
        g = randrange(0,255)
        b = randrange(0,255)
        introtxt.setTextColor(color_rgb(r,g,b))
        explanationtxt.setTextColor(color_rgb(r,g,b))
        introtxt.move(0,-10)
        sleep(0.07)
        explanationtxt.move(0,10)
        sleep(0.01)
    introtxt.undraw()
    explanationtxt.undraw()

    


    main(win)
    


def isClicked(button, point): #is clicked button takes two parameters button and point
    #find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    #get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()

    #calc min/max for the range of x and y
    minX = min(pt1.getX(), pt2.getX())
    maxX = max(pt1.getX(), pt2.getX())
    minY = min(pt1.getY(), pt2.getY())
    maxY = max(pt1.getY(), pt2.getY())

    #range test
    if ( minX <= x <= maxX and minY <= y <= maxY):
        return True
    else:
        return False


                
def drawButton(pt1,pt2,color,labelText,win):#functioning defining with four paramters
    button = Rectangle(pt1,pt2)#passes the paramaeter to draw a rectangle 
    button.setFill(color)#passes parameter to color the rectangle 
    button.draw(win)

    centerX = (pt1.getX() + pt2.getX()) /2
    centerY = (pt1.getY() + pt2.getY()) /2

    label = Text(Point(centerX,centerY),labelText)#passes the parameter for the text to be written on the button
    label.setFill("white")#passes the parameter to color in color of rectangle
    label.setFace('courier')#gives the parameter for a new font 
    label.draw(win)
    return button

def encode(string,key):#function defining two paraameters string and key one for the string input value and the key value for the encoder and decoder

    mssgtot = ""
    

    for ch in string:#for loop is the encoder
        if ord(ch) >= 65 and ord(ch) <= 90:
            newint = ord(ch)+int(key)
            if newint > 90:
                newint = newint - 26
            mssgtot += chr(newint)
        elif ord(ch) >= 97 and ord(ch) <= 122:
            newint = ord(ch) + int(key)
            if newint > 122:
                newint = newint - 26
            mssgtot += chr(newint)
        else:
            mssgtot = mssgtot + ch
            
    return mssgtot#return statement 

def decode(string,key):#function defining two paramaters string and key one for the string input value and one for the key value

    decodemssg = ""
    for ch in string:#for loop for decoder
        if ord(ch) >= 65 and ord(ch) <= 90:
            newint = ord(ch) - int(key)
            if newint < 65:
                newint = newint + 26
            decodemssg += chr(newint)
        elif ord(ch) >= 97 and ord(ch) <= 122:
            newint = ord(ch) - int(key)
            if newint < 97:
                newint = newint + 26
            decodemssg += chr(newint)
        else:
            decodemssg = decodemssg + ch
    return decodemssg


def main(win):#main window function

    welcometxt = Text(Point(550,100),"Welcome to my program. It is a Caesar Cipher!")#welcome text for the program
    welcometxt.setSize(25)#sets the font size
    welcometxt.setFace('arial')#sets the font
    welcometxt.setStyle('bold')#bolds the text
    welcometxt.setTextColor('white')#sets the text color to be white 
    welcometxt.draw(win)#draws the welcome txt 
    
    userInputstring = Entry(Point(200,35),50)#first user entry point for the string value
    userInputstring.draw(win)#draws entry point
    encbox = Text(Point(500,35), " < -- Encoder Box!")
    encbox.setSize(20)
    encbox.setStyle('bold')
    encbox.setTextColor('black')
    encbox.draw(win)
    
    userInputkey = Entry(Point(200,200),50)#has the user enter the key value 
    userInputkey.draw(win)#draws second entry point
    keytext = Text(Point(500,200), "< -- Key Box!")
    keytext.setSize(20)
    keytext.setStyle('bold')
    keytext.setTextColor('black')
    keytext.draw(win)
    
    encodeButton = drawButton(Point(500,300),Point(400,250),"blue","Encode",win)#calls the button function for the encode
    decodeButton = drawButton(Point(700,300),Point(600,250),"black","Decode",win)#calls the button function for the decode function
    QuitButton = drawButton(Point(900,300),Point(800,250),"blue","Quit",win)#falls the button function for quit
    FileButton = drawButton(Point(300,300),Point(200,250),"black","File",win)#calls the button function for a file button
    
    G = False
    while G != True:#while looop to allow user to continously enter and press buttons
        target = win.getMouse()#gets user click
        enc = isClicked(encodeButton,target)#calls the isClicked function for the encode button
        dec = isClicked(decodeButton,target)#calls the isClicked function for the decode button
        Q = isClicked(QuitButton,target)#calls the isClicked function for the quit button
        filebut = isClicked(FileButton,target)#calls the isCLicked function for the file button
        if isClicked(QuitButton,target):#closes the windown if quit is clicked
            win.close()
        elif isClicked(encodeButton,target):#encodes when the encode button is pressed
            string = userInputstring.getText()
            key = eval(userInputkey.getText())
            msg = encode(string,key)
            answer = Text(Point(500,650), msg)
            answer.setSize(18)
            answer.setStyle('bold')
            answer.draw(win)
            print(msg)
        elif isClicked(decodeButton,target):#decodes when the decode button is pressed 
            string = userInputstring.getText()
            key = eval(userInputkey.getText())
            msg = decode(string,key)
            answer = Text(Point(500,750), msg)
            answer.setSize(18)
            answer.setStyle('bold')
            answer.draw(win)
            print(msg)


 
animationwindow()
    

