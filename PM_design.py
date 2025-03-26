# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PM-design.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 858)
        self.mainCentralWidget = QtWidgets.QWidget(MainWindow)
        self.mainCentralWidget.setStyleSheet("background-color:black;")
        self.mainCentralWidget.setObjectName("mainCentralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainCentralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signalDisplay = QtWidgets.QWidget(self.mainCentralWidget)
        self.signalDisplay.setStyleSheet("border: 1px solid white")
        self.signalDisplay.setObjectName("signalDisplay")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.signalDisplay)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ECG = QtWidgets.QVBoxLayout()
        self.ECG.setObjectName("ECG")
        self.label = QtWidgets.QLabel(self.signalDisplay)
        self.label.setStyleSheet("color:#39FF5E;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;\n"
"border:none;")
        self.label.setObjectName("label")
        self.ECG.addWidget(self.label)
        self.ecgSignal = QtWidgets.QLabel(self.signalDisplay)
        self.ecgSignal.setStyleSheet("border:none;")
        self.ecgSignal.setObjectName("ecgSignal")
        self.ECG.addWidget(self.ecgSignal)
        self.arrythmiaType = QtWidgets.QLabel(self.signalDisplay)
        self.arrythmiaType.setStyleSheet("color:#39FF5E;\n"
"border:none;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;\n"
"border-bottom:1px solid white;")
        self.arrythmiaType.setObjectName("arrythmiaType")
        self.ECG.addWidget(self.arrythmiaType)
        self.ECG.setStretch(0, 1)
        self.ECG.setStretch(1, 8)
        self.ECG.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.ECG)
        self.SpO2 = QtWidgets.QVBoxLayout()
        self.SpO2.setObjectName("SpO2")
        self.label_4 = QtWidgets.QLabel(self.signalDisplay)
        self.label_4.setStyleSheet("color:#00B7E2;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;\n"
"border:none;")
        self.label_4.setObjectName("label_4")
        self.SpO2.addWidget(self.label_4)
        self.spo2Signal = QtWidgets.QLabel(self.signalDisplay)
        self.spo2Signal.setStyleSheet("border:none;\n"
"")
        self.spo2Signal.setObjectName("spo2Signal")
        self.SpO2.addWidget(self.spo2Signal)
        self.spo2Alarm = QtWidgets.QLabel(self.signalDisplay)
        self.spo2Alarm.setStyleSheet("color:#00B7E2;\n"
"border:none;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;\n"
"border-bottom:1px solid white;\n"
"")
        self.spo2Alarm.setObjectName("spo2Alarm")
        self.SpO2.addWidget(self.spo2Alarm)
        self.SpO2.setStretch(0, 1)
        self.SpO2.setStretch(1, 8)
        self.SpO2.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.SpO2)
        self.RR = QtWidgets.QVBoxLayout()
        self.RR.setObjectName("RR")
        self.label_6 = QtWidgets.QLabel(self.signalDisplay)
        self.label_6.setStyleSheet("color:#E8D34B;\n"
"border:none;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;")
        self.label_6.setObjectName("label_6")
        self.RR.addWidget(self.label_6)
        self.rrSignal = QtWidgets.QLabel(self.signalDisplay)
        self.rrSignal.setStyleSheet("border:none;\n"
"")
        self.rrSignal.setObjectName("rrSignal")
        self.RR.addWidget(self.rrSignal)
        self.rrAlarm = QtWidgets.QLabel(self.signalDisplay)
        self.rrAlarm.setStyleSheet("color:#E8D34B;\n"
"border:none;\n"
"font-weight:bolder;\n"
"font-size:20px;\n"
"padding-left:20px;\n"
"border-bottom:1px solid white;\n"
"")
        self.rrAlarm.setObjectName("rrAlarm")
        self.RR.addWidget(self.rrAlarm)
        self.RR.setStretch(0, 1)
        self.RR.setStretch(1, 8)
        self.RR.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.RR)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem)
        self.loadSpo2 = QtWidgets.QPushButton(self.signalDisplay)
        self.loadSpo2.setStyleSheet("color:white;\n"
"padding:15px;\n"
"\n"
"")
        self.loadSpo2.setObjectName("loadSpo2")
        self.buttons.addWidget(self.loadSpo2)
        self.laodECG = QtWidgets.QPushButton(self.signalDisplay)
        self.laodECG.setStyleSheet("color:white;\n"
"padding:15px;\n"
"\n"
"")
        self.laodECG.setObjectName("laodECG")
        self.buttons.addWidget(self.laodECG)
        self.load = QtWidgets.QPushButton(self.signalDisplay)
        self.load.setStyleSheet("color:white;\n"
"padding:15px;")
        self.load.setObjectName("load")
        self.buttons.addWidget(self.load)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem1)
        self.buttons.setStretch(0, 1)
        self.buttons.setStretch(1, 2)
        self.buttons.setStretch(2, 2)
        self.buttons.setStretch(3, 2)
        self.buttons.setStretch(4, 1)
        self.verticalLayout_4.addLayout(self.buttons)
        self.horizontalLayout.addWidget(self.signalDisplay)
        self.MeasurementsDisplay = QtWidgets.QWidget(self.mainCentralWidget)
        self.MeasurementsDisplay.setStyleSheet("border:1px solid white;")
        self.MeasurementsDisplay.setObjectName("MeasurementsDisplay")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.MeasurementsDisplay)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.heartRateMeasurements = QtWidgets.QVBoxLayout()
        self.heartRateMeasurements.setObjectName("heartRateMeasurements")
        self.label_2 = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.label_2.setStyleSheet("color:#39FF5E;\n"
"font-weight:bolder;\n"
"font-size:30px;\n"
"border-bottom:none;\n"
"padding-left:20px;")
        self.label_2.setObjectName("label_2")
        self.heartRateMeasurements.addWidget(self.label_2)
        self.HRvalue = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.HRvalue.setStyleSheet("color:#39FF5E;\n"
"font-weight:bolder;\n"
"font-size:80px;\n"
"border-top:none;\n"
"")
        self.HRvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.HRvalue.setObjectName("HRvalue")
        self.heartRateMeasurements.addWidget(self.HRvalue)
        self.verticalLayout_12.addLayout(self.heartRateMeasurements)
        self.bloodPressureMeasurements = QtWidgets.QVBoxLayout()
        self.bloodPressureMeasurements.setObjectName("bloodPressureMeasurements")
        self.label_3 = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.label_3.setStyleSheet("color:#FF3B50;\n"
"font-weight:bolder;\n"
"font-size:30px;\n"
"border-bottom:none;\n"
"padding-left:20px;")
        self.label_3.setObjectName("label_3")
        self.bloodPressureMeasurements.addWidget(self.label_3)
        self.BPvalue = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.BPvalue.setStyleSheet("color:#FF3B50;\n"
"font-weight:bolder;\n"
"font-size:80px;\n"
"border-top:none;\n"
"")
        self.BPvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.BPvalue.setObjectName("BPvalue")
        self.bloodPressureMeasurements.addWidget(self.BPvalue)
        self.verticalLayout_12.addLayout(self.bloodPressureMeasurements)
        self.spo2Measurements = QtWidgets.QVBoxLayout()
        self.spo2Measurements.setObjectName("spo2Measurements")
        self.label_5 = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.label_5.setStyleSheet("color:#00B7E2;\n"
"font-weight:bolder;\n"
"font-size:30px;\n"
"border-bottom:none;\n"
"padding-left:20px;")
        self.label_5.setObjectName("label_5")
        self.spo2Measurements.addWidget(self.label_5)
        self.spo2Value = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.spo2Value.setStyleSheet("color:#00B7E2;\n"
"font-weight:bolder;\n"
"font-size:80px;\n"
"border-top:none;\n"
"")
        self.spo2Value.setAlignment(QtCore.Qt.AlignCenter)
        self.spo2Value.setObjectName("spo2Value")
        self.spo2Measurements.addWidget(self.spo2Value)
        self.verticalLayout_12.addLayout(self.spo2Measurements)
        self.RRmeasurements = QtWidgets.QVBoxLayout()
        self.RRmeasurements.setObjectName("RRmeasurements")
        self.label_8 = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.label_8.setStyleSheet("color:#E8D34B;\n"
"font-weight:bolder;\n"
"font-size:30px;\n"
"border-bottom:none;\n"
"padding-left:20px;")
        self.label_8.setObjectName("label_8")
        self.RRmeasurements.addWidget(self.label_8)
        self.RRvalue = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.RRvalue.setStyleSheet("color:#E8D34B;\n"
"font-weight:bolder;\n"
"font-size:80px;\n"
"border-top:none;\n"
"")
        self.RRvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.RRvalue.setObjectName("RRvalue")
        self.RRmeasurements.addWidget(self.RRvalue)
        self.verticalLayout_12.addLayout(self.RRmeasurements)
        self.temperatureMeasurements = QtWidgets.QVBoxLayout()
        self.temperatureMeasurements.setObjectName("temperatureMeasurements")
        self.label_10 = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.label_10.setStyleSheet("color:#39FF5E;\n"
"font-weight:bolder;\n"
"font-size:30px;\n"
"border-bottom:none;\n"
"padding-left:20px;")
        self.label_10.setObjectName("label_10")
        self.temperatureMeasurements.addWidget(self.label_10)
        self.tempValue = QtWidgets.QLabel(self.MeasurementsDisplay)
        self.tempValue.setStyleSheet("color:#39FF5E;\n"
"font-weight:bolder;\n"
"font-size:80px;\n"
"border-top:none;\n"
"")
        self.tempValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tempValue.setWordWrap(True)
        self.tempValue.setObjectName("tempValue")
        self.temperatureMeasurements.addWidget(self.tempValue)
        self.verticalLayout_12.addLayout(self.temperatureMeasurements)
        self.horizontalLayout.addWidget(self.MeasurementsDisplay)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECG"))
        self.ecgSignal.setText(_translate("MainWindow", "TextLabel"))
        self.arrythmiaType.setText(_translate("MainWindow", "Arrythmia Dtected :"))
        self.label_4.setText(_translate("MainWindow", "SpO2"))
        self.spo2Signal.setText(_translate("MainWindow", "TextLabel"))
        self.spo2Alarm.setText(_translate("MainWindow", "Alarm :"))
        self.label_6.setText(_translate("MainWindow", "Respiratory Rate"))
        self.rrSignal.setText(_translate("MainWindow", "TextLabel"))
        self.rrAlarm.setText(_translate("MainWindow", "Alarm :"))
        self.loadSpo2.setText(_translate("MainWindow", "load ECG"))
        self.laodECG.setText(_translate("MainWindow", "load spo2"))
        self.load.setText(_translate("MainWindow", "load RR"))
        self.label_2.setText(_translate("MainWindow", "Heart Rate"))
        self.HRvalue.setText(_translate("MainWindow", "85"))
        self.label_3.setText(_translate("MainWindow", "Blood Pressure"))
        self.BPvalue.setText(_translate("MainWindow", "128 / 77"))
        self.label_5.setText(_translate("MainWindow", "SpO₂ %"))
        self.spo2Value.setText(_translate("MainWindow", "98"))
        self.label_8.setText(_translate("MainWindow", "Respiration"))
        self.RRvalue.setText(_translate("MainWindow", "22"))
        self.label_10.setText(_translate("MainWindow", "T °C"))
        self.tempValue.setText(_translate("MainWindow", "37"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
