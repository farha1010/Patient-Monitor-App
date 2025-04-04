# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PM-design.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
from scipy import stats, signal
import pandas as pd
from matplotlib.animation import FuncAnimation
from scipy.signal import find_peaks
import scipy.signal as signal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all_plots)
        self.timer.start(1000)  # 1Hz update rate
        
        # Data initialization
        self.spo2_data = []
        self.spo2_displayed_values = []
        self.current_index = 0
        self.heart_rate = None

        # ECG data initialization
        self.file_path = None
        self.ecg_data = []
        self.time_data = []
        # Initialize the ECG plot
        self.ecgSignal = pg.PlotWidget()
        self.ecg_curve = self.ecgSignal.plot(pen='r')  # Red color for ECG

        self.ecg_data = []  # Store ECG data
        self.index = 0  # Current position in the signal

        self.timer_ecg = QTimer()
        self.timer_ecg.timeout.connect(self.update_ECG_plot)

        
        # Alarm thresholds
        self.spo2_alarm_thresholds = {
            'critical_low': 85,
            'low': 90,
            'high': 100,
            'critical_high': 105
        }

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
        self.ecgSignal = pg.PlotWidget()
        self.ecgSignal.setStyleSheet("border: none;")
        self.ecgSignal.setFixedHeight(200)
        self.ecg_curve = self.ecgSignal.plot(pen=pg.mkPen(color=(255, 255, 0), width=2))
        self.ecgSignal.setBackground('black')  # Set background color
        self.ecgSignal.showGrid(x=False, y=False)  # Hide grid
        self.ecgSignal.getAxis("left").setStyle(showValues=False)  # Hide y-axis labels
        self.ecgSignal.getAxis("bottom").setStyle(showValues=False)  # Hide x-axis labels
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
        self.spo2Signal = pg.PlotWidget()
        self.spo2Signal.setFixedHeight(200)
        self.spo2_curve = self.spo2Signal.plot(pen=pg.mkPen(color=(0, 183, 226), width=2))
        self.spo2Signal.setBackground('black')  # Set background color
        self.spo2Signal.showGrid(x=False, y=False)  # Hide grid
        self.spo2Signal.getAxis("left").setStyle(showValues=False)  # Hide y-axis labels
        self.spo2Signal.getAxis("bottom").setStyle(showValues=False)  # Hide x-axis labels
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
        self.rrSignal = pg.PlotWidget()
        self.rrSignal.setFixedHeight(200)
        self.rr_curve = self.rrSignal.plot(pen=pg.mkPen(color=(255, 255, 0), width=2))
        self.rrSignal.setBackground('black')  # Set background color
        self.rrSignal.showGrid(x=False, y=False)  # Hide grid
        self.rrSignal.getAxis("left").setStyle(showValues=False)  # Hide y-axis labels
        self.rrSignal.getAxis("bottom").setStyle(showValues=False)  # Hide x-axis labels
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
        self.laodECG = QtWidgets.QPushButton(self.signalDisplay)
        self.laodECG.clicked.connect(self.open_file_dialog)
        self.laodECG.setStyleSheet("color:white;\n"
"padding:15px;\n"
"\n"
"")
        self.laodECG.setObjectName("laodECG")
        self.buttons.addWidget(self.laodECG)
        self.loadSpo2 = QtWidgets.QPushButton(self.signalDisplay)
        self.loadSpo2.clicked.connect(self.load_spo2_data)
        self.loadSpo2.setStyleSheet("color:white;\n"
"padding:15px;\n"
"\n"
"")
        self.loadSpo2.setObjectName("loadSpo2")
        self.buttons.addWidget(self.loadSpo2)
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
        self.arrythmiaType.setText(_translate("MainWindow", "Arrythmia Dtected :"))
        self.label_4.setText(_translate("MainWindow", "SpO2"))
        # self.spo2Signal.setText(_translate("MainWindow", "TextLabel"))
        self.spo2Alarm.setText(_translate("MainWindow", "Alarm :"))
        self.label_6.setText(_translate("MainWindow", "Respiratory Rate"))
        self.rrAlarm.setText(_translate("MainWindow", "Alarm :"))
        self.loadSpo2.setText(_translate("MainWindow", "load Spo2"))
        self.laodECG.setText(_translate("MainWindow", "load ECG"))
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

    def load_spo2_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Dataset", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, "r") as file:
                    self.spo2_data = [float(line.strip()) for line in file.readlines()]
                self.index = 0  # Reset index after loading new data
            except Exception as e:
                print("Error loading dataset:", e)
    
    def update_all_plots(self):
        self.update_spo2_plot()
        self.update_bp_value()
        # self.update_ECG_plot()
    
    def update_bp_value(self):
        systolic = np.random.randint(125, 130)
        diastolic = np.random.randint(75, 80)
        self.BPvalue.setText(f"{systolic} / {diastolic}")
            
            # Set color based on BP status
        if systolic > 140 or diastolic > 90:
             self.BPvalue.setStyleSheet("color:#FF0000;font-weight:bolder;font-size:80px;border-top:none;")
        else:
             self.BPvalue.setStyleSheet("color:#FF3B50;font-weight:bolder;font-size:80px;border-top:none;")
    
    def update_spo2_plot(self):
        max_points = 500
        if not self.spo2_data:
            return
        
        if self.current_index >= len(self.spo2_data):
            self.current_index = 0  # Restart if end is reached
        
        current_spo2 = self.spo2_data[self.current_index]
        self.spo2_displayed_values.append(current_spo2)
        self.current_index += 1
        
        if len(self.spo2_displayed_values) > max_points:
            self.spo2_displayed_values.pop(0)
        
        # Update plot ranges
        min_val = min(self.spo2_displayed_values) - 1
        max_val = max(self.spo2_displayed_values) + 1
        x_min = max(len(self.spo2_displayed_values) - 500, 0)
        x_max = max(len(self.spo2_displayed_values), 500)
        
        self.spo2Signal.setYRange(min_val, max_val) 
        self.spo2Signal.setXRange(x_min, x_max)
        self.spo2Signal.setLimits(xMin=x_min, xMax=x_max, yMin=min_val, yMax=max_val)
        
        # Update SpO2 value display
        self.spo2Value.setText(f"{current_spo2}")
        
        # Check for alarms and update display
        self.check_spo2_alarms(current_spo2)
        
        # Update plot
        self.spo2_curve.setData(self.spo2_displayed_values)
    
    def check_spo2_alarms(self, spo2_value):
        """Check SpO2 value against thresholds and display appropriate alarm"""
        if spo2_value < self.spo2_alarm_thresholds['critical_low']:
            alarm_text = "CRITICAL ALARM: SpO2 extremely low!"
            alarm_color = "#FF0000"  # Red
        elif spo2_value < self.spo2_alarm_thresholds['low']:
            alarm_text = "WARNING: SpO2 low"
            alarm_color = "#FFA500"  # Orange
        elif spo2_value > self.spo2_alarm_thresholds['critical_high']:
            alarm_text = "CRITICAL ALARM: SpO2 extremely high!"
            alarm_color = "#FF0000"  # Red
        elif spo2_value > self.spo2_alarm_thresholds['high']:
            alarm_text = "WARNING: SpO2 high"
            alarm_color = "#FFA500"  # Orange
        else:
            alarm_text = "Normal"
            alarm_color = "#00FF00"  # Green
        
        # Update alarm display
        self.spo2Alarm.setText(alarm_text)
        self.spo2Alarm.setStyleSheet(f"color:{alarm_color};border:none;font-weight:bolder;font-size:20px;padding-left:20px;border-bottom:1px solid white;")
        
        # Also update the value color to match alarm status
        self.spo2Value.setStyleSheet("color:#00B7E2;font-weight:bolder;font-size:80px;border-top:none;")

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Open ECG File", "", "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
                self.file_path = file_path
                self.load_ECG_data()

    def load_ECG_data(self):
        """Load ECG data from a CSV file with headers."""
        if not self.file_path:
                print("Error: No file selected.")
                return
        try:
                df = pd.read_csv(self.file_path)  # Load CSV into Pandas DataFrame
                self.time_data = df['Time'].values  # Extract time column
                self.ecg_data = df['Amplitude'].values  # Extract ECG signal column
                self.index = 0  # Reset position
                self.extract_features(self.file_path)
                self.timer_ecg.start(50)  # Start updating every 50ms

        except Exception as e:
                print("Error loading ECG file:", e)


    def extract_features(self, file_path):
        try:

            df = pd.read_csv(file_path)
            self.time_data = df['Time'].values
            self.ecg_data = df['Amplitude'].values
            fs = 1 / (self.time_data[1] - self.time_data[0])  # Sampling rate

            # Frequency-Domain Features
            freqs, psd = signal.welch(self.ecg_data, fs, nperseg=1024)
            spectral_entropy = stats.entropy(psd + 1e-10)
            dominant_freq = freqs[np.argmax(psd)]
            spectral_centroid = np.sum(freqs * psd) / np.sum(psd)
            rolloff_85 = freqs[np.where(np.cumsum(psd) >= 0.85 * np.sum(psd))[0][0]]
            rolloff_95 = freqs[np.where(np.cumsum(psd) >= 0.95 * np.sum(psd))[0][0]]
            
            # Time-Domain Features
            mean = np.mean(self.ecg_data)
            variance = np.var(self.ecg_data)
            std = np.std(self.ecg_data)
            skew = stats.skew(self.ecg_data)
            kurtosis = stats.kurtosis(self.ecg_data)
            rms = np.sqrt(np.mean(self.ecg_data**2))
            zcr = np.sum(np.diff(np.sign(self.ecg_data)) != 0) / len(self.ecg_data)
            
            # Arrhythmia Classification
            classification = self.classify_arrhythmia(dominant_freq, spectral_entropy, zcr, kurtosis, skew, rolloff_85, rolloff_95, spectral_centroid)
            arrhythmia_result = (classification)
            
            # Display Features and Arrhythmia Classification
            features_str = (
                "=== Time-Domain Features ===\n"
                f"Mean: {mean:.4f}\nVariance: {variance:.4f}\nStd Dev: {std:.4f}\n"
                f"Skewness: {skew:.4f}\nKurtosis: {kurtosis:.4f}\nRMS: {rms:.4f}\nZero-Crossing Rate: {zcr:.4f}\n\n"
                "=== Frequency-Domain Features ===\n"
                f"Spectral Entropy: {spectral_entropy:.4f}\nDominant Frequency: {dominant_freq:.4f} Hz\n"
                f"Spectral Centroid: {spectral_centroid:.4f} Hz\n"
                f"Spectral Rolloff (85%): {rolloff_85:.4f} Hz\nSpectral Rolloff (95%): {rolloff_95:.4f} Hz\n\n"
                "=== Arrhythmia Classification ===\n"
                f"{arrhythmia_result}"
            )
            alarm_color = "#00FF00"  # Green
            self.arrythmiaType.setText(f"Arrhythmia Detected: {arrhythmia_result}")
            self.arrythmiaType.setStyleSheet(f"color:{alarm_color};border:none;font-weight:bolder;font-size:20px;padding-left:20px;border-bottom:1px solid white;")


        except Exception as e:
            pass
        

    def update_ECG_plot(self):
        """Update the ECG signal dynamically with instant heart rate feedback"""
        if not hasattr(self, 'ecg_data') or len(self.ecg_data) == 0:
                return

        # Calculate sampling rate if not already set
        if not hasattr(self, 'fs'):
                if len(self.time_data) > 1:
                        self.fs = 1 / (self.time_data[1] - self.time_data[0])
                else:
                        self.fs = 250  # default sampling rate

        # Always show the complete signal up to current index
        x = np.arange(self.index + 1)
        y = self.ecg_data[:self.index + 1]
        self.ecg_curve.setData(x, y)

        # Calculate heart rate on sliding window (last 2 seconds of data)
        window_size = int(2 * self.fs)  # 2 second window
        if self.index >= window_size:
                current_window = y[-window_size:]
                heart_rate = self.calculate_heart_rate(current_window, self.fs)
                
                # Display heart rate immediately when first calculation is available
                if heart_rate is not None and heart_rate > 0:
                        self.HRvalue.setText(f"{heart_rate:.0f}")
                        # Color coding
                        if heart_rate > 100:
                                self.HRvalue.setStyleSheet("color: red; font-size: 24px;")
                        elif heart_rate < 60:
                                self.HRvalue.setStyleSheet("color: yellow; font-size: 24px;")
                        else:
                                self.HRvalue.setStyleSheet("color: green; font-size: 24px;")
                else:
                        self.HRvalue.setText("--")  # Show placeholder when no valid HR
        
        # For first 2 seconds, show "Calculating..." message
        elif self.index > 0:
                self.HRvalue.setText("Calculating...")
                self.HRvalue.setStyleSheet("color: white; font-size: 24px;")

        self.index += 1

        # Stop when we reach the end
        if self.index >= len(self.ecg_data):
                self.timer_ecg.stop()

    def calculate_heart_rate(self,ecg_signal, time_data):
        """Calculate heart rate (BPM) from an ECG signal."""
        if len(ecg_signal) < 2:
                return None  # Not enough data to process

        # Sampling rate calculation
        fs = 1 / (self.time_data[1] - self.time_data[0])  # Sampling frequency (Hz)

        # Detect R-peaks using find_peaks
        peaks, _ = signal.find_peaks(ecg_signal, height=np.mean(ecg_signal) + np.std(ecg_signal), distance=fs*0.6)  
        # distance=fs*0.6 ensures we detect R-peaks at least 0.6 sec apart

        if len(peaks) < 2:
                return self.heart_rate  # Not enough peaks to determine heart rate

        # Calculate RR intervals (time between consecutive R-peaks)
        rr_intervals = np.diff(self.time_data[peaks])  # Time differences between R-peaks

        # Convert RR intervals to heart rate (BPM)
        heart_rates = 60 / rr_intervals  # BPM calculation for each interval
        avg_heart_rate = np.mean(heart_rates)  # Average HR

        self.heart_rate = avg_heart_rate

        return avg_heart_rate


        # Arrhythmia Classification Function
    def classify_arrhythmia(self,dominant_freq, spectral_entropy, zcr, kurtosis, skewness, rolloff_85, rolloff_95, spectral_centroid): 
        classification = []
        if dominant_freq < 2.6:
                classification.append("Bradycardia")
        if 1.3 <= dominant_freq <= 2.2 and spectral_entropy > 4.0 and zcr > 0.10:
                classification.append("Atrial Flutter")
        if 1.8 <= dominant_freq <= 2.6 and spectral_entropy < 3.5 and zcr < 0.05 and kurtosis > 8:
                classification.append("Atrial Fibrillation")
        if zcr < 0.05:
                classification.append("Very Stable Rhythm")
        elif 0.05 <= zcr < 0.15:
                classification.append("Moderately Irregular")
        else:
                classification.append("Possible AFib")
        return classification
     #aa
    def update_temperature(self):
        """
        Generate a random temperature with slight variations
        Typical normal body temperature range of 36.5-37.5°C
        """
        base_temp = 37.0  # Normal body temperature
        variation = np.random.uniform(-0.5, 0.5)  # Small random variation
        current_temp = round(base_temp + variation, 1)

        # Update temperature display
        self.tempValue.setText(str(current_temp))

        # Color code temperature
        if current_temp > 38.0 or current_temp < 36.0:
            self.tempValue.setStyleSheet("color:#FF0000;font-weight:bolder;font-size:80px;border-top:none;")
        else:
            self.tempValue.setStyleSheet("color:#39FF5E;font-weight:bolder;font-size:80px;border-top:none;")

    def update_respiratory_rate(self):
        """
        Simulate respiratory rate calculation
        Typical respiratory rate: 12-20 breaths per minute
        """
        # Simulate respiratory rate calculation
        base_rate = 16  # Average respiratory rate
        variation = np.random.randint(-4, 5)  # Small random variation
        current_rate = base_rate + variation

        # Ensure rate stays within reasonable bounds
        current_rate = max(8, min(current_rate, 30))

        # Update respiratory rate display
        self.RRvalue.setText(str(current_rate))

        # Color code respiratory rate
        if current_rate < 10 or current_rate > 25:
            self.RRvalue.setStyleSheet("color:#FF0000;font-weight:bolder;font-size:80px;border-top:none;")
        else:
            self.RRvalue.setStyleSheet("color:#E8D34B;font-weight:bolder;font-size:80px;border-top:none;")

    def update_all_plots(self):
        self.update_spo2_plot()
        self.update_bp_value()
        self.update_temperature()  # Add this line
        self.update_respiratory_rate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
