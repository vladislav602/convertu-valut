import requests
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()


app.setStyleSheet(""" 
         QWidget {
             background : #FFFFFF;
             
        } 
        
        QPushButton
        
        {
            backgoround-color: #00FFFF;
            border-style: outset;
            border-width: 5px;
            border-color:black;
            border-radius: 10px:
            font-family: Roboto;
            min-width: 59px;
            min-height:40px;
            color: red
            paddig: 6px;
    
        }   
                 
    """)




val_input = QLineEdit()
val_input.setPlaceholderText("Валюта з якої перевести")


times_input = QLineEdit()
times_input.setPlaceholderText("Валюта в яку перевести")


cilcict_input = QLineEdit()
cilcict_input.setPlaceholderText("Ведіть кількість")


result_input = QLineEdit()
result_input.setPlaceholderText("Результат")

vidpovid = QPushButton("Конвертація")





main_line = QVBoxLayout()
main_line.addWidget(val_input)
main_line.addWidget(times_input)
main_line.addWidget(cilcict_input)
main_line.addWidget(result_input)
main_line.addWidget(vidpovid)


window.setLayout(main_line)
window.show()
app.exec()