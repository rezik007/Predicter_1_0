from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import scipy
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model



import gui

class Application(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    xTrain = []
    yTrain = []
    xTest = []
    yTest = []
    xTrainReshaped = []
    yTrainReshaped = []
    yChoose = 22

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
        print(msgText)

    def Engine(self):
        regr = linear_model.LinearRegression(fit_intercept=False)
        regr.fit(self.xTrainReshaped, self.yTrainReshaped)
        LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
        meanSquareError = np.mean((regr.predict(self.xTestReshaped) - (self.yTestReshaped))**2)
        varianceScore = regr.score((self.xTestReshaped), (self.yTestReshaped))
        yLength = len(self.yTest)


        self.InfoBox("Linear regression coeffitient: " + str(regr.coef_)+"\n\rThe mean square error: "
                     + str(meanSquareError)+"\n\rVariance score: " + str(varianceScore)+"\n\rReal Y value:"
                     +str(self.yTest[yLength-1])+"\n\rPredicted Y value:"
                     +str(regr.predict(self.xTestReshaped[self.textEdit_6.toPlainText()]))
                     +"\n\rChosen X kolumn:"+str(self.textEdit_6.toPlainText()))


    def LoadDataFromFile(self):
        self.textEdit_2.setText("1")
        self.textEdit_3.setText("10000")
        self.textEdit_4.setText("10001")
        self.textEdit_5.setText("10050")
        self.textEdit.setText("roundedNumbersLogFinal.txt")
        if self.radioButton.isChecked():
            self.yChoose = 22
        elif self.radioButton_2.isChecked():
            self.yChoose = 23

        for index, line in enumerate(open(self.textEdit.toPlainText(), "r")):
            if  index >= int(self.textEdit_2.toPlainText()) and index <= int(self.textEdit_3.toPlainText()):
                self.textBrowser.append(line)
                self.xTrain.append(int(line.split("|")[int(self.textEdit_6.toPlainText())]))
                self.yTrain.append(int(line.split("|")[int(self.yChoose)]))
            elif index >= int(self.textEdit_4.toPlainText()) and index <= int(self.textEdit_5.toPlainText()):
                self.textBrowser_2.append(line)
                self.xTest.append(int(line.split("|")[int(self.textEdit_6.toPlainText())]))
                self.yTest.append(int(line.split("|")[int(self.yChoose)]))
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
