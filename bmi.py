# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 724)
        MainWindow.setMinimumSize(QtCore.QSize(469, 724))
        MainWindow.setMaximumSize(QtCore.QSize(469, 724))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(180, 160, 91, 41))
        self.login.setObjectName("login")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(180, 350, 91, 41))
        self.calculate.setObjectName("calculate")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 260, 341, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.weight = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.gridLayout_2.addWidget(self.weight, 0, 0, 1, 1)
        self.weight_show = QtWidgets.QLineEdit(self.layoutWidget)
        self.weight_show.setObjectName("weight_show")
        self.gridLayout_2.addWidget(self.weight_show, 0, 1, 1, 1)
        self.height = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.gridLayout_2.addWidget(self.height, 1, 0, 1, 1)
        self.height_show = QtWidgets.QLineEdit(self.layoutWidget)
        self.height_show.setObjectName("height_show")
        self.gridLayout_2.addWidget(self.height_show, 1, 1, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 440, 341, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bmi_show = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.bmi_show.setObjectName("bmi_show")
        self.gridLayout_3.addWidget(self.bmi_show, 0, 1, 1, 1)
        self.result = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.gridLayout_3.addWidget(self.result, 2, 0, 1, 1)
        self.bmi = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmi.setFont(font)
        self.bmi.setObjectName("bmi")
        self.gridLayout_3.addWidget(self.bmi, 0, 0, 1, 1)
        self.result_show = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.result_show.setObjectName("result_show")
        self.gridLayout_3.addWidget(self.result_show, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 70, 341, 81))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.id = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)
        self.id_show = QtWidgets.QLineEdit(self.widget)
        self.id_show.setObjectName("id_show")
        self.gridLayout.addWidget(self.id_show, 0, 1, 1, 1)
        self.name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.name_show = QtWidgets.QLineEdit(self.widget)
        self.name_show.setObjectName("name_show")
        self.gridLayout.addWidget(self.name_show, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "BMI CALCULATOR"))
        self.login.setText(_translate("MainWindow", "Log in"))
        self.calculate.setText(_translate("MainWindow", "RUN!!!!!"))
        self.weight.setText(_translate("MainWindow", "weight :          "))
        self.height.setText(_translate("MainWindow", "height :"))
        self.result.setText(_translate("MainWindow", "Result :"))
        self.bmi.setText(_translate("MainWindow", "BMI :          "))
        self.id.setText(_translate("MainWindow", "ID :          "))
        self.name.setText(_translate("MainWindow", "Name :"))
#............................part2...........................
#............................part2...........................
#............................part2...........................
#............................part2...........................
#............................part2...........................
        self.login.clicked.connect(self.loginfun)
        self.calculate.clicked.connect(self.calbmi)


    def loginfun(self):
        uid = self.id_show.text()
        return(uid)
    
    def calbmi(self):
        weight = int(self.weight_show.text())
        height = int(self.height_show.text())
        bmiresult = weight/((height/100)*(height/100))
        if(bmiresult<18):
            bmiid = 1
        elif(bmiresult<23):
            bmiid = 2
        elif(bmiresult<25):
            bmiid = 3
        elif(bmiresult<30):
            bmiid = 4
        elif(bmiresult>=30):
            bmiid = 5
        print("haha")
        comment = callbmi(bmiid)
        print(bmiresult)
        print(comment)
        self.bmi_show.setPlaceholderText(str(bmiresult))
        self.result_show.setPlaceholderText(comment)
        #sendbackresult(bmiid,uid=self.loginfun)

import mysql.connector

def ConnectorMysql():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bmi",
        # auth_plugin='mysql_native_password'
    )
    print("db is on the way")
    return mydb

def callbmi(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT bmicomment FROM bmicare WHERE bmiid="+str(id)+";")
    mycursor.execute(sql)
    myresult = str(mycursor.fetchall())
    finalresult = myresult[2:]
    finalresult = finalresult[:-3]
    # print(type(finalresult))
    return finalresult

def sendbackresult(bmiid,uid):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("UPDATE user SET bmiid = %s WHERE uid = %s")
    val = (bmiid, uid)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
