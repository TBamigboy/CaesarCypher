#COM110 graphics exercise: button
#illustration of looping mouse clicks until an "exit" button is clicked

from graphics import *

#in the GraphWin object gwin, this function draws
#a blue rectangular button with corners at Point objects pt1 and pt2
#then labels the button with the string variable words
def drawButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(win)

    #find the x and y coords of the middle of the button
    #recall that point object has method getX() and getY()
    #and you can compute center point by averaging two Xs and two Ys
    #i.e. centerX = (pt1.getX() + pt2.getX()) / 2.0
    ### your code here



    #create a button label (text object)
    #use centerX and centerY computed above for the position of the text
    ### your code here



#function that returns a value
#tests if the point is within the rectangle object or not
def isClicked(button, point):

    #we are going to implement this soon!

    return True



def main():

    #create a window
    myWin = GraphWin("loop test", 600, 600)

    #create exit button (call drawButton function)
    #use two point coordinate (250,450) and (350,500)
    #and text 'exit'
    ###your code here

    
    #close the window only when user clicks the exit button
    #i.e., keep taking mouse clicks until exit button is clicked
    pt = myWin.getMouse()

    #we are going to write while loop for above purpose later class
        
    #exit button has been clicked at this point
    myWin.close()
    

main()
