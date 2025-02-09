from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()


val = QLineEdit("Введіть назву валюти")
times = QLineEdit("Введіть час")
result = QLineEdit("")
vidpovid = QPushButton("Конвертація")



main_line = QVBoxLayout()
main_line.AddWinget(val)
main_line.AddWinget(times)
main_line.AddWinget(result)
main_line.AddWinget(vidpovid)
