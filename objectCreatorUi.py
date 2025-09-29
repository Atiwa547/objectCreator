try:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

class ObjectCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(300, 350)
		self.setWindowTitle('🗿Object Creator')

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = QtWidgets.QListWidget()
		self.object_listWidget.setIconSize(QtCore.QSize(60,60))
		self.object_listWidget.setSpacing(5)
		self.object_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.object_listWidget.setMovement(QtWidgets.QListView.Static)
		self.object_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)
		self.name_label = QtWidgets.QLabel('Name:')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet(
			'''
				QLineEdit {
					border-radius: 5px;
					background-color: white;
					color: navy;
					font-size: 24px;
					font-family: Oswald;
				}
			'''
		)

		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('😊 Create')
		self.create_button.setStyleSheet(
			'''
				QPushButton {
					background-color: #ED378D
				}
			'''
		)

		self.cancel_button = QtWidgets.QPushButton('❌ Cancel')
		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)

		self.initIconWidget()

	def initIconWidget(self):
		objs = ['cube', 'cone', 'sphere', 'torus']
		for obj in objs:
			item = QtWidgets.QListWidgetItem(obj)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{obj}.png')))
			self.object_listWidget.addItem(item)

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = ObjectCreatorDialog(parent=ptr)
	ui.show()