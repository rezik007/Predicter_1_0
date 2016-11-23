from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import scipy
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.linear_model import LinearRegression

import gui

class Application(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    xTrain = []
    yTrain = []
    xTest = []
    yTest = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Events handlers
        button = self.pushButton
        button.clicked.connect(self.on_click1)
        #QtCore.QObject.connect(self.pushButton, QtCore('clicked()'), lambda msg ="" : self.SetDataSets())

    def InfoBox(self, msgText):
        self.msgText = QtWidgets.QMessageBox()
        self.msgText.setText(msgText)
        self.msgText.exec()

    def Engine(self):
        regr = linear_model.LinearRegression()

        try:
            # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
            regr.fit(self.xTrain, self.yTrain)
        except Exception:
            print("Blad wywolania zewnetrznej funkcji")


        # meanSquareError = np.mean((regr.predict(np.uint32(self.xTest)) - np.uint32(self.yTest)))
        # varianceScore = regr.score(np.uint32(self.xTest), np.uint32(self.yTest))
        #
        # self.msgText = QtWidgets.QMessageBox()
        # self.msgText.setText("The mean square error: " + str(meanSquareError) + "Variance score: " + str(varianceScore) +"Linear regression coeffitient: " + str(regr.coef_))
        # self.msgText.exec()

    def LoadDataFromFile(self):
        self.textEdit_2.setText("0")
        self.textEdit_3.setText("3")
        self.textEdit_4.setText("4")
        self.textEdit_5.setText("7")
        self.textEdit.setText("aaa.txt")
        for index, line in enumerate(open(self.textEdit.toPlainText(), "r")):
            if  index >= int(self.textEdit_2.toPlainText()) and index <= int(self.textEdit_3.toPlainText()):
                self.textBrowser.append(line)
                self.xTrain.append(line.split("|")[4])
                self.yTrain.append(line.split("|")[21])
            elif index >= int(self.textEdit_4.toPlainText()) and index <= int(self.textEdit_5.toPlainText()):
                self.textBrowser_2.append(line)
                self.xTest.append(line.split("|")[4])
                self.yTest.append(line.split("|")[21])
            else:
                continue
        self.xTrain = np.array(self.xTrain).reshape(-1, 1)
        self.yTrain = np.array(self.yTrain).reshape(-1, 1)
        regr = linear_model.LinearRegression()
        regr.fit(self.xTrain, self.yTrain)

        LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

        # meanSquareError = np.mean((regr.predict(np.uint32(xTest)) - np.uint32(yTest)))
        # varianceScore = regr.score(np.uint32(xTest), np.uint32(yTest))




    def SetDataSets(self, trainX, testX, trainY, testY):
        for line in open(self.textEdit.toPlainText(), "r"):
            trainX.append(line.split("|")[4])
            if line.split("|")[23] == "y\n":
                trainY.append(1)
            else:
                trainY.append(0)

        trainX[0] = 0
        trainX = np.array(trainX).reshape(-1, 1)
        trainY = np.array(trainY).reshape(-1, 1)
        print(trainX)
        print(trainY)

    @pyqtSlot()
    def on_click1(self):
        self.LoadDataFromFile()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainDesing = Application()
    mainDesing.show()
    sys.exit(app.exec_())

    # import numpy as np
    # import scipy
    # import matplotlib.pyplot as plt
    # from sklearn import linear_model, datasets
    # from sklearn.linear_model import LinearRegression
    #
    # xTrain = []
    # yTrain = []
    # for line in open("newLogWithoutQuestionMark.txt", "r"):
    #     xTrain.append(line.split("|")[4])
    #     if line.split("|")[23] == "y\n":
    #         yTrain.append(1)
    #     else:
    #         yTrain.append(0)
    #
    # xTrain[0] = 0
    # xTrainn = np.array(xTrain).reshape(-1, 1)
    # yTrainn = np.array(yTrain).reshape(-1, 1)
    #
    # xTest = xTrainn[101:150]
    # yTest = yTrainn[101:150]
    #
    # regr = linear_model.LinearRegression()
    # regr.fit(xTrainn[:100], yTrainn[:100])
    #
    # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    #
    # meanSquareError = np.mean((regr.predict(np.uint32(xTest)) - np.uint32(yTest)))
    # varianceScore = regr.score(np.uint32(xTest), np.uint32(yTest))
    #
    # print("The mean square error: " + str(meanSquareError))
    # print("Variance score: " + str(varianceScore))
    # print("Linear regression coeffitient: " + str(regr.coef_))
    # print(regr.predict(np.uint32(xTest)))