import requests
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()


app.setStyleSheet(""" 
         QWidget {
             background-color: #00FFFF;
             
        } 
        
        QPushButton
        {
            background-color: #00FF00;
            border-style: outset;
            border-width: 5px;
            border-color:black;
            border-radius: 10px;
            font-family: fantasy;
            font-size: 13px;
            min-width: 59px;
            min-height:40px;
            color: red;
            padding: 6px;
    
        }   
        
        QLineEdit
        {
            background-color: #00FF00;
            border-style: outset;
            border-width: 5px;
            border-color:black;
            border-radius: 10px;
            font-family: fantasy;
            font-size: 12px;
            min-width: 65px;
            min-height:40px;
            color: red;
            padding: 6px;
    
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

def valuta():
    val = val_input.text()
    if val.lower() != "uah":
        response = requests.get(
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&&json"
        )
        data = response.json()
        print(data)
        inputreyt = data[0]["rate"]
    else:
        inputreyt = 1

    out = times_input.text()
    if out.lower() != "uah":
        response = requests.get(
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={out}&&json"
        )
        data = response.json()
        print(data)
        outreyt = data[0]["rate"]
    else:
        outreyt = 1

    rate = outreyt/inputreyt
    kilkist = float(cilcict_input.text())
    result_input.setText(str(rate*kilkist))

vidpovid.clicked.connect(valuta)
app.exec()