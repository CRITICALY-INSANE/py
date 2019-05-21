import time
from PyQt5.QtCore import QDir, Qt, QUrl,QThread,pyqtSignal,pyqtSlot,QDate,QObject,QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton,QCheckBox,QComboBox,QDialogButtonBox, QBoxLayout,QLineEdit, QSplashScreen,
                             QProgressBar, QSizePolicy, QTabWidget, QSlider, QStyle, QVBoxLayout,
                                         QCalendarWidget,QVBoxLayout,QWidget,QDialog,QMainWindow,QWidget, QAction)
from PyQt5.QtWebEngineWidgets import QWebEnginePage,QWebEngineView
from PyQt5.QtGui import (QIcon,QFont,QPalette,QColor,QPixmap,)
import sys
from win32api import GetSystemMetrics
import cv2
import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import threading
import datetime

global ei,hsi,oi,ri,what,oe,ce,pe,ne,xsi,ysi,b,what
global arr,arr1,me,todo,chal
todo='nothing'
me=0
arr=[]
arr1=[]
creds=[]
ei=0
oi=0
hsi=0
chal='!'
sw=(GetSystemMetrics(0))
sh=(GetSystemMetrics(1))
lf = QFont("Times", 20, QFont.Bold)


        
class camera(QThread):
    global what
    
    list_of_dict_signals = pyqtSignal(list)
    str_signal = pyqtSignal(str)
    
    def __init__(self,  parent=None):
        QThread.__init__(self, parent)
        self.running = False
        global what

    def run(self):
        self.running = True
        self.new()
    def new(self):
           
                     
                 #an =tkinter.messagebox.askyesno("Confirmation","Do you want to proceed ?",parent=app)
                     global ei,hsi,oi,ri,what,oe,ce,pe,ne,xsi,ysi,b
                     global fck,what
                     oe=ce=0
                     cap = cv2.VideoCapture(0)
                     what="Now"
                              
                     def fck():
                             global what
                             what="Stop"         
                     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                     smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
                     eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
                     closed_cascade = cv2.CascadeClassifier('closed.xml')
                     x1=[]
                     y1=[]
                     oe=0
                     ce=0
                     pe=0
                     vw=int(0.7*sw)
                     vh=int(0.7*sh)
                     ne=0
                     cap = cv2.VideoCapture(0)
                     fourcc = cv2.VideoWriter_fourcc(*'XVID')
                     out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (vw,vh))

                     while(cap.isOpened()):
                         ret, frame = cap.read()
                         
                         if ret==True:
                             out.write(frame)

                         # Our operations on the frame come here
                             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                             faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                             for (x,y,w,h) in faces:
                                 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
                                 roi_gray = gray[y:y+h, x:x+w]
                                 roi_color = frame[y:y+h, x:x+w]
                                 smile = smile_cascade.detectMultiScale(roi_gray)
                                 eyes = eye_cascade.detectMultiScale(roi_gray)
                                 ceyes = closed_cascade.detectMultiScale(roi_gray)
                                 for (ex,ey,ew,eh) in eyes:
                                   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                                   oe=oe+1
                                   
                                 for (cex,cey,cew,ceh) in ceyes:
                                   cv2.rectangle(roi_color,(cex,cey),(cex+cew,cey+ceh),(0,0,255),2)
                                   ce=ce+1
                                   
                                 for (pex,pey,pew,peh) in smile:
                                   cv2.rectangle(roi_color,(pex,pey),(pex+pew,pey+peh),(255,0,0),2)
                                   pe=pe+1
                                   
                               
                                 x1=x1+[x]
                                 y1=y1+[y]
                                 #print (len(smile))
                                 if len(smile)==0:
                                     ne=ne+1
                                                              
                                              
                         # Display the resulting frame
                             cv2.resizeWindow('frame', 320,240)
                             cv2.moveWindow("frame", int(0.75*sw),int(0.4*sh))
                             frame=cv2.resize(frame, (320 , 240))
                             cv2.rectangle(frame,(30,0),(294,28),(0,0,25),-1)
                             #cv2.putText(frame,"Press 'Q'/'q' to Stop ",(30,19), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0),2,cv2.LINE_4)
                             
                             if cv2.waitKey(1) & 0xFF == ord('q') or what=="Stop" :
                                 break
                             elif cv2.waitKey(1) & 0xFF==ord('Q'):
                                 break
                             else:
                                pass

                     # When everything done, release the capture
                     cap.release()
                     out.release()
                     cv2.destroyAllWindows()
                     ei=(pe)/float(pe+ne+10)*95
                     oi=((oe+10)/(10+oe+ce)*98)
                     xsi=1- np.std(x1)/np.mean(x1)
                     ysi=1- np.std(y1)/np.mean(y1)
                     hsi=(xsi+ysi)/2*100
                     
                     print(oi)
                     print(ei)
                     print(hsi)

import pymongo
@pyqtSlot()

class cloud(QThread):
    global arr,me,arr1,d,c,k,chal
    
    list_of_dict_signals = pyqtSignal(list)
    str_signal = pyqtSignal(str)
    
    
    
    
    def __init__(self,  parent=None):
        
        QThread.__init__(self, parent)
        self.running1 = False       
   
    def runk():
        self.running1 = True
        self.new1()
    
    def new1():     
       if todo =='register':
          land=arr.copy()
          daate=datetime.datetime.now()
          dam=diff(land)
          
          try:
             cli = pymongo.MongoClient("mongodb+srv://anirban:<AFL6rQQQq82TqU2j>@db4ruhjhaan-9hpwe.mongodb.net/test?retryWrites=true",27017,maxPoolSize=500)
             #cli=pymongo.MongoClient("localhost",27017,maxPoolSize=500)         
             #!@%^&()_-+ it will work with db
             #...$*  this won't work 
             k=(str(dam[0]))
             k2=(str(dam[3]))
             k3=str(k+'#'+k2)
             dat=cli[k3]
             col=dat[str(arr[0])]
             lis=[{'UserName':arr[0].strip(),"Full Name":arr[1].strip(),"Password":arr[2].strip(),'Roll No':arr[3].strip(),"email":arr[4].strip(),'gender':arr[5].strip(),'Date Of Registration':daate}]
             x=col.insert_many(lis)
         
          except Exception as ex:
             print(ex)
               
    def new2():
          
          land=creds.copy()
          global chal
          daate=datetime.datetime.now()
          dam=diff(land)
          print('dam',dam)
          try:
             cli = pymongo.MongoClient("mongodb+srv://anirban:<AFL6rQQQq82TqU2j>@db4ruhjhaan-9hpwe.mongodb.net/test?retryWrites=true",27017,maxPoolSize=500)
             #cli=pymongo.MongoClient("localhost",27017,maxPoolSize=500)
             k=(str(dam[0]))
             k2=(str(dam[2]))
             k3=str(k+'#'+k2)
             dat=cli[k3]
             cool=dat[str(creds[0])]
             #lis=[{'UserName  ':arr[0],"Full Name  ":arr[1],"Password  ":arr[2],'Roll No  ':arr[3],"email  ":arr[4],'gender  ':arr[5],'Date Of Registration':daate}]
             fm=cool.find_one()
             for i,j in fm.items():
                   if "_id" in fm:
                      print('y',i,j)
                      if i=='Password':
                            print('password is-------------:>',j)
                            if j==creds[1]:
                               print('now u can pursue')
                               chal='ok'
                               print('cha;',chal)
                               #auth.bully1.setEnabled(True)
                            else:
                               pass
                            break
                   else:    
                      print("password invalid")
             
         
          except Exception as ex:
             print('now u can fuck off----',ex)          

    new1()


            
class MainWindow2(QMainWindow):

        def __init__(self, *args, **kwargs):
                super(MainWindow2, self).__init__(*args, **kwargs)
                
        @pyqtSlot()
        def kon(self,link):
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl(link))
                                
                self.qwerty=QBoxLayout(QBoxLayout.LeftToRight,self)
                self.qwerty.addWidget(self.browser)
                self.qwerty.stretch(1)
                return self.qwerty


class auth(QMainWindow):
        switch_window = pyqtSignal()
        global chal,todo
        

        def __init__(self, *args, **kwargs):
                super(auth, self).__init__(*args, **kwargs)
                self.setWindowIcon(QIcon('icon.png'))
                self.setWindowTitle('Rujhaan-- Authenticating')
                self.setFixedSize(560,500)
                self.lau=QLabel(self)
                self.lau.setText('Please Wait While  '+'\n'+'Roohjhaan is Authenticating '+'\n'+'your '+todo)
                self.k=0

                self.bully1=QPushButton("Next",self)
                self.bully1.setToolTip('Click here To Stop Analysis')
                self.bully1.setEnabled(False)
                self.bully1.clicked.connect(self.getout)

                self.cone=QPushButton("Connect",self)
                self.cone.setToolTip('Click here To Stop Analysis')
                self.cone.clicked.connect(self.noun)
                            
                self.dumdum = QProgressBar(self)
                self.dumdum.setValue(self.k)                
                self.dumdum1 = QProgressBar(self)
                self.dumdum1.setValue(self.k)
                self.dumdum2 = QProgressBar(self)
                self.dumdum2.setValue(self.k)
                self.dumdum3 = QProgressBar(self)
                self.dumdum3.setValue(self.k)

                self.dumdum3.move(50,300)
                self.dumdum2.move(70,250)
                self.dumdum1.move(70,200)
                self.dumdum.move(50,150)   
                self.bully1.move(50,100)
                self.cone.move(280,100)
                self.lau.move(50,50)
                self.lau.resize(250,50)
                self.bully1.resize(150,30)
                self.cone.resize(150,30)
                self.dumdum.resize(390,30)
                self.dumdum1.resize(350,30)
                self.dumdum2.resize(350,30)
                self.dumdum3.resize(390,30)
                
                self.timer1 = QTimer()
                self.timer1.timeout.connect(self.updateabelTime22)
                self.timer1.start(100)

                
                
                
        #self.Final()

        @pyqtSlot()
        def updateabelTime22(self):
               global chal,todo
               print(chal,todo)
               self.k=self.k+1
               if self.k==99:
                  self.k=0
                  if chal=='ok' or todo=='register':
                     print('now...')
                     self.bully1.setEnabled(True)
                  
               
               self.dumdum.setValue(self.k)
               self.dumdum1.setValue(self.k)
               self.dumdum2.setValue(self.k)
               self.dumdum3.setValue(self.k)
               self.lau.setText('Please Wait While  '+'\n'+'Roohjhaan is Authenticating '+'\n'+'your '+(todo)+('.'*self.k))

        def noun(self):
             #cas=QMessageBox.question(self, "Title", "Message",QMessageBox.Yes | QMessageBox.No)
             #cas.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
             #cloud.new1()
             cloud.new2()
             
             #self.getout()
             
             
        def getout(self):
            #cloud.new2()
            self.switch_window.emit()
        
                             
@pyqtSlot()               
class Start(QTabWidget,QMainWindow,QVideoWidget):
    switch_window = pyqtSignal()
    
    global what
    global ei,hsi,oi,ri,what,oe,ce,pe,ne,xsi,ysi,b,arr
    def __init__(self,*args):

       
        super(Start,self).__init__(*args)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Rujhaan')
    
        global fck,what
##        me=1
        #self.connect(lambda:cloud.new1())
        
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        
        self.addTab(self.tab4,"        Profile         ")
        self.addTab(self.tab2,"Lectures")                
        self.addTab(self.tab1,"Today's Performance")
        self.addTab(self.tab5,"About Us")
        self. per()
        self.lec()
        self.pro()
        self.abt()
        self.laabel=QLabel(self)
        time_str = "Current time: {0}".format(QTime.currentTime().toString())
        
        
        self.laabel.move(sw+50,0)
        self.laabel.resize(150,30)
        self.laabel.setText(time_str)
        self.updateabelTime()
        def start(self):
            global fck,new,what,oi,ei
            oi=0
            ei=0
            hsi=0
            what="Stop"
           
        self.st=QPushButton("Start",self)
        self.st.setToolTip('Click here To start Analysis')
        self.st.clicked.connect(camera.new)
        self.st.move(sw-250,0)
        self.st.resize(100,30)
       
        self.st1=QPushButton("Stop",self)
        self.st1.setToolTip('Click here To Stop Analysis')
        #self.st1.setEnabled(False)
        self.st1.clicked.connect(start)
        self.st1.move(sw-100,0)
        self.st1.resize(100,30)
       
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateabelTime)
        self.timer.start(1000)
        #self.Final()

    @pyqtSlot()
    def updateabelTime(self):
            
            time_str = "Current time: {0}".format(QTime.currentTime().toString())
            self.laabel.setText(time_str)
        
    @pyqtSlot()
    def lec(self):
       self.tab=QtWidgets.QTabWidget()
       self.tabk = QWidget()
       self.tabk2 = QWidget()                   
       self.tab.addTab(self.tabk,"Offline Lectures")
       self.tab.addTab(self.tabk2,"Online Lectures")
       q=QBoxLayout(QBoxLayout.LeftToRight,self)
       q.addWidget(self.tab)
       self.tab2.setLayout(q)
       self.ok()
       self.off()
       
    #@pyqtSlot()
    def ok(self):
          
          link="https://www.youtube.com"
          game=MainWindow2.kon(self,link)
          self.tabk2.setLayout(game)
    def off(self):
          self.now()
          
          
          
    #@pyqtSlot()
    def per(self):
       global ei,hsi,oi,ri,what,oe,ce,pe,ne,xsi,ysi,b
       self.pbar1 = QProgressBar(self)
       self.pbar1.setValue(1)
       self.pbar2 = QProgressBar(self)
       self.pbar2.setValue(1)
       self.pbar3 = QProgressBar(self)
       self.pbar3.setValue(1)
       self.bb=QLabel("Your OI is ",self)
       self.bb.setFont(QFont("Times", 10, QFont.Bold))
       
       self.bb1=QLabel("Your EI is ",self)
       self.bb1.setFont(QFont("Times", 10, QFont.Bold))
       self.bb2=QLabel("Your HSI is ",self)
       self.bb2.setFont(QFont("Times", 10, QFont.Bold))
       
       self.bba=QLabel(str(oi),self)
       self.bba.setFont(QFont("Times", 11, QFont.Bold))
       self.bb1a=QLabel(str(ei),self)
       self.bb1a.setFont(QFont("Times", 11, QFont.Bold))
       self.bb2a=QLabel(str(hsi),self)
       self.bb2a.setFont(QFont("Times", 11, QFont.Bold))
   
       self.bb4=QPushButton("Summary",self)
       self.bb4.setFont(QFont("Times", 10, QFont.Bold))
       self.bb4.clicked.connect(self.summ)       
       
       self.update_labelTime()
       
       self.time=QTimer()
       self.time.timeout.connect(self.update_labelTime)
       self.time.start(1000)

       #self.button2.clicked.connect(self.on_signup)
       bbq=QFormLayout(self)
       bbq.setContentsMargins(100, 100,700,100)
       bbq.addRow(self.bb,self.bba)
       bbq.addRow(self.pbar1)
       bbq.addRow(self.bb1,self.bb1a)
       bbq.addRow(self.pbar2)
       bbq.addRow(self.bb2,self.bb2a)
       bbq.addRow(self.pbar3)
       #bbq.addRow(self.bb3,self.bb3a)
       bbq.addRow(self.bb4)
       self.tab1.setLayout(bbq)
       
    @pyqtSlot()    
    def update_labelTime(self):
        global oi,hsi,ri,ei
        

        _oi = str(oi)
        self.bba.setText(_oi)
        _ei = str(ei)
        self.bb1a.setText(_ei)
        _hsi = str(hsi)
        self.bb2a.setText(_hsi)
        
        self.update()

    def update(self):
        global oi,hsi,ri,ei
        self.pbar1.setValue(int(oi))
        self.pbar2.setValue(int(ei))
        self.pbar3.setValue(int(hsi))
    def summ(self):
       global oi,hsi,ri,ei
       pass
       
    
    def now(self):
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()
        #self.videoWidget.setFullscreen(False)
        

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        # Create new action
        openAction = QPushButton(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.clicked.connect(self.openFile)

        
        self.setStyleSheet("QPushButton { margin: 150px; }")
        # Create a widget for window contents
        wid = QWidget(self)
        #self.setCentralWidget(wid)

        # Create layouts to place inside widget
        frm=QFormLayout()
        #frm.setContentsMargins(50, 300,100,10)
        frm.addRow(openAction,self.playButton)
        
        #50, 100,100,10
        mylay = QBoxLayout(QBoxLayout.TopToBottom)
        mylay.stretch(1)
        
        #videoWidget.setFullscreen(False)
        
        mylay.addWidget(videoWidget)
        mylay.addLayout(frm)
        mylay.addWidget(self.positionSlider)

        controlLayout = QHBoxLayout()
        controlLayout.stretch(1)
        controlLayout.setContentsMargins(0, 0, 0,0)
        controlLayout.addLayout(mylay)

        layout = QVBoxLayout()
        layout.stretch(1)
        layout.addWidget(videoWidget)
        
        layout.addWidget(self.errorLabel)
        layout.addLayout(controlLayout)
        

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        
        
        self.tabk.setLayout(layout)
        #self.show()
        
        #return self.wid
    
    def play(self):
         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
             self.mediaPlayer.pause()
         else:
            self.mediaPlayer.play()
    
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
    
       
    def pro(self):
       qq=QBoxLayout(QBoxLayout.LeftToRight,self)
       stq=QLabel("Your Details Are listed Here ",self)
       stq.setFont(QFont("Times", 50, QFont.Bold))
       self.bay = QPushButton('cloud', self)
       self.bay.setToolTip('refresh')
       self.bay.clicked.connect(cloud.new1)
       self.bay1 = QPushButton('check login', self)
       self.bay1.setToolTip('refresh')
       self.bay1.clicked.connect(cloud.new1)
   

       qq.addWidget(stq)
       qq.addWidget(self.bay)
       qq.addWidget(self.bay1)
       self.tab4.setLayout(qq)
    def abt(self):
       link="https://humosys.com/team"
       game=MainWindow2.kon(self,link)
       self.tab5.setLayout(game)
       

class first(QTabWidget):
    #global switch_window
    switch_window = pyqtSignal(int,name='regs')
    trial=pyqtSignal(int,name='logs')
    
   
    def __init__(self,*args):

       
        super(first,self).__init__(*args)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Rujhaan')
        self.setFixedSize(560,500)
        global arr
    
        global fck,what
        self.bull = QPushButton('Proceed', self)
        self.bull.setToolTip('Click here to Register And use the App')
        self.bull.move(500,260)
        

        palette = self.bull.palette()
        role = self.bull.backgroundRole() #choose whatever you like
        palette.setColor(role, QColor('Green'))
        self.bull.setPalette(palette)
        self.bull.setAutoFillBackground(False)
        self.bull.clicked.connect(self.on_out)


        self.lo = QWidget()
        self.reGGG = QWidget()
        self.dummy = QWidget()
        self.ceed = QWidget()
        
        
        #self.addTab(self.dummy,"    Welcome     ")
        self.addTab(self.lo,"        Login         ")
        self.addTab(self.reGGG,"    Register     ")
        self.addTab(self.dummy,"    Proceed   -->  ")
        
        self.orange()
        self.newbeta()       
        self.only_()
                           
    @pyqtSlot()
    def only_(self):
              self.lala=QLabel(self)
              self.lala.setText("Welcome")
              self.lala.setAlignment(Qt.AlignCenter) 
              self.lala.setFont(QFont("Times", 25, QFont.Bold))

              self.redbull = QPushButton('Sign-In', self)
              self.bluebull = QPushButton('Sign-Up', self)


              

              
              asasasas=QBoxLayout(QBoxLayout.TopToBottom)
              asasasas.addWidget(self.lala)
              

              boxeraa=QBoxLayout(QBoxLayout.LeftToRight)
              boxeraa.stretch(1)
              boxeraa.setSpacing(1)
              asasasas.addWidget(self.bull)
              boxeraa.addWidget(self.redbull)
              boxeraa.addWidget(self.bluebull)
              asasasas.addLayout(boxeraa)
              self.dummy.setLayout(asasasas)
              
              
    def orange(self):
        try:
              d='ss'
              #self.setStyleSheet("QPushButton { margin: 10px,4ex; }")
              self.label1=QLabel(self)
              self.label1.setText("Welcome")
              self.label1.setAlignment(Qt.AlignCenter) 
              self.label1.setFont(QFont("Times", 25, QFont.Bold))
              self.label2=QLabel(self)
              self.label2.setText("                        Login")       
              self.label2.setAlignment(Qt.AlignRight)
              self.label2.setFont(QFont("Times", 10, QFont.Bold))
              self.log=QLabel(self)
              self.log.setText("**Enter your credentials to login")
              self.log.setAlignment(Qt.AlignLeft)
              self.log.setFont(QFont("Times", 10, QFont.Bold))
              self.bel2=QLabel(self)
              self.bel2.setText("Username    ")
              self.bel2.setAlignment(Qt.AlignLeft)
              self.bel2.setFont(QFont("Times", 10, QFont.Bold))
              self.bel3=QLabel(self)
              self.bel3.setText("Password     ")       
              self.bel3.setAlignment(Qt.AlignCenter)
              self.bel3.setFont(QFont("Times", 10, QFont.Bold))        
              self.entry1=QLineEdit(self)
              self.entry1.setText("Username")
              self.entry1.setAlignment(Qt.AlignCenter)        
              self.entry2=QLineEdit(self)
              self.entry2.setText("Passwor")
              self.entry2.setAlignment(Qt.AlignCenter)
              self.entry2.setEchoMode(QLineEdit.Password)

              self.try1=QLineEdit(self)
              self.try1.setText("Roll Number")
              self.try1.setAlignment(Qt.AlignCenter)
              self.rol_1=QLabel(self)
              self.rol_1.setText("Roll Number   ")
              self.rol_1.setAlignment(Qt.AlignLeft)
              self.rol_1.setFont(QFont("Times", 9.8, QFont.Bold))
              
              
              self.button = QPushButton('Sign-In', self)
              self.button.setToolTip('Click here if you are an existing user')
              self.button.clicked.connect(lambda:self.on_signin())
              
              self.button3 = QPushButton('Forgot Password', self)
              self.button3.setToolTip("Click here if you don't remember your password")
              self.button3.clicked.connect(self.on_forget) 
              self.button22 = QPushButton('Reset', self)
              self.button22.setToolTip('Click here To Reset Form')
              self.c=str('logclear')
              self.button22.clicked.connect(lambda:self.on_reset1(self.c))

              
              
              
              lay1=QBoxLayout(QBoxLayout.LeftToRight)
              lay2=QBoxLayout(QBoxLayout.LeftToRight)
              lay3=QBoxLayout(QBoxLayout.LeftToRight)
              lay4=QBoxLayout(QBoxLayout.LeftToRight)
              lay5=QBoxLayout(QBoxLayout.LeftToRight)
              lay6=QBoxLayout(QBoxLayout.LeftToRight)

              
              
              
              lay1.addWidget(self.label1)        
              lay2.addWidget(self.label2)
              lay2.addWidget(self.log)
              lay3.addWidget(self.bel2)
              lay3.addWidget(self.entry1)
              lay4.addWidget(self.bel3)
              lay4.addWidget(self.entry2)

              lay6.addWidget(self.rol_1)
              lay6.addWidget(self.try1)

              
              lay5.addWidget(self.button)
              lay5.addWidget(self.button22)
              lay5.addWidget(self.button3)

              
              
              
              box1a=QBoxLayout(QBoxLayout.TopToBottom)
              boxnew=QBoxLayout(QBoxLayout.TopToBottom)
              box1a.stretch(1)
              box1a.setSpacing(50)
              #box1a.setContentsMargins(0.44*sw, 0.08*sh, 0.44*sw,0.2*sh)       
              box1a.addLayout(lay1)
              box1a.addLayout(lay2)
              box1a.addLayout(lay3)
              box1a.addLayout(lay4)
              box1a.addLayout(lay6)
              box1a.addLayout(lay5)
              
              
              
              
              #box1a.addLayout(self.newbeta.boxer)
              self.lo.setLayout(box1a)
        except Exception as dumm:
            print(dumm)
        
    #@pyqtSlot()         
    def newbeta(self):
                #self.setStyleSheet("QPushButton { margin: 450pxself.setLayout(self.box)
            try:  
                self.labe=QLabel(self)
                self.labe.setText("Welcome")
                self.labe.setAlignment(Qt.AlignCenter)
                self.labe.setFont(lf)
                self.labe.resize(160,100)
                self.label=QLabel(self)
                
                self.label.setText("**Enter your credentials to login to Register")
                self.l1=QLabel(self)
                self.l1.setText('        Registration Form')
                self.l1.resize(150,100)                
                self.l2=QLabel(self)
                self.l2.setText('                Full Name')
                self.l2.resize(150,100)
                self.l2.move(0.32*sw,0.22*sh)
                self.fnme=QLineEdit(self)
                self.fnme.setText("Full Name")
                
        
                self.l3=QLabel(self)
                self.l3.setText('                Username')
                self.us=QLineEdit(self)
                self.us.setText("Username")
                self.l4=QLabel(self)
                self.l4.setText('                Password')
                self.us1=QLineEdit(self)
                self.us1.setText("Password")
                self.us1.setEchoMode(QLineEdit.PasswordEchoOnEdit)
                
                self.l5=QLabel(self)
                self.l5.setText('    Confirm Password')
                self.l5.resize(150,100)
                self.l5.move(0.32*sw,0.40*sh)
                self.us2=QLineEdit(self)
                self.us2.setText("Confirm ")
                self.us2.setEchoMode(QLineEdit.Password)
                
                self.l6=QLabel(self)
                self.l6.setText('                    Roll No')
                self.us3=QLineEdit(self)
                self.us3.setText("Roll No")
                
                self.l7=QLabel(self)
                self.l7.setText('                    Gender')                
                self.gen=QComboBox(self)
                self.gen.addItem("        Male", )
                self.gen.addItem("      Female", )
                self.gen.addItem("      Others", )
                self.current='None'
                self.gen.activated.connect(self.handleActivated)
                
                
                self.l8=QLabel(self)
                self.l8.setText('            Date of Birth')
                self.dt = QPushButton('Calendar', self)
                self.dt.setToolTip('Click Here to see the Calendar ')
                #self.dt.clicked.connect(dante)
                                
                self.l9=QLabel(self)
                self.l9.setText('                  email ID')                
                self.us6=QLineEdit(self)
                self.us6.setText(" email ID")
                
                
                self.ag=QCheckBox("I Agree To Terms And Condition",self)
                
                
              
                self.but1 = QPushButton('Reset', self)
                self.but1.setToolTip('Click Here To Go Back To Sign-In Form')
                self.but1.resize(170,20)
                self.but1.clicked.connect(lambda:self.on_reset1('regclear'))
                   
                self.butt2 = QPushButton('Back', self)
                self.butt2.setToolTip('Click Here to Reset The Form')
                self.butt2.clicked.connect(lambda:self.on_back)
                
                self.butt3 = QPushButton('Register', self)
                self.butt3.setToolTip('Click here to Register And use the App')
                self.butt3.clicked.connect(self.on_yes)

                

                box=QBoxLayout(QBoxLayout.LeftToRight)
                box.stretch(1)
                box.setSpacing(1)
                box.addWidget(self.but1)
                box.addWidget(self.butt2)
                box.addWidget(self.butt3)
                
                
                
                
                
                ay1=QBoxLayout(QBoxLayout.LeftToRight)
                aya=QBoxLayout(QBoxLayout.LeftToRight)
                ay2=QBoxLayout(QBoxLayout.LeftToRight)
                ay3=QBoxLayout(QBoxLayout.LeftToRight)
                ay4=QBoxLayout(QBoxLayout.LeftToRight)
                ay5=QBoxLayout(QBoxLayout.LeftToRight)
                ay6=QBoxLayout(QBoxLayout.LeftToRight)
                ay7=QBoxLayout(QBoxLayout.LeftToRight)
                ay8=QBoxLayout(QBoxLayout.LeftToRight)
                ay9=QBoxLayout(QBoxLayout.LeftToRight)
                ay10=QBoxLayout(QBoxLayout.LeftToRight)
            
                ay1.addWidget(self.labe)
                aya.addWidget(self.label)
                aya.addWidget(self.l1)
                ay2.addWidget(self.l2)
                ay2.addWidget(self.fnme)
                ay3.addWidget(self.l3)
                ay3.addWidget(self.us)
                ay4.addWidget(self.l4)
                ay4.addWidget(self.us1)
                ay5.addWidget(self.l5)
                ay5.addWidget(self.us2)
                ay6.addWidget(self.l6)
                ay6.addWidget(self.us3)
                ay7.addWidget(self.l7)
                ay7.addWidget(self.gen)
                ay8.addWidget(self.l8)
                ay8.addWidget(self.dt)
                #ay8.addWidget(self.us5)
                ay9.addWidget(self.l9)
                ay9.addWidget(self.us6)
                ay10.addWidget(self.ag)
                #self.la.setContentsMargins(0.44*sw, 0.2*sh, 0.44*sw,0
                
                box1=QVBoxLayout()
                box1.stretch(1)
                box1.setSpacing(8)
                #box1.setContentsMargins(0.44*sw, 0.1*sh, 0.44*sw,0.1*sh)
                                
                box1.addLayout(ay1)
                box1.addLayout(aya)
                box1.addLayout(ay2)
                box1.addLayout(ay3)
                box1.addLayout(ay4)
                box1.addLayout(ay5)
                box1.addLayout(ay6)
                box1.addLayout(ay7)
                box1.addLayout(ay8)
                box1.addLayout(ay9)
                box1.addLayout(ay10)
                box1.addLayout(box)
                
                
                self.reGGG.setLayout(box1)
                
            except Exception as dumm1:
                print(dumm1)
    def on_back(self):
        print("back")
        #self.Login()
        #self.switch_window.emit()

    
    def handleActivated(self, index):
        self.current= self.gen.itemText(index)

    def proto(self):
       pass
       
       
    @pyqtSlot()
    def on_out(self):    

        if todo != 'nothing':   
              self.switch_window.emit(0)
        
    @pyqtSlot()   
    def on_yes(self):    
        global arr,me,todo
        todo='register'
        
        Full_Name=self.fnme.text()
        UserName=self.us.text()
        Password=self.us1.text()
        confirm=self.us2.text()
        Roll_No=self.us3.text()
        email=self.us6.text()
        gender=self.current            
        arr.append(UserName)
        arr.append(Full_Name)
        arr.append(Password)
        arr.append(Roll_No)
        arr.append(email)
        arr.append(gender)
        
        
        self.button2 = self.bluebull
        palette = self.button2.palette()
        role = self.button2.backgroundRole() #choose whatever you like
        palette.setColor(role, QColor('dark Red'))
        self.button2.setPalette(palette)
        self.button2.setAutoFillBackground(False)

        button = self.redbull
        palette = self.button.palette()
        role = self.button.backgroundRole() #choose whatever you like
        palette.setColor(role, QColor('Black'))
        button.setPalette(palette)
        self.button.setAutoFillBackground(False)
        
        
        #self.switch_window.emit(0)
   
    @pyqtSlot()
    def on_reset1(self,k):
        print("reset")
        print(k)
        if k=='logclear':
           self.entry1.setText("")
           self.entry2.setText("")
           self.try1.setText("")
        else:
           self.fnme.setText('')
           self.us.setText('')
           self.us1.setText('')
           self.us2.setText('')
           self.us3.setText('')
           self.us6.setText('')
        
        
    @pyqtSlot()
    def on_signin(self):
        global todo,d,c,k
        #print("")
        todo='login'
        print(todo)
        d=self.entry1.text()
        c=self.entry2.text()
        k=self.try1.text()
        print(d,c,k)
        try:
              creds.insert(0,d)
              creds.insert(1,c)
              creds.insert(2,k)
        except Exception as p:
            for i in range(0,3):
               creds.remove(i)
            creds.insert(0,d)
            creds.insert(1,c)
            creds.insert(2,k)
            
            
        button = self.redbull
        palette = self.button.palette()
        role = self.button.backgroundRole() #choose whatever you like
        palette.setColor(role, QColor('dark Red'))
        button.setPalette(palette)
        self.button.setAutoFillBackground(False)

        self.button2 = self.bluebull
        palette = self.button2.palette()
        role = self.button2.backgroundRole() #choose whatever you like
        palette.setColor(role, QColor('Black'))
        self.button2.setPalette(palette)
        self.button2.setAutoFillBackground(False)
  
            
        
    @pyqtSlot()
    def on_forget(self):
       pass
        
       

##class dante(QWidget):
##    switch_window = pyqtSignal()
##                          
##    def __init__(self):
##       super(dante, self).__init__()       
##       print('hence')
##       self.initUI()
##		
##    def initUI(self):
##	
##      cal = QCalendarWidget(self)
##      cal.setGridVisible(True)
##      cal.move(20, 20)
##      cal.clicked[QDate].connect(self.showDate)
##		
##      self.lbl =QLabel(self)
##      date = cal.selectedDate()
##      self.lbl.setText(date.toString())
##      self.lbl.move(120, 300)
##
##      self.close = QPushButton('Close', self)
##      self.close.setToolTip('Close the calendar')
##      self.close.move(0,0)
##      g=QBoxLayout(QBoxLayout.LeftToRight)
##      g.addWidget(self.lbl)
##      g.addWidget(cal)
##      self.setLayout(g)
##		
##      self.setGeometry(100,100,300,300)
##      self.setWindowTitle('Calendar')
##      self.setWindowIcon(QIcon('icon.png'))
##      self.show()
##      
##      #time.sleep(20)
##		
##    def showDate(self, date):	
##      self.lbl.setText(date.toString())
    
def diff(dull):
    print(dull)
    hara=[]
    for i in range(0,4):
              mj=dull[i]
              xc=len(mj)
              n='#'
              for j in range(0,xc):
                 if mj[j]==' ':
                    n+=str('!')
                
                 elif mj[j]=='.':
                    n+=str('@')
                 elif mj[j]=='*':
                    n+=str('@')
                 elif mj[j]=='$':
                    n+=str('!')
                 else:
                     n+=mj[j]
                     print('bla___'+(mj[j]))
              hara.append(str(n))
               
    return(hara)

    
class Controller:

##    def __init__(self):
##        pass
##      
        
    def show_first(self):
        self.login = first()
        
        #self.login.switch_window.connect(self.show_start)
        self.login.switch_window.connect(self.show_auth)
        self.login.show()


    def show_auth(self):
        self.authl=auth()
        self.authl.show()
        self.authl.switch_window.connect(self.show_start)
        
    def show_start(self):
        self.st = Start()
        #self.st.switch_window.connect(self.show_start)
        #self.st.setStyleSheet("background-color: #00FFFF")
        self.st.show()
        self.login.close()
        self.authl.close()
        #self.st.switch_window.connect(self.show_first)

      
    
    


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet("QPushButton { margin: 200ex; }")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)


    splash.show()
    splash.showMessage("<h1><font color='green'>Welcome!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)
    
    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
           app.processEvents()
    
    time.sleep(2)
    splash.close()
    controller = Controller()
    controller.show_first()
    sys.exit(app.exec_())
    #
    # Simulate something that takes time

if __name__ == '__main__':
    main()
