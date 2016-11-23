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
    xTrainReshaped = []
    yTrainReshaped = []

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

    # Back up the reference to the exceptionhook
    def Engine(self):
        regr = linear_model.LinearRegression(fit_intercept=False)
        regr.fit(self.xTrainReshaped, self.yTrainReshaped)
        LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
        meanSquareError = np.mean(regr.predict((self.xTestReshaped) - (self.yTestReshaped))**2)
        varianceScore = regr.score((self.xTestReshaped), (self.yTestReshaped))

        self.InfoBox("The mean square error: " + str(meanSquareError)+"\n\rVariance score: " + str(varianceScore)+"\n\rLinear regression coeffitient: " + str(regr.coef_))

            # meanSquareError = np.mean((regr.predict(np.uint32(self.xTrain)) - np.uint32(self.yTrain)))
            # print(meanSquareError)



        # meanSquareError = np.mean((regr.predict(np.uint32(self.xTest)) - np.uint32(self.yTest)))
        # varianceScore = regr.score(np.uint32(self.xTest), np.uint32(self.yTest))
        #
        # self.msgText = QtWidgets.QMessageBox()
        # self.msgText.setText("The mean square error: " + str(meanSquareError) + "Variance score: " + str(varianceScore) +"Linear regression coeffitient: " + str(regr.coef_))
        # self.msgText.exec()

    def LoadDataFromFile(self):
        self.textEdit_2.setText("1")
        self.textEdit_3.setText("100")
        self.textEdit_4.setText("101")
        self.textEdit_5.setText("150")
        self.textEdit.setText("roundedNumbersLog.txt")

        for index, line in enumerate(open(self.textEdit.toPlainText(), "r")):
            if  index >= int(self.textEdit_2.toPlainText()) and index <= int(self.textEdit_3.toPlainText()):
                self.textBrowser.append(line)
                self.xTrain.append(int(line.split("|")[3]))
                self.yTrain.append(int(line.split("|")[22]))
            elif index >= int(self.textEdit_4.toPlainText()) and index <= int(self.textEdit_5.toPlainText()):
                self.textBrowser_2.append(line)
                self.xTest.append(int(line.split("|")[3]))
                self.yTest.append(int(line.split("|")[22]))
            else:
                continue
        self.xTrainReshaped = np.array(self.xTrain, dtype=int).reshape(-1, 1)
        self.yTrainReshaped = np.array(self.yTrain, dtype=int).reshape(-1, 1)
        self.xTestReshaped = np.array(self.xTest, dtype=int).reshape(-1, 1)
        self.yTestReshaped = np.array(self.yTest, dtype=int).reshape(-1, 1)
        self.Engine()

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