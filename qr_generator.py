import style
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import validations

class Qr_Generator(QtWidgets.QMainWindow):
	def __init__(self):
		super(Qr_Generator,self).__init__()
		self.setWindowTitle("URL Generator")
		self.setFixedSize(580, 500)
		self.setStyleSheet(style.style)
		# Contenedor
		self.contenedor = QtWidgets.QFrame(self)
		self.contenedor.setObjectName("contenedor")
		self.contenedor.setGeometry(130,160,350,320)
		# Etiquetas
		self.labelURL=QtWidgets.QLabel("URL:",
		self)
		self.labelURL.setObjectName("labelURL")
		self.labelURL.setGeometry(40, 35, 85, 41)
		self.labelqr = QtWidgets.QLabel(self.contenedor)
		self.labelqr.setGeometry(25,20,300,300)
		# Editar texto
		self.EditUrl = QtWidgets.QLineEdit(
			self)
		self.EditUrl.setGeometry(100,32, 450, 31)
		self.EditUrl.setAlignment(
			QtCore.Qt.AlignCenter)
		
		#Botones
		self.BtnGenerar = QtWidgets.QPushButton("Generar",self)
		self.BtnGenerar.setGeometry(250, 85, 131, 41)
		self.BtnGenerar.clicked.connect(self.Generar_qr)
		self.BtnGenerar.setObjectName("BtnGenerar") 


	def Generar_qr(self):
		url = self.EditUrl.text()
		if validations.Is_URL(url):
			validations.Genrar_qrcode(url)
			self.labelqr.setPixmap(QtGui.QPixmap("url.png"))
			self.EditUrl.setFocus()
			self.EditUrl.setSelection(0, len(self.EditUrl.text()))
		else:
			self.error=QtWidgets.QMessageBox.about(self, "ERROR",
			 "¡Introduzca una URL correcta!")
			self.labelqr.clear()
			self.EditUrl.clear()


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	application = Qr_Generator()
	application.show()
	sys.exit(app.exec())



