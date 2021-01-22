import sys
import os 
import data_create
import logic_dataCreate
from PyQt5 import QtWidgets, QtCore
# from PyQt5.QtWidgets import (QHBoxLayout,QLabel, QApplication)
from PyQt5.QtGui import *


class ExampleApp(QtWidgets.QMainWindow, data_create.Ui_MainWindow):
	def __init__(self):
		# Это здесь нужно для доступа к переменным, методам
		# и т.д. в файле design.py
		super().__init__()
		self.setupUi(self)  # Это нужно для инициализации нашего дизайна
		self.windowImage8x8()
		self.windowMap()
		self.buttonImage()

		#buttons
		self.left_button.clicked.connect(self.clickLeft)
		self.right_button.clicked.connect(self.clickRight)
		self.up_button.clicked.connect(self.clickUp)
		self.down_button.clicked.connect(self.clickDown)

		self.line1_button.clicked.connect(self.clickLnUp)
		self.line2_button.clicked.connect(self.clickLnRght)
		self.line4_button.clicked.connect(self.clickLnUpRght)
		self.line5_button.clicked.connect(self.clickLnUpLft)

	def windowImage8x8(self):
		img8x8, img = logic_dataCreate.Part_image()
		height, width, channel = img8x8.shape
		bytesPerLine = 3 * width
		image8x8 = QImage(img8x8.data, width, height, bytesPerLine, QImage.Format_RGB888)
		pixmap = QPixmap(image8x8)
		pixmap = pixmap.scaled(400, 400)
		self.image_label.setPixmap(pixmap)

	def windowMap(self):
		img8x8, img = logic_dataCreate.Part_image()
		height, width, channel, = img.shape
		bytesPerLine = 3 * width
		image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
		pixmap = QPixmap(image)
		pixmap = pixmap.scaled(256, 256)
		self.map_label.setPixmap(pixmap)


	def labelButton(self, pixmap, button, angle, move = 14):
		self.pixmap = pixmap
		self.button = button
		self.angle = angle

		label_right = QtWidgets.QLabel(button)
		label_right.setPixmap(pixmap.transformed(QTransform().rotate(angle)))
		label_right.move(move, move)

	def buttonImage(self):
		pixmap_arrow = QPixmap("arrow_black.png").scaled(100,100)
		pixmap_stick = QPixmap("stick_black.png").scaled(100,100)

		self.labelButton(pixmap_arrow, self.up_button, 0)
		self.labelButton(pixmap_arrow, self.down_button, 180)
		self.labelButton(pixmap_arrow, self.right_button, 90)
		self.labelButton(pixmap_arrow, self.left_button, 270)

		self.labelButton(pixmap_stick, self.line1_button, 0)
		self.labelButton(pixmap_stick, self.line2_button, 90)
		self.labelButton(pixmap_stick, self.line4_button, 45, move = -5)
		self.labelButton(pixmap_stick, self.line5_button, 135, move = -5)

	def clickRight(self):
		self.image_label.clear()
		self.windowImage8x8()
		logic_dataCreate.Part_image(1,0)
		self.map_label.clear()
		self.windowMap()
	def clickLeft(self):
		self.image_label.clear()
		self.windowImage8x8()
		logic_dataCreate.Part_image(-1,0)
		self.map_label.clear()
		self.windowMap()
	def clickUp(self):
		self.image_label.clear()
		self.windowImage8x8()
		logic_dataCreate.Part_image(0,-1)
		self.map_label.clear()
		self.windowMap()
	def clickDown(self):
		self.image_label.clear()
		self.windowImage8x8()
		logic_dataCreate.Part_image(0,1)
		self.map_label.clear()
		self.windowMap()

	def clickLnUp(self):
		logic_dataCreate.SaveAnsArray(0)
	def clickLnRght(self):
		logic_dataCreate.SaveAnsArray(1)
	def clickLnUpRght(self):
		logic_dataCreate.SaveAnsArray(2)
	def clickLnUpLft(self):
		logic_dataCreate.SaveAnsArray(3)



def main():
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = ExampleApp()  # Создаём объект класса ExampleApp
	window.setWindowTitle("data creator")
	window.setWindowIcon(QIcon("dataCreator.ico"))
	window.show()  # Показываем окно
	app.exec_()  # и запускаем приложение

if __name__ == '__main__': 
	logic_dataCreate.LoadDataset() 
	# Если мы запускаем файл напрямую, а не импортируем
	main()  # то запускаем функцию main()