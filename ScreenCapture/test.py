# import pyscreenshot
import os, sys
from PyQt4.QtGui import *

# im = pyscreenshot.grab()
# im.show()

from multiprocessing import Process, Pipe
import time
def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    # parent_conn, child_conn = Pipe()
    # p = Process(target=f, args=(child_conn,))
    # if len(sys.argv) == 2:
    #     print sys.argv[1]
    # os.execv('E:\\ffmpeg\\bin\\ffmpeg', ('ffmpeg', '-i output.mp4 | test.py',))
    # p.start()
    # print(parent_conn.recv())   # prints "[42, None, 'hello']"
    # p.join()
    app = QApplication(sys.argv)
    dia = QDialog()
    hlay = QHBoxLayout()
    label = QLabel()
    hlay.addWidget(label)
    i = 0

    dia.setLayout(hlay)
    dia.show()
    while i < 300:

        pic = QPixmap.grabWindow(QApplication.desktop().winId())
        label.setPixmap(pic.scaled(450,300))
        i += 1
        time.sleep(.03)
    app.exec_()
