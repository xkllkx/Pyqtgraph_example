import pyqtgraph as pg
import numpy as np
import array
app = pg.mkQApp()

data = array.array ('d')
N = 200
win = pg.GraphicsWindow ()
win.setWindowTitle (u'pyqtgraph畫波型')
win.resize(500, 300)

p = win.addPlot()
p.showGrid (x=True, y=True)
p.setRange (xRange=[0, N-1], yRange=[-1.2, 1.2], padding=0)
p.setLabels (left='y / V', bottom='x point', title='y = sin (x) ')

curve = p.plot (pen='y')
idx = 0
def plotData ():
    global idx
    tmp = np.sin (np.pi / 50 * idx)
    if len (data) < N:
        data.append (tmp)
    else:
        data[:-1] = data [1:]
        data[-1] = tmp
    curve.setData (data)
    idx += 1

timer = pg.QtCore.QTimer ()
timer.timeout.connect (plotData)
timer.start (30)
app.exec ()