
# Import for the Desktop Bot
from botcity.document_processing import *
import pathlib
import pandas as pd

dados = []
def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(arquivo)


    _date = parser.get_first_entry("Date:")
    date = parser.read(_date, 1.380952, -1.8, 3.142857, 3.7)
    print('Date : ' + date)
    
    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.314815, -2.8, 6.703704, 5.1)
    print('Bill to: ' + bill_to)

    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.223684, -1.3, 5.723684, 3.5)
    print('Contact: ' + contact)

    _balance_due = parser.get_first_entry("Balance due:")
    balance_due = parser.read(_balance_due, 1.126667, -1.25, 1.666667, 3.166667)
    print('Balance due: ' + balance_due)

    dados.append([date, bill_to, contact, balance_due])


arquivos = pathlib.Path(r"C:\temp\Python\readPDF\readPDF\docs").glob('*.pdf')
for arquivo in arquivos:
        lerPDF(arquivo)
        print("=========================")

df = pd.DataFrame(dados, columns= ['Date', 'Bill to', 'Contact', 'Balance due'])
df.to_csv('data_pdf.csv', sep=',')