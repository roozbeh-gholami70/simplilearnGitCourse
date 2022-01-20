def setColor():
    colors = ["pink","orange","purple","beige"]
    return(colors)

def pltShow(myplt, myisShow):
    if (myisShow == True):
        myplt.show()


def plotPoints(myx, myy, mySize):
    import matplotlib.pyplot as localplt
    myColor = setColor()
    localplt.scatter(myx,myy,color=myColor, s=mySize)
    return(localplt)

def setPoints():
    myx = [1, 2, 3, 4]
    myy = [1, 2, 3, 4]
    return(myx,myy)

x,y = setPoints()
plt = plotPoints(x,y,100)
pltShow(plt,True)