import pyaudio
import scipy.fftpack as sf
import numpy as np 
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import queue
import sys
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512   # either 1024 or 2048 didn't work.
DEVICE = 3

data = queue.Queue(16)
desiredChunk = 8192

class MyAudio(object):

    def __init__(self):
        self.x = [RATE/desiredChunk]
        for i in range(0, int(desiredChunk/2) - 2):
            self.x.append(self.x[i] + RATE/desiredChunk)

        self.audio = pyaudio.PyAudio()


        self.stream = self.audio.open(
                input=True,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE, 
                input_device_index=DEVICE,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

        print ("recording...")
        self.stream.start_stream()
        self.g = Graph()
        self.g.setButton(self)

    def update(self):
        global data
        if data.full():    
            alldata = data.get()
            for _ in range(15):
              alldata = alldata + data.get()

            self.y = sf.fft(np.fromstring(alldata, dtype=np.int16))

            self.y = np.abs(self.y)[1:int(desiredChunk/2)]
            self.g.curve.setData(self.x, self.y)
            
def callback(in_data, frame_count, time_info, status): 
    global data

    data.put(in_data)
    return (None, pyaudio.paContinue)

ZERO_POS = float( 81 )
END_POS = float( 731 )
END_VAL = float( 1400 )

class Graph(object):

    def __init__(self):
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle("My Graph")
        self.plt=self.win.addPlot() 
        self.plt.setYRange(0,400000) 
        self.plt.setXRange(0,1500)
        self.curve=self.plt.plot()

        self.win.scene().sigMouseClicked.connect(self.onClick)

    def close(self, audio):
        print("Quitting...")
        self.audio.stream.stop_stream()
        self.audio.stream.close()
        self.audio.audio.terminate()
        QtGui.QApplication.closeAllWindows()

    def setButton(self, audio):
        self.audio = audio
        self.button = QtGui.QPushButton('Close', self.win)
        self.button.move(self.win.width()/2.5, 0)
        self.button.clicked.connect(self.close)
        self.button.show()

    def onClick(self,event):
        pt1 = event.scenePos()
        print( ( pt1[0] - ZERO_POS ) * END_VAL / ( END_POS - ZERO_POS ) )


if __name__ == '__main__':

    a = MyAudio()
    timer = QtCore.QTimer()
    timer.timeout.connect(a.update)
    timer.start(10)
    if (sys.flags.interactive!=1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_() 
