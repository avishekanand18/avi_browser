from PyQt5 import QtWidgets,QtWebEngineWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit,QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import mysql.connector

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="avi_browser")
        self.mycursor = self.conn.cursor()
        

    def show_browser(self):
        
        self.my_web = QWebEngineView()
        self.my_web.load(QUrl("https://www.google.com/"))
    
        self.setCentralWidget(self.my_web)
        
        tb=self.addToolBar("sadasd")

        back_btn = QtWidgets.QPushButton()
        back_btn.setText("Previous Page")
        back_btn.clicked.connect(self.my_web.back)
        tb.addWidget(back_btn)
        tb.addSeparator()

        forw_btn = QtWidgets.QPushButton()
        forw_btn.setText("Next Page")
        #forw_btn.setIcon(QtGui.QIcon('x.bmp'))
        forw_btn.clicked.connect(self.my_web.forward)
        tb.addWidget(forw_btn)
        tb.addSeparator()
        
        self.urlbar = QLineEdit()
        tb.addWidget(self.urlbar)
        self.urlbar.returnPressed.connect(self.nav_to_url)
        tb.addSeparator()

        s_btn = QtWidgets.QPushButton()
        s_btn.setText("Search")
        s_btn.clicked.connect(self.nav_to_url)
        tb.addWidget(s_btn)
        tb.addSeparator()

        bookmark_btn = QtWidgets.QPushButton()
        bookmark_btn.setText("Bookmark page")
        bookmark_btn.clicked.connect(self.add_bookmark)
        tb.addWidget(bookmark_btn)
        tb.addSeparator()

        hist_btn = QtWidgets.QPushButton()
        hist_btn.setText("history")
        hist_btn.clicked.connect(self.u_history)
        tb.addWidget(hist_btn)
        tb.addSeparator()

        b_btn = QtWidgets.QPushButton()
        b_btn.setText("Bookmarks")
        b_btn.clicked.connect(self.u_bookmarks)
        tb.addWidget(b_btn)
        tb.addSeparator()

        self.my_web.urlChanged.connect(self.set_url_text)


    def set_url_text(self,q):
        
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
        self.mycursor.execute("INSERT INTO history(email,u_hist) VALUES('{}','{}')".format(self.emailid,q.toString()))
        self.conn.commit()

    def nav_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.my_web.load(q)

    def u_history(self):
        #pass
        self.mycursor.execute("SELECT u_hist FROM history WHERE email LIKE '{}'".format(self.emailid))
        result=self.mycursor.fetchall()
        
        if len(result)==0:
            msg=QMessageBox()
            msg.setWindowTitle("HISTORY")
            msg.setText("history not found!")
            msg.exec_()
            
        else:
            
            s=""
            for i in range(len(result)):
                s=s+str(result[i][0])+"\n"
            
            msg=QMessageBox()
            msg.setWindowTitle("HISTORY")
            msg.setText(s)
            msg.exec_()

    def u_bookmarks(self):
        #pass
        self.mycursor.execute("SELECT DISTINCT u_book FROM bookmarks WHERE email LIKE '{}'".format(self.emailid))
        result=self.mycursor.fetchall()
        if len(result)==0:
            msg=QMessageBox()
            msg.setText("Bookmarks empty")
            msg.exec_()
            print("Bookmarks empty")
        else:
            s=""
            for i in range(len(result)):
                s=s+str(result[i][0])+"\n"
            
            msg=QMessageBox()
            msg.setWindowTitle("BOOKMARKS")
            msg.setText(s)
            msg.exec_()

    def add_bookmark(self):
        q = QUrl(self.urlbar.text())
        
        self.mycursor.execute("INSERT INTO bookmarks(email,u_book) VALUES('{}','{}')".format(self.emailid,q.toString()))
        self.conn.commit()
        
    def register_button_clicked(self):
        self.emailid = self.textbox1.text()
        self.password = self.textbox2.text()
        try:
            
            self.mycursor.execute("INSERT INTO login(email,psw) VALUES('{}','{}')".format(self.emailid,self.password))
            self.conn.commit()

        except Exception as e:
            self.b2.setText("Email Exists!\n Login -> ")

        else:
            self.b2.setText("Registration done! ")
        
    def login_button_clicked(self):

        #print("h")
        self.emailid = self.textbox1.text()
        self.password = self.textbox2.text()
        self.mycursor.execute("SELECT * FROM login WHERE email LIKE '{}' AND psw LIKE '{}'".format(self.emailid,self.password))
        if len(self.mycursor.fetchall())!=0:
            self.show_browser()
            print("f")
        else:
            self.b1.setText("wrong email or password!\n Enter again ")
            print("nf")
        
        

    def initUI(self):
        self.setGeometry(400, 100, 600, 300)
        self.setWindowTitle("AVI BROWSER")

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("EMAIL ID")
        self.label1.move(110,50)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("PASSWORD")
        self.label2.move(400,50)
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(10,120)
        self.textbox1.resize(280,40)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(300,120)
        self.textbox2.resize(280,40)        


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("login")
        self.b1.move(220,190)
        self.b1.resize(150,40)
        self.b1.clicked.connect(self.login_button_clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("new user? \n register")
        self.b2.move(220,250)
        self.b2.resize(150,40)
        self.b2.clicked.connect(self.register_button_clicked)

        
        self.show()

        


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    
    sys.exit(app.exec_())

window()
