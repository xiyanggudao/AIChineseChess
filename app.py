import tkinter

def setWindowSize(window, width, height):
	geometry = '%dx%d' % (width, height)
	window.geometry(geometry)

def drawChess(canvas, x, y, chessSize, text, textSize, textColor):
	canvas.create_oval(x-chessSize, y-chessSize, x+chessSize, y+chessSize)
	canvas.create_text((x, y), text=text, fill=textColor, font='-family 楷体 -size '+str(textSize))

def drawOutline(canvas, width, height, border=3):
	margin=20
	canvas.create_rectangle(border+margin, border+margin, width-border-margin, height-border-margin, width=border)

def drawBackground(canvas, width, height):
	canvas.create_rectangle(0, 0, width, height, fill='grey')

def setWindowTitle(window, title):
	window.title(title)

def repaintCanvas(canvas, width, height):
	drawBackground(canvas, width, height)
	drawOutline(canvas, width, height)
	drawChess(canvas, 120, 120, 29, '相', 38, '#ff6666')

def onResize(event):
	'''
	print(type(event))
	print(event.width)
	print(event.height)
	print(event.type)
	print(type(event.widget))
	'''
	repaintCanvas(event.widget, event.width, event.height)

def onLButtonClick(event):
	print(event.x, event.y)

rootWindow = tkinter.Tk()

cv = tkinter.Canvas(rootWindow, bg='grey')
cv.update();
drawOutline(cv, 300, 400)

setWindowSize(rootWindow, 300, 400)
rootWindow.minsize(100, 200)
setWindowTitle(rootWindow, '中国象棋')

cv.bind('<Configure>', onResize)
cv.bind('<Button-1>', onLButtonClick)

cv.pack(fill=tkinter.BOTH, expand=1)
rootWindow.mainloop();
